import argparse
from tiles_to_tiff import convert

parser = argparse.ArgumentParser("tiles_to_tiff", "python tiles_to_tiff https://tileserver-url.com/{z}/{x}/{y}.png 21.49147 65.31016 21.5 65.31688 -o output -z 17")
parser.add_argument("tile_source", type=str, help="Local directory pattern or URL pattern to a slippy maps tile source.", )
parser.add_argument("lng_min", type=float, help="Min longitude of bounding box")
parser.add_argument("lat_min", type=float, help="Min latitude of bounding box")
parser.add_argument("lng_max", type=float, help="Max longitude of bounding box")
parser.add_argument("lat_max", type=float, help="Max latitude of bounding box")
parser.add_argument("-z", "--zoom", type=int, help="Tilesource zoom level", default=14)
parser.add_argument("-o", "--output", type=str, help="Output directory", required=True)

args = parser.parse_args()

tile_source = args.tile_source if args.tile_source.startswith("http") else "file:///" + args.tile_source

convert(tile_source, args.output, [args.lng_min, args.lat_min, args.lng_max, args.lat_max], args.zoom)