# -*- coding: utf-8 -*-
import sys
import shyloo

def printMsg(args, isPrintPath):
	for m in args:print (m)

def TRACE_MSG(*args): 
	shyloo.scriptLogType(shyloo.LOG_TYPE_NORMAL)
	printMsg(args, False)
	
def DEBUG_MSG(*args): 
	if shyloo.publish() == 0:
		shyloo.scriptLogType(shyloo.LOG_TYPE_DBG)
		printMsg(args, True)
	
def INFO_MSG(*args): 
	if shyloo.publish() <= 1:
		shyloo.scriptLogType(shyloo.LOG_TYPE_INFO)
		printMsg(args, False)
	
def WARNING_MSG(*args): 
	shyloo.scriptLogType(shyloo.LOG_TYPE_WAR)
	printMsg(args, True)

def ERROR_MSG(*args): 
	shyloo.scriptLogType(shyloo.LOG_TYPE_ERR)
	printMsg(args, True)
