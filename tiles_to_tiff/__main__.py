import argparse
from tiles_to_tiff import convert

parser = argparse.ArgumentParser("tiles_to_tiff", "python tiles_to_tiff https://tileserver-url.com/{z}/{x}/{y}.png 21.49147 65.31016 21.5 65.31688 -o output -z 17")
parser.add_argument("tile_source", type=str, help="Local directory pattern or URL pattern to a slippy maps tile source.", )
parser.add_argument("lng_1", type=float, help="Longitude of first bounding box corner")
parser.add_argument("lat_1", type=float, help="Latitude of first bounding box corner")
parser.add_argument("lng_2", type=float, help="Longitude of second bounding box corner")
parser.add_argument("lat_2", type=float, help="Latitude of second bounding box corner")
parser.add_argument("-z", "--zoom", type=int, help="Tilesource zoom level", default=14)
parser.add_argument("-o", "--output", type=str, help="Output directory", required=True)

args = parser.parse_args()

convert(args.tile_source, args.output, [args.lng_1, args.lat_1, args.lng_2, args.lat_2], args.zoom)