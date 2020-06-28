#
# Convert images to GIF animation.
#
# Author:
#   Julien Cohen-Adad


import os
import glob
import argparse
import imageio
import numpy as np
from scipy.ndimage import zoom


def creategif(infiles, outfile, duration, rescale_factor=1, interp=2, crop=None, save_individual_files=False):
    """

    :param infiles: list of image file names
    :param outfile: output file name. Should be gif ext.
    :param duration: in second
    :param rescale_factor: float: Rescale factor. 1: no rescaling. 0.5: 2x downsampling.
    :param interp: int: Interpolation order
    :param crop: (int, int, int, int): xmin, xmax, ymin, ymax for cropping
    :param save_individual_files: Bool: Save individual processed images.
    :return:
    """
    images = []
    for filename in infiles:
        im = imageio.imread(filename)
        # Image cropping
        if crop is not None:
            # note: x and y are swapped compared to typical image editors
            im = im.copy()[crop[2]:crop[3], crop[0]:crop[1]]
        # Image resampling
        if rescale_factor == 1:
            imr = im
        else:
            for idim in range(4):
                im2d = im[..., idim]
                if idim == 0:
                    # first assignment
                    imr = zoom(im2d, rescale_factor, order=interp)[..., np.newaxis]
                else:
                    imr = np.concatenate((imr, zoom(im2d, rescale_factor, order=interp)[..., np.newaxis]), axis=2)
        images.append(imr)
        if save_individual_files:
            outfile_indiv = ''.join([os.path.splitext(outfile)[0], '_', os.path.splitext(filename)[0], '.png'])
            imageio.imwrite(outfile_indiv, imr[:, :, 0])
    imageio.mimsave(outfile, images, 'GIF', duration=duration, subrectangles=True)
    print("File created: "+outfile)


def main():
    extension = 'png'
    infiles = '*.'+extension  # default input files
    outfile = 'anim.gif'
    duration = 0.5  # default duration (in s)
    rescale_factor = 1
    interp = 2
    crop = None

    # initiate the parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--infiles", nargs='*', help="Input files. Default="+infiles)
    parser.add_argument("-e", "--extension", type=str, help="Search all files with this extension. Default="+extension)
    parser.add_argument("-o", "--outfile", help="Output file. Default="+outfile)
    parser.add_argument("-d", "--duration", type=float, help="Duration in seconds. Default="+str(duration))
    parser.add_argument("-r", "--rescale", type=float,
                        help="Rescale factor. 1: no rescaling. 0.5: 2x downsampling. Default=".format(rescale_factor))
    parser.add_argument("-x", "--interp", type=int, choices={0, 1, 2, 3},
                        help="Interpolation method. 0: nearest neighbour, 1: linear, 2: spline. Default=".format(interp))
    parser.add_argument("-c", "--crop", type=int, nargs=4,
                        help="Crop images before creating the gif. Argument orders are: xmin, xmax, ymin, ymax.")
    parser.add_argument("-s", "--save-indiv", action='store_true', help="Save individual processed images.")

    # read arguments from the command line
    args = parser.parse_args()

    # retrieve arguments
    if args.infiles:
        infiles = args.infiles
    if args.outfile:
        outfile = args.outfile
    if args.duration:
        duration = args.duration
    if args.rescale:
        rescale_factor = args.rescale
    if args.interp:
        interp = args.interp
    if args.crop:
        crop = args.crop

    # in case using default infiles or running via IDE, need to parse names into list
    if not isinstance(infiles, list):
        infiles = [infiles]
    # then, check if "*" needs to be interpreted
    if any("*" in s for s in infiles) and len(infiles) == 1:
        infiles = glob.glob(infiles[0])

    print("Input files:\n{}".format(infiles))
    creategif(infiles, outfile, duration, rescale_factor, interp, crop, args.save_indiv)


if __name__ == "__main__":
    main()
