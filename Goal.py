# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 19:24:48 2016

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

def countDays(date1, date2):
    date_format = "%Y/%m/%d"
    a = datetime.strptime(date1, date_format)
    b = datetime.strptime(date2, date_format)
    delta = b - a
    return delta.days
    
    
class Goal:
    """
    FIELDS:
    - name: name of the work
    - data: list
    - values: list of values of work
    - dates: ordered list of days. Day 0 is starting date
    - address: string representing where the project is
    - firstDay: date of the first day (time module)
    
    METHODS:
    - __init__(self, name)
    - delete(self)
    - add(self, value)
    - add_otherDay(self, date, value)
    - set_firsday(self, date)
    - statistics(self)
    - plot(self)
    """
    
    def __init__(self, name):
        firstLine = True
        
        self.name = name
        
        self.address = os.getcwd() + "/currentGoals/" + name + ".txt"
        
        self.data = []
        self.values = []
        self.dates = []
        if os.path.isfile(self.address):
            with open(self.address) as f:
                for line in f:
                    if firstLine:
                        self.firstDay = time.strftime(line)
                        firstLine = False
                    date, value = line.split()
                    self.dates.append(int(date))
                    self.values.append(int(value))
                    self.data.append([date, value])
        else:
            self.firstDay = time.strftime("%Y/%m/%d")
            f = open(self.address, 'a')
            f.write(self.firstDay)
            f.close()
            
            
        
        self.goal = -1
            
    
    def delete(self):
        os.remove(self.address)
        
    def add(self, value):
        currentDate = time.strftime("%Y/%m/%d")
        beginning = self.firstDay
        nDays = countDays(beginning, currentDate)
        toWrite = str(nDays) + " " + str(value) + "\n"
        i = bisect(self.dates, nDays)
        self.dates.insert(i, nDays)
        self.values.insert(i, value)
        with open(self.address, "a") as f:
            f.write(toWrite)
            
    def add_otherDay(self, date, value):
        beginning = self.firstDay
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
        self.firstDay = date
        