ℹ️ If you came here from [the original tutorial](https://dev.to/jimutt/generate-merged-geotiff-imagery-from-web-maps-xyz-tile-servers-with-python-4d13) you will find the corresponding source code in the v1 branch: https://github.com/jimutt/tiles-to-tiff/tree/v1

The master branch has been updated with a small additional to offer a simple CLI.

# tiles-to-tiff
Python script for converting XYZ raster tiles for slippy maps to a georeferenced TIFF image. 

## Prerequisites:
- Python & available GDAL installation

## Usage:

```
tiles_to_tiff {tile_source} {lng_min} {lat_min} {lng_max} {lat_max} -o {output_directory} -z {zoom level}
```

Create georeferenced TIFF from online tileserver: 
```
python tiles_to_tiff https://tileserver-url.com/{z}/{x}/{y}.png 21.49147 65.31016 21.5 65.31688 -o output -z 17
```

Use local tile source:
```
python tiles_to_tiff file:///Users/Bob/local-directory 21.49147 65.31016 21.5 65.31688 -o output -z 17
```

In the tile source there is the ability to use {-y} in the URL. In TMS, the origin of coordinates is the bottom left corner so the Y coordinate goes up.

### CLI arguments:

- `lng_min` - Min longitude of bounding box
- `lat_min` - Min latitude of bounding box
- `lng_max` - Max longitude of bounding box
- `lat_max` - Max latitude of bounding box
- `-z, --zoom` - Tilesource zoom level, default 14
- `-o, --output` - Output directory, required