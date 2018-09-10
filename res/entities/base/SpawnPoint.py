# -*- coding: utf-8 -*-
import shyloo
from KBEDebug import *
from interfaces.GameObject import GameObject

class SpawnPoint(shyloo.Base, GameObject):
	def __init__(self):
		shyloo.Base.__init__(self)
		GameObject.__init__(self)
		self.createCellEntity(self.createToCell)
	
	def callRPCTest(self, index):
		print("BASE call Rpc.... ", index)
		self.cell.onCallRPCTest(index)
		

