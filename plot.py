import matplotlib.pyplot as plt

class PlotHistogram:
	def __init__(self, data, filename, xlabel, title):
		self.data		= data
		self.filename	= filename
		self.xlabel		= xlabel
		self.title		= title
		self.nb			= len(data)
		# Call mandatory methods
		self.plot()
	
	def plot(self):
		plt.figure()
		bins = len(range(int(min(self.data)),int(max(self.data))+1))
		n, bins, patches = plt.hist(self.data, bins, normed=1)

		plt.grid(True)
		plt.xlabel(self.xlabel)
		plt.ylabel('Frequency [% / 100]')
		plt.title('Histogram of {0:s}: {1:d} images used'.format(self.title, self.nb))

		#plt.show()
		plt.savefig(self.filename)

