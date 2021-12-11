import urllib.request
import os
import glob
import shutil
from tile_convert import bbox_to_xyz, tile_edges
from osgeo import gdal

temp_dir = os.path.join(os.path.dirname(__file__), 'temp')

def fetch_tile(x, y, z, tile_source):
    url = tile_source.replace(
        "{x}", str(x)).replace(
        "{y}", str(y)).replace(
        "{z}", str(z))
    path = f'{temp_dir}/{x}_{y}_{z}.png'
    urllib.request.urlretrieve(url, path)
    return(path)


def merge_tiles(input_pattern, output_path):
    vrt_path = temp_dir + "/tiles.vrt"
    gdal.BuildVRT(vrt_path, glob.glob(input_pattern))
    gdal.Translate(output_path, vrt_path)


def georeference_raster_tile(x, y, z, path):
    bounds = tile_edges(x, y, z)
    filename, extension = os.path.splitext(path)
    gdal.Translate(filename + '.tif',
                   path,
                   outputSRS='EPSG:4326',
                   outputBounds=bounds)

def convert(tile_source, output_dir, bounding_box, zoom): 
    lon_min, lat_min, lon_max, lat_max = bounding_box

    # Script start:
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    x_min, x_max, y_min, y_max = bbox_to_xyz(
        lon_min, lon_max, lat_min, lat_max, zoom)

    print(f"Fetching {(x_max - x_min + 1) * (y_max - y_min + 1)} tiles")

    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            try:
                png_path = fetch_tile(x, y, zoom, tile_source)
                print(f"{x},{y} fetched")
                georeference_raster_tile(x, y, zoom, png_path)
            except OSError:
                print(f"{x},{y} missing")
                pass

    print("Fetching of tiles complete")

    print("Merging tiles")
    merge_tiles(temp_dir + '/*.tif', output_dir + '/merged.tif')
    print("Merge complete")

    shutil.rmtree(temp_dir)
