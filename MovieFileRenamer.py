import logging,os,sys
logging.basicConfig(filename = os.path.join(os.getcwd(), 'log.txt'), level = logging.DEBUG,filemode = "w")

class MovieFileRenamer(object):
	
	def __init__(self, dirName):
		self.dirName = dirName

	def process(self):
		files=self.getFiles()
		
	def getFiles(self):
		if not os.path.exists(self.dirName):
			print("Directory not exist")
			sys.exit()
		else:
			files = files = [ f for f in os.listdir( self.dirName ) if os.path.isfile(os.path.join(self.dirName,f)) and not f.startswith('.') ]
			print("Directory contains files:")
			for f in files:
				print(f)



if __name__ == '__main__':
	dirName=input("Please input the directory:")
	renamer=MovieFileRenamer(dirName)
	renamer.process()
		