# -*- coding: utf-8 -*-
import shyloo
import KBExtra
from KBEDebug import *

class GameObject:
	def __init__(self):
		pass
		
	def getScriptName(self):
		return self.__class__.__name__
		
	def onEnterWorld(self):
		"""
		shyloo method.
		这个entity已经进入世界了
		"""
		pass
		
	def onLeaveWorld(self):
		"""
		shyloo method.
		这个entity将要离开世界了
		"""
		pass
		
	def set_name(self, oldValue):
		"""
		Property method.
		服务器设置了name属性
		"""
		DEBUG_MSG("%s::set_name: %i changed:%s->%s" % (self.getScriptName(), self.id, oldValue, self.name))

	def set_modelNumber(self, oldValue):
		"""
		Property method.
		服务器设置了modelNumber属性
		"""
		DEBUG_MSG("%s::set_modelNumber: %i changed:%s->%s" % (self.getScriptName(), self.id, oldValue, self.modelNumber))
		
	def set_modelScale(self, oldValue):
		"""
		Property method.
		服务器设置了modelNumber属性
		"""
		DEBUG_MSG("%s::set_modelScale: %i changed:%s->%s" % (self.getScriptName(), self.id, oldValue, self.modelScale))
