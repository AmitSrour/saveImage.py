import sys
import os
import webbrowser
import urllib2
import threading

class MyThread(threading.Thread):
	# Override Thread's __init__ method to accept the parameters needed(urls,dest,name,ext):
	def __init__( self,url,dest,name,ext ):

		super(MyThread,self).__init__()
		self.url = url
		self.dest = dest
		self.name = name
		self.ext = ext

	def run(self):

		saveImageWrite(self.url,self.dest,self.name,self.ext)
def saveImage( url,dest,name,ext ):


	MyThread( url,dest,name,ext ).start()
	return '%s.%s'%(name,ext)


def saveImageWrite(url,dest,name,ext): ##saveImage(Original url,Destination,name, Extension) Name should include the folder Live/Profile

	opener1 = urllib2.build_opener()
	page1 = opener1.open(url)
	my_picture = page1.read()
	filename = "%s%s.%s" %(dest,name,ext)
	fout = open(filename, "wb")
	fout.write(my_picture)
	fout.close()
	#return '%s.%s'%(name,ext) ## should return the functional destination ex: images/Live/1231231.jpg

if __name__ == "__main__":
	if len(sys.argv) <2:
		print "filesystem.py url destination filename"
	if len(sys.argv) == 2:
		print "job done succesfully saved in %s"% saveImage(sys.argv[1],sys.argv[2])
	if len(sys.argv) == 3:
		print "job done succesfully saved in %s"% saveImage(sys.argv[1],sys.argv[2],sys.argv[3])
