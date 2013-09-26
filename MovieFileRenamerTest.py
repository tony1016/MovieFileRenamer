#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import MovieFileRenamer

class MovieFileRenamerTest(unittest.TestCase):
	def test_get_video_file_metadata(self):
		metadata=MovieFileRenamer.getVideoMetadata("How It Feels [through Glass].mp4")
		# print(metadata.get("width"))
		self.assertTrue(metadata)

	def test_shuold_get_10_result_from_tmdb(self):
		result=MovieFileRenamer.searchMovieInTmdb("Fight Club")
		self.assertTrue(result)
		self.assertEqual(10,result["total_results"])

	def test_genarate_file_name(self):
		fakeTmdbInfo={"original_title":"original title","title":"title","release_date":"2013-09-01"}
		newname=MovieFileRenamer.generateFileName("How It Feels [through Glass].mp4", fakeTmdbInfo)
		self.assertEqual("original.title.title.2013.720p.avc1.mp4",newname)

if __name__ == '__main__':
	unittest.main()