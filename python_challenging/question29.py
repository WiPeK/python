#!/usr/bin/env python
# -*- coding: utf-8 -*-
class American:
	@staticmethod
	def printNationality():
		print("USA")

class State(American):
	@staticmethod
	def printState():
		print("NY")

American.printNationality()
State.printNationality()
State.printState()