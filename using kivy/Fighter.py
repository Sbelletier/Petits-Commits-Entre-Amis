#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Utilities import Gauge
from random import randint

class Fighter(object):
	def __init__(self):
		self.stats = dict()
		self.stat_names = ['Vitesse', 'Physique', 'Stabilite', 'Finesse', 'Volonte', 'Instinct', 'Perception', 'Apparence']
		for k in self.stat_names:
			self.stats[k] = 4
		self.derive_secondary_stats()
		#Let's define heat as a Gauge to get the neat redefinition of += and -=
		self.heat = Gauge(max=333, filled=False)#Nobody will ever reach that max so it's ok
		self.comp = dict()
			
			
	def derive_secondary_stats(self):
		maxHP = 10*(self.stats['Physique']+self.stats['Stabilite']+self.stats['Volonte'])
		maxSP = 15*(self.stats['Physique']+self.stats['Stabilite']+self.stats['Volonte'])#SP stands for Strain Points Heh
		self.hp = Gauge(max=maxHP,filled=True)
		self.sp = Gauge(max=maxSP, filled=False)
		pass #Will insert max life and other stuff here
		
	def roll_initiative(self):
		return randint(1,20), self.stats['Vitesse']+self.stats['Instinct']
	
	def roll_competence(self, name='.atk', attrList=[]):
		bonus = 0
		if name in self.comps.keys():
			for attr in self.comp[name].attrList:
				if attr in self.stat_names:
					bonus += self.stats[attr]
			bonus += self.comp[name].value
		else:
			for attr in attrList:
				if attr in self.stat_names:
					bonus += self.stats[attr]
		return randint(1,100), bonus
		