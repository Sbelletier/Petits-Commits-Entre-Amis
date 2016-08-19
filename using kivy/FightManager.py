#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Fighter import Fighter
from Utilities import Competence
from random import randint

def attack_melee( atker, defer, nbManeuvers=1, defComp = ".hld" ):
	"""
	Both atker and defer must be Fighter instances
	"""
	diceAtk, bonusAtk = atker.roll_competence(name='.atk', attrList=['Physique','Volonte'])
	scoreAtk = diceAtk + bonusAtk
	print 'Attacker rolled a ' + str(diceAtk) +' for a total of '+str(scoreAtk)
	if defComp == ".hld":
		diceDef, bonusDef = defer.roll_competence(name='.hld', attrList=['Stabilite','Volonte'])
		scoreDef = diceDef + bonusDef
		dmgMod = (scoreAtk - scoreDef)/5
		dmg = 0
		for i in range(nbManeuvers):
			diceDmg = randint(1,10)
			dmg += diceDmg
		dmg = max(dmg + dmgMod, 0)
	elif defComp == ".dodg":
		diceDef, bonusDef = defer.roll_competence(name='.dodg', attrList=['Finesse','Instinct'])
		scoreDef = diceDef + bonusDef
		if scoreAtk < scoreDef:
			dmg = 0
			dmgMod = 0
		else:
			dmgMod = (scoreAtk)/5
			dmg = 0
			for i in range(nbManeuvers):
				diceDmg = randint(1,10)
				dmg += diceDmg
			dmg = max(dmg + dmgMod, 0)
				
	print 'Defender rolled a ' + str(diceDef) +' for a total of '+str(scoreDef)
	print 'Damage taken : ' + str(dmg) + ' ( ' + str(dmgMod) + ' due to modifier)'



if __name__ == '__main__':
	a = Fighter()
	a.add_competence( Competence('.atk',12,['Physique','Volonte']) )
	a.comp['.hld'] = Competence('.hld',22,['Stabilite','Volonte'])
	print "hold 1"
	attack_melee(a, a)
	print "hold 2"
	attack_melee(a, a, nbManeuvers=5)
	print "dodge 1"
	attack_melee(a, a, defComp=".dodg")