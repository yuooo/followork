# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 21:31:11 2016

@author: jessicahoffmann
"""
import os
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
        with open(self.address, "a") as f:
            f.write(toWrite)
            
    def add_otherDay(self, date, value):
        beginning = self.firstday
        nDays = countDays(beginning, date)
        toWrite = str(nDays) + " " + str(value) + "\n"
        with open(self.address, "a") as f:
            f.write(toWrite)
            
    def statistics(self):
        print "average, working days:", sum(self.values)/(len(self.values) - 0.)
        print "average, overall:", sum(self.values)/(max(self.dates) - 0.)
        print "average, last 10 days:", "TODO"
        print self.values
            
    def plot(self):
        plt.bar(self.dates, self.values, color="red", linestyle="-")
        
            
goal1 = Goal("test")
goal1.statistics()
goal1.plot()
#goal1.delete()

        
        
        
        
    