#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Fighter(object):
	def __init__(self):
		self.stats = dict()
		stat_names = ['Vitesse', 'Physique', 'Stabilite', 'Finesse', 'Volonte', 'Instinct', 'Perception', 'Apparence']
		for k in stat_names:
			self.stats[k] = 4
			
	def derive_secondary_stats(self):
		pass #Will insert max life and other stuff here