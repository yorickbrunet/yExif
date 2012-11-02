import pyexiv2

class ExifData:
	def __init__(self, metadata):
		if 'Exif.Image.Artist' in metadata:
			self.Artist				= str(metadata['Exif.Image.Artist'].value)
		else:
			self.Artist				= ''
		if 'Exif.CanonPr.ColorTemperature' in metadata:
			self.ColorTemperature	= int(metadata['Exif.CanonPr.ColorTemperature'].value)
		else:
			self.ColorTemperature	= 0
		if 'Exif.Image.DateTime' in metadata:
			self.DateTime			= str(metadata['Exif.Image.DateTime'].value)
		else:
			self.DateTime			= ''
		if 'Exif.Photo.DateTimeOriginal' in metadata:
			self.DateTimeOriginal	= str(metadata['Exif.Photo.DateTimeOriginal'].value)
		else:
			self.DateTimeOriginal	= ''
		if 'Exif.Photo.ExposureBiasValue' in metadata:
			self.ExposureBiasValue	= str(metadata['Exif.Photo.ExposureBiasValue'].value)
		else:
			self.ExposureBiasValue	= ''
		if 'Exif.Photo.ExposureTime' in metadata:
			self.ExposureTime		= str(metadata['Exif.Photo.ExposureTime'].value)
		else:
			self.ExposureTime		= ''
		if 'Exif.Photo.FocalLength' in metadata:
			self.FocalLength		= int(int(metadata['Exif.Photo.FocalLength'].value))
		else:
			self.FocalLength		= 0
		if 'Exif.Photo.FNumber' in metadata:
			self.FNumber			= float(metadata['Exif.Photo.FNumber'].value)
		else:
			self.FNumber			= 0.0
		if 'Exif.Image.ImageWidth' in metadata:
			self.ImageWidth			= int(metadata['Exif.Image.ImageWidth'].value)
		else:
			self.ImageWidth			= 0
		if 'Exif.Image.ImageLength' in metadata:
			self.ImageLength		= int(metadata['Exif.Image.ImageLength'].value)
		else:
			self.ImageLength		= 0
		if 'Exif.Photo.ISOSpeedRatings' in metadata:
			self.ISOSpeedRatings	= int(metadata['Exif.Photo.ISOSpeedRatings'].value)
		else:
			self.ISOSpeedRatings	= 0
		if 'Exif.Canon.LensModel' in metadata:
			self.LensModel			= str(metadata['Exif.Canon.LensModel'].value)
		else:
			self.LensModel			= ''
		if 'Exif.CanonCs.LensType' in metadata:
			self.LensType			= int(metadata['Exif.CanonCs.LensType'].value)
		else:
			self.LensType			= 0
		if 'Exif.Image.Model' in metadata:
			self.Model				= str(metadata['Exif.Image.Model'].value)
		else:
			self.Model				= ''
		if 'Exif.Image.Orientation' in metadata:
			self.Orientation		= bool(metadata['Exif.Image.Orientation'].value)
		else:
			self.Orientation		= False

#		self.ExposureProgram	= metadata['Exif.Photo.ExposureProgram'].value
#		self.MeteringMode	= metadata['Exif.Photo.MeteringMode'].value
#		self.Flash		= metadata['Exif.Photo.Flash'].value
	
	def __str__(self):
		return \
			'ImageWidth ........... {0:d} px\n'.format(self.ImageWidth) + \
			'ImageLength .......... {0:d} px\n'.format(self.ImageLength) + \
			'ExposureTime ......... {0:s} s\n'.format(self.ExposureTime) + \
			'FNumber .............. {0:.1f}\n'.format(self.FNumber) + \
			'FocalLength .......... {0:d}\n'.format(self.FocalLength) + \
			'ISOSpeedRatings ...... {0:d} ISO\n'.format(self.ISOSpeedRatings) + \
			'ExposureBiasValue .... {0:s}\n'.format(self.ExposureBiasValue) + \
			'Orientation .......... {0:d}\n'.format(self.Orientation) + \
			'ColorTemperature ..... {0:d}\n'.format(self.ColorTemperature) + \
			'DateTimeOriginal ..... {0:s}\n'.format(self.DateTimeOriginal) + \
			'DateTime ............. {0:s}\n'.format(self.DateTime) + \
			'Artist ............... {0:s}\n'.format(self.Artist) + \
			'Model ................ {0:s}\n'.format(self.Model) + \
			'LensModel ............ {0:s}\n'.format(self.LensModel) + \
			'LensType ............. {0:d}\n'.format(self.LensType)
#			'ExposureProgram: {0:}\n'.format(self.ExposureProgram) + \
#			'MeteringMode: {0:}\n'.format(self.MeteringMode) + \
#			'Flash: {0:}\n'.format(self.Flash) + \

class ExifList:
	def __init__(self, files):
		self.files	= files
		self.data	= []
		# Call mandatory methods
		self.process()
	
	def process(self):
		for f in self.files:
			md = pyexiv2.ImageMetadata(f)
			md.read()
			self.data.append(ExifData(md))
	
	def calcHistogram(self, li):
		histo = dict()
		for val in li:
			if val in histo:
				histo[val] += 1
			else:
				histo[val] = 1
		return histo, len(li)

	def focalLengthValues(self):
		li = []
		for d in self.data:
			if d.FocalLength > 0:
				li.append(d.FocalLength)
		return li
	
	def focalLengthHistogram(self):
		return self.calcHistogram(self.focalLengthValues())
	
	def apertureValues(self):
		li = []
		for d in self.data:
			if d.FNumber > 0:
				li.append(d.FNumber)
		return li
	
	def apertureHistogram(self):
		return self.calcHistogram(self.apertureValues())

