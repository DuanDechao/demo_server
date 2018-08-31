# -*- coding: utf-8 -*-
import shyloo
import KBExtra
from KBEDebug import *
from interfaces.GameObject import GameObject

class Gate(shyloo.Entity, GameObject):
	def __init__(self):
		shyloo.Entity.__init__(self)
		GameObject.__init__(self)
