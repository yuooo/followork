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

def countDays(date1, date2):
    date_format = "%Y/%m/%d"
    a = datetime.strptime(date1, date_format)
    b = datetime.strptime(date2, date_format)
    delta = b - a
    return delta.days
    

class Goal:
    def __init__(self, name):
        self.name = name
        
        self.address = os.getcwd() + "/currentGoals/" + name + ".txt"
        
        self.data = []
        self.values = []
        self.dates = []
        if os.path.isfile(self.address):
            with open(self.address) as f:
                for line in f:
                    date, value = line.split()
                    self.dates.append(int(date))
                    self.values.append(int(value))
                    self.data.append([date, value])
        else:
            open(self.address, 'a').close()
        
        self.firstday = time.strftime("%Y/%m/%d")
        
        self.goal = -1
            
    
    def delete(self):
        os.remove(self.address)
        
    def add(self, value):
        currentDate = time.strftime("%Y/%m/%d")
        beginning = self.firstday
        nDays = countDays(beginning, currentDate)
        toWrite = str(nDays) + " " + str(value) + "\n"
        i = bisect(self.dates, nDays)
        self.dates.insert(i, nDays)
        self.values.insert(i, value)
        with open(self.address, "a") as f:
            f.write(toWrite)
            
    def add_otherDay(self, date, value):
        beginning = self.firstday
        nDays = countDays(beginning, date)
        i = bisect(self.dates, nDays)
        self.dates.insert(i, nDays)
        self.values.insert(i, value)
        with open(self.address, "w") as f:
            for k in range(len(self.dates)):
                toWrite = str(self.dates[k]) + " " + str(self.values[k]) + "\n"
                f.write(toWrite)
                
            
    def statistics(self):
        print "average, working days:", sum(self.values)/(len(self.values) - 0.)
        print "average, overall:", sum(self.values)/(max(self.dates) + 1.)
        print "average, last 10 days:", "TODO"
#        print self.values
            
    def plot(self):
#        plt.bar(self.dates, self.values, color="red", linestyle="-")
        axes = plt.gca()
        axes.set_xlim([0, max(self.dates) + 1])
        axes.set_ylim([0,max(self.values) + 1])
        plt.plot(self.dates, self.values, color="red", linestyle="--", marker = "o")
        plt.show()
        
    def set_firsday(self, date):
        self.firstday = date
        
#%% 
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
        elif (s1 == "firstday"):
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

        
        
        
        
    