#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Gauge(object):
	def __init__(self, max=100, filled=True):
		self.__dict__['max'] = max
		if filled:
			self.__dict__['curr'] = max
		else:
			self.curr = 0
	
	def __setattr__(self, name, value):
		if name == 'curr':
			if value > self.max:
				self.__dict__[name] = self.max
			else:
				self.__dict__[name] = max(0, value)
		elif name == 'max':
			if value < self.curr:
				self.curr = value
			self.__dict__[name] = value
		else:
			self.__dict__[name] = value
			
	def __iadd__(self, other):#redefines += operand
		self.curr = self.curr + other
		return self
		
	def __isub__(self, other):
		self.curr = self.curr - other
		return self
		
	def __str__(self):
		string = "Gauge "+str(self.curr)+"/"+str(self.max)
		return string

class Bonus(object):
	pass #probably duration, effect and targetStat as attributes probably only an abstract class