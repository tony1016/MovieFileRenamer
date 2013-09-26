#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import MovieFileRenamer

class MovieFileRenamerTest(unittest.TestCase):
	def test_get_video_file_metadata(self):
		metadata=MovieFileRenamer.getVideoMetadata("Discover the North Island Rotorua to Auckland.3gp")
		# print(metadata.get("width"))
		self.assertTrue(metadata)

	def test_shuold_get_10_result_from_tmdb(self):
		result=MovieFileRenamer.searchMovieInTmdb("Fight Club")
		self.assertTrue(result)
		self.assertEqual(10,result["total_results"])

	def test_genarate_file_name(self):
		fakeTmdbInfo={"original_title":"Discover the North Island Rotorua to Auckland","title":"title","release_date":"2013-09-01"}
		newname=MovieFileRenamer.generateFileName("Discover the North Island Rotorua to Auckland.3gp", fakeTmdbInfo)
		self.assertEqual("Discover.the.North.Island.Rotorua.to.Auckland.title.2013.144p.mp4v.3gp",newname)

if __name__ == '__main__':
	unittest.main()