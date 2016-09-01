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
		
	def add_competence(self, comp):
		#Note : adds or change the competence with comp.name as a name
		#TODO for this and remove comp : kwargs
		self.comp[comp.name] = comp.copy()
	
	def remove_competence(self, compName):
		if compName in self.comp.keys():
			del self.comp[compName]
		
	def roll_initiative(self):
		return randint(1,20), self.stats['Vitesse']+self.stats['Instinct']
	
	def roll_competence(self, name='.atk', attrList=[]):
		#TODO use kwargs
		bonus = 0
		if name in self.comp.keys():
			for attr in self.comp[name].attrList:
				if attr in self.stat_names:
					bonus += self.stats[attr]
			bonus += self.comp[name].value
		else:
			for attr in attrList:
				if attr in self.stat_names:
					bonus += self.stats[attr]
		return randint(1,100), bonus
		
	def take_damage(self, dmg):
		self.hp -= dmg
		if self.hp.curr <= 0:
			return 'killed'
		else:
			return 'hit'
			
	def __getitem__(self, key):
		if key in self.stat_names:
			return self.stats[key]
		elif key in self.comp.keys():
			return self.comp[key]
		else:
			raise KeyError('Key not in fighter stats/comps')
	
	def __setitem__(self, key, value):
		if key in self.stat_names:
			self.stats[key] = value
		elif key in self.comp.keys():
			self.comp[key].value = value
		else:
			raise KeyError('Key not in fighter stats/comps')
			
		