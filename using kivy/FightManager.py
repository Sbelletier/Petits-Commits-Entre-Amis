#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Fighter import Fighter
from Utilities import Competence

def attack_melee( atker, defer ):
	"""
	Both atker and defer must be Fighter instances
	"""
	diceAtk, bonusAtk = atker.roll_competence(name='.atk', attrList=['Physique','Volonte'])
	scoreAtk = diceAtk + bonusAtk
	print 'Attacker rolled a ' + str(diceAtk) +' for a total of '+str(scoreAtk)
	diceDef, bonusDef = defer.roll_competence(name='.hld', attrList=['Stabilite','Volonte'])
	scoreDef = diceDef + bonusDef
	print 'Defender rolled a ' + str(diceDef) +' for a total of '+str(scoreDef)
	



if __name__ == '__main__':
	a = Fighter()
	a.comp['.atk'] = Competence('.atk',10,['Physique','Volonte'])
	a.comp['.hld'] = Competence('.hld',22,['Stabilite','Volonte'])
	attack_melee(a, a)