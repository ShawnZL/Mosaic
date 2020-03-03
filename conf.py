# GEN TILES CONFS

# number of divisions per color (R, G and B)
# DEPTH = 4 -> 4 * 4 * 4 = 64 colors
DEPTH = 128
# list of rotations, in degrees, to apply over the original image
ROTATIONS = [0]#旋转角度，


#############################


# TILER CONFS

# number of colors per image
COLOR_DEPTH = 128
# tiles scales (1 = default resolution)
RESIZING_SCALES = [0.1]
# number of pixels shifted to create each box (tuple with (x,y))
# if value is None, shift will be done accordingly to tiles dimensions
PIXEL_SHIFT = None
# if tiles can overlap
OVERLAP_TILES = False
# render image as its being built
RENDER = True
# multiprocessing pool size
POOL_SIZE = 128

# out file name
OUT = 'out.png'
# image to tile (ignored if passed as the 1st arg)
IMAGE_TO_TILE = None
# folder with tiles (ignored if passed as the 2nd arg)
TILES_FOLDER = None
