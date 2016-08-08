# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 21:31:11 2016

@author: jessicahoffmann
"""
import os
import sys
import time
from datetime import datetime
from bisect import bisect
import numpy as np
import matplotlib.pyplot as plt
import pickle
import Goal
 
def welcome():
    s = "Welcome to the Followork project!!\n\nMan, you look lovely today =D " + \
    "Is that a new haircut? \nAnyway, which project would you like to record " + \
    "today? \n\n" + \
    "-l: list all active goals \n" + \
    "name: open or create the goal name \n"
    print s
    
def actions():
    s = "What would you like to do?"
    print s

def followork():
    welcome()
    s = sys.stdin.readline().strip()
    if s.startswith("-l"):
        for f in os.listdir("currentGoals/"):
            if f.endswith(".txt"):
                print(os.path.splitext(f)[0])
        print
        print "Which project would you like to choose?"
        s = sys.stdin.readline().strip()
    goal = Goal(s)
    actions()
    s1 = ""
    while s1 != "quit":
        s1 = sys.stdin.readline().strip()
        if (s1 == "add"):
            v = int(input())
            goal.add(v)
            print "Value added"
            print
        elif (s1 == "addo"):
            d, v = sys.stdin.readline().split()
            goal.add_otherDay(d, int(v))
            print "Value added"
            print
        elif (s1 == "show"):
            goal.statistics()
            goal.plot()
        elif (s1 == "firstDay"):
            d = sys.stdin.readline().strip()
            goal.set_firsday(d)
            print "Date set."
            print
    
    
    
        
    
    
followork()
            
#goal1 = Goal("test")
#goal1.add(4)
#goal1.add_otherDay("2016/07/08", 4)
#goal1.add_otherDay("2016/07/06", 8)
#goal1.statistics()
#goal1.plot()
#goal1.delete()

        
        
        
        
    