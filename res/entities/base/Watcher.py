# -*- coding: utf-8 -*-
import shyloo
from KBEDebug import *

def countPlayers():
	"""
	shyloo.addWatcher("players", "UINT32", countPlayers)
	上面代码将这个函数添加到监视器中，可以从GUIConsole等工具中实时监视到函数返回值
	"""
	i = 0
	for e in shyloo.entities.values():
		if e.__class__.__name__ == "Avatar":
			i += 1

	return i
	


def setup():
	shyloo.addWatcher("players", "UINT32", countPlayers)
