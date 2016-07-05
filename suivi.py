# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 21:31:11 2016

@author: jessicahoffmann
"""
import os
import sys
import time
from datetime import datetime
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
        self.dates.append(nDays)
        self.values.append(value)
        with open(self.address, "a") as f:
            f.write(toWrite)
            
    def add_otherDay(self, date, value):
        beginning = self.firstday
        nDays = countDays(beginning, date)
        toWrite = str(nDays) + " " + str(value) + "\n"
        self.dates.append(nDays)
        self.values.append(value)
        with open(self.address, "a") as f:
            f.write(toWrite)
            
    def statistics(self):
        print "average, working days:", sum(self.values)/(len(self.values) - 0.)
        print "average, overall:", sum(self.values)/(max(self.dates) + 1.)
        print "average, last 10 days:", "TODO"
#        print self.values
            
    def plot(self):
        plt.bar(self.dates, self.values, color="red", linestyle="-")
        
#%% 
def welcome():
    s = "Welcome to the Followork project!!\n\nMan, you look lovely today =D " + \
    "Is that a new haircut? \nAnyway, which project would you like to record " + \
    "today? \n\n" + \
    "-l: list all active goals \n" + \
    "name: open or create the goal name \n"
    print s
    
def actions():
    "TODO"

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
    goal.statistics()
    goal.plot()
    
    
    
        
    
    
followork()
            
#goal1 = Goal("test2")
#goal1.add(4)
#goal1.add_otherDay("2016/07/08", 5)
#goal1.add_otherDay("2016/07/06", 8)
#goal1.statistics()
#goal1.plot()
#goal1.delete()

        
        
        
        
    