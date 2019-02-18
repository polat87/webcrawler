########################################################################
#							   Crawler								   #
#						GOEKHAN POLAT (0830690)						   #
########################################################################

# -*- coding: UTF-8 -*-
"#!/usr/bin/env python"
#import sys
import codecs
import urllib2
import numpy as np
import networkx as nX
import xml.dom.minidom
from networkx import *
import matplotlib.pyplot as plt
from urllib2 import HTTPError
from random import randint
import random
reload(sys)
sys.setdefaultencoding("utf-8")
#from collections import deque

API_KEY = 'f7b363e31c8830bc2021998fb0e33159'
API_URL = 'http://ws.audioscrobbler.com/2.0/?'

TOP_FANS_URL = API_URL + 'api_key=' + API_KEY + '&method=artist.getTopFans&artist='
TOP_ARTISTS_URL = API_URL + 'api_key=' + API_KEY + '&method=user.getTopArtists&user='
FRIENDS_URL = API_URL + 'api_key=' + API_KEY + '&method=user.getFriends&user='

NETWORK_A_ADJMAT = '../networks/networkA.csv'
NETWORK_A_ACTORS = '../networks/actorLabelsA.txt'
NETWORK_A_EVENTS = '../networks/eventLabelsA.txt'
NETWORK_B_ADJMAT = '../networks/networkB.csv'
NETWORK_B_LABELS = '../networks/nodeLabelsB.txt'


def main():
	two_mode = TwoModeNetwork()
	two_mode.startCrawling()
	two_mode.storeAdjMatrixToFile()
	two_mode.storeActorLabels()
	two_mode.storeEventLabels()
	one_mode = OneModeNetwork()
	one_mode.startCrawling()
	one_mode.storeAdjMatrixToFile()
	one_mode.storeActorLabels()

class OneModeNetwork():
	def __init__(self):
		self.graph = nX.Graph()
		self.user_list = []
		self.user_list.append('Jelvins')
	
	def startCrawling(self):		

		while(1):
						
			if (number_of_nodes(self.graph) > 100):
				if(self.getAvgDegree() > 1.5):
					if(is_connected(self.graph)):
						break;		
			
			user = self.user_list[randint(0, len(self.user_list)-1)]			

			friends = []
			try:
				friends = self.getFriends(user)
			except HTTPError, err:
				friends = []
			
			cnt = 3;
			
			for i in range(0, len(friends)):
				randfriend = friends[randint(0, len(friends)-1)]
				if randfriend not in self.user_list:
					self.user_list.append(randfriend);
					self.graph.add_edge(user, randfriend);
				
				cnt-= 1;
				if(cnt == 0):
					break;	
				
	def getAvgDegree(self):
		sum = 0;
		for i in range(0, len(self.user_list)):
			sum += len(nX.neighbors(self.graph, self.user_list[i]))
		return float(sum) / float(len(self.user_list))

	def getFriends(self, fan):
		url = FRIENDS_URL + fan
		url = url.replace(' ','%20')
		doc = xml.dom.minidom.parseString(urllib2.urlopen(url).read())
		elements =  doc.getElementsByTagName('name')
		return [title.childNodes[0].data for title in elements]	

	def storeAdjMatrixToFile(self):
		users = self.user_list
		csv = ''
		for i in range(0,  len(users)):
			nbors = nX.neighbors(self.graph,  self.user_list[i])		
			for j in range(0,  len(users)):
				if users[j] not in nbors:
					csv+='0'
				else:
					csv+='1'
				if j < len(users)-1:
					csv+=','
			csv+= '\n'		

		file = codecs.open(NETWORK_B_ADJMAT, 'w',  'utf-8') 
		file.write(csv)
		file.close()

	def storeActorLabels(self):
		file = codecs.open(NETWORK_B_LABELS,  'w',  'utf-8')
		for i in range(0,  len(self.user_list)):
			file.write(str(self.user_list[i])+'\n')
		file.close()
		
class TwoModeNetwork():
	def __init__(self):
		self.graph = nX.Graph()
		self.artist_list = ['Shakira']
		self.fans_list = []
		self.finish = False;
		
	def storeAdjMatrixToFile(self):
		csv = ''		
		for i in range(0, len(self.fans_list)):
			nbors = nX.neighbors(self.graph,  self.fans_list[i])
			for j in range(0, len(self.artist_list)):
				if self.artist_list[j] not in nbors:
					csv+= '0'
				else:
					csv+= '1'
				if j < len(self.artist_list)-1:
					csv+= ','				
			csv+= '\n'
			
		file = codecs.open(NETWORK_A_ADJMAT, 'w',  'utf-8') 
		file.write(csv)
		file.close()
	
	def storeActorLabels(self):
		file = codecs.open(NETWORK_A_ACTORS,  'w',  'utf-8')
		for i in range(0,  len(self.fans_list)):
			file.write(str(self.fans_list[i])+'\n')
		file.close()
		
	def storeEventLabels(self):
		file = codecs.open(NETWORK_A_EVENTS,  'w',  'utf-8')
		for i in range(0,  len(self.artist_list)):
			file.write(str(self.artist_list[i]) + '\n')
		file.close()

	def startCrawling(self):
		while self.finish == False:
			self.crawlByArtists()
			self.crawlByFans()
			if (len(self.fans_list) > 100) & (len(self.artist_list) > 100):
				if(self.getAvgPartRate() > 1.5) & (self.getAvgEvents() > 1.5):
					if(is_connected(self.graph)):
						self.finish = True

	def getAvgPartRate(self):
		sum = 0;
		for i in range(0, len(self.fans_list)):
			sum += len(nX.neighbors(self.graph, self.fans_list[i]))
		return float(sum) / float(len(self.fans_list))

	def getAvgEvents(self):
		sum = 0;
		for i in range(0, len(self.artist_list)):
			sum += len(nX.neighbors(self.graph, self.artist_list[i]))
		return float(sum) / float(len(self.artist_list))

	def crawlByArtists(self):
		artist = self.artist_list[randint(0, len(self.artist_list)-1)]
		if artist not in self.artist_list:
			self.artist_list.append(artist)
		
		fans = []
		try:
			fans = self.getArtistFans(artist)
		except HTTPError, err:
			return
			
		if(len(fans) >= 5):
			for f in range(0, randint(2,5)):
				self.graph.add_edge(artist, fans[f])
				if fans[f] not in self.fans_list:
					self.fans_list.append(fans[f])

	def crawlByFans(self):
		fan = self.fans_list[randint(0, len(self.fans_list)-1)]					
		if fan not in self.fans_list:
			self.fans_list.append(fan)
		artists = []			
		try:
			artists = self.getFansArtists(fan)
		except HTTPError, err:
			return
		
		if(len(artists) >= 5):
			for a in range(0, randint(2,5)):
				self.graph.add_edge(fan, artists[a])
				if artists[a] not in self.artist_list:
					self.artist_list.append(artists[a])

	def getArtistFans(self, artist):
		url = TOP_FANS_URL + artist
		url = url.replace(' ','%20')
		doc = xml.dom.minidom.parseString(urllib2.urlopen(url).read())
		elements =  doc.getElementsByTagName('name')
		return [title.childNodes[0].data for title in elements]


	def getFansArtists(self, fan):
		url = TOP_ARTISTS_URL + fan + '&limit=10'
		url = url.replace(' ','%20')
		doc = xml.dom.minidom.parseString(urllib2.urlopen(url).read())
		elements =  doc.getElementsByTagName('name')
		return [title.childNodes[0].data for title in elements]	

if __name__ == '__main__':
	main()
	
