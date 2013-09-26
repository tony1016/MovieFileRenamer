#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob
import enzyme
import urllib2,urllib,json,os

def listFiles(dir):
	return glob.glob(dir)


def getVideoMetadata(file):
	return enzyme.parse(file).convert()

def searchMovieInTmdb(searchKey):
	headers = {"Accept": "application/json"}
	data={"api_key":"2d47f493560c897a2b6471bc6dc66bf7","query":searchKey,"language":"zh"}
	request=urllib2.Request("http://api.themoviedb.org/3/search/movie?"+urllib.urlencode(data), headers=headers)
	response=urllib2.urlopen(request).read().decode('utf-8')
	jsonResult=json.loads(response)
	return jsonResult

def process(file):
	selectedItem=None
	while not selectedItem:
		searchKey=raw_input("Please input the search key:")
		result=searchMovieInTmdb(searchKey)
		while result["total_results"]==0:
			searchKey=raw_input("Please input the search key:")
			result=searchMovieInTmdb(searchKey)

		seq=1
		for movie in result["results"]:
			print(str(seq)+"\t"\
				+movie["original_title"]+"\t"\
				+movie["title"]+"\t"\
				+movie["release_date"])
			seq=seq+1
		print(str(0)+"\t input again")

		replaceId=input("Please input the choice:")
		if replaceId==0:
			continue
		else:
			selectedItem=result["results"][replaceId-1]
			break

	newname=generateFileName(file, selectedItem)
	newname=os.path.join(os.path.dirname(file),newname)
	print(newname)
	prompt=raw_input("Change to ?(y/n)")
	if prompt=="y":
		os.rename(file, newname)

def generateFileName(file,tmdbInfo):
	metadata=getVideoMetadata(file)
	# print(metadata)
	fileName, fileExtension = os.path.splitext(file)
	newname=tmdbInfo["original_title"]\
	+" "+tmdbInfo["title"]\
	+" "+tmdbInfo["release_date"][0:4]\
	+" "+str(metadata["video"][0]["height"])+"p"\
	+" "+metadata["video"][0]["codec"]\
	+fileExtension
	return newname.replace(" ", ".")


def promptConfirmation(file):
	result=raw_input("R U sure to process this file:"+file+"?(y/n)")
	if result=="y":
		return True
	else:
		return False


if __name__ == '__main__':
	dir=raw_input("Please input the dir:")
	files=listFiles(dir+"/*")
	for file in files:
		if promptConfirmation(file):
			process(file)