#!/usr/bin/env python

from exif import *
from plot import *
import argparse

def doFocalLengthHistogram(el):
	histo, nbValues = el.focalLengthHistogram()
	# txt
	f = open('focallength.txt', 'w')
	f.write('{0:d} images prises en compte\n'.format(nbValues))
	f.write('{0:d} longueurs de focale differentes\n'.format(len(histo)))
	f.write('\n')
	f.write('FocalLength\tNumberOfImages\n')
	f.write('-----------\t--------------\n')
	for k,v in sorted(histo.iteritems()):
		f.write('{0:3d}\t\t\t{1:d}\n'.format(k,v))
	f.close()
	# png
	PlotHistogram(el.focalLengthValues(), 'focallength.png', 'Focal length [mm]', 'Focal Lengths')

def doApertureHistogram(el):
	histo, nbValues = el.apertureHistogram()
	# txt
	f = open('aperture.txt', 'w')
	f.write('{0:d} images prises en compte\n'.format(nbValues))
	f.write('{0:d} ouvertures differentes\n'.format(len(histo)))
	f.write('\n')
	f.write('Aperture\tNumberOfImages\n')
	f.write('-----------\t--------------\n')
	for k,v in sorted(histo.iteritems()):
		f.write('{0:4.1f}\t\t\t{1:d}\n'.format(k,v))
	f.close()
	# png
	PlotHistogram(el.apertureValues(), 'aperture.png', 'Aperture [1:value]', 'Apertures')

def main():
	parser = argparse.ArgumentParser(description='Read EXIF metadata of image files')
	parser.add_argument('-f', '--files',
						nargs='*',
						required=True,
						dest='files', 
						help='Files to read')
	args = parser.parse_args()

	###

	el = ExifList(args.files)
	# Focal Length
	doFocalLengthHistogram(el)
	# Aperture
	doApertureHistogram(el)

if __name__ == '__main__':
	main()

