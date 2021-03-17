# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 19:53:47 2021

@author: Ria Kale

The purpose of this program is to analyze the dataset 
and return computations as well as a line plot and a histogram.

I completed this assignment individually
"""
# import csv
import csv
import matplotlib.pyplot as plt

def analyzer():
    def descStats(rows):
        rows = sorted(rows)
        count = len(rows)
        mean = (sum(rows))/(count)
        diffs = []
        for i in range(count):
            diffs.append((mean-rows[i])**2)
        sd = (sum(diffs)/(count-1))**0.5
        mini = rows[0]
        p25x = .25*(count-1) + 1
        p25 = rows[int(p25x)-1] + (p25x-p25x//1)*(rows[int(p25x)]-rows[int(p25x)-1])
        p50x = .50*(count-1) + 1
        p50 = rows[int(p50x)-1] + (p50x-p50x//1)*(rows[int(p50x)]-rows[int(p50x)-1])
        p75x = .75*(count-1) + 1
        p75 = rows[int(p75x)-1] + (p75x-p75x//1)*(rows[int(p75x)]-rows[int(p75x)-1])
        maxi = rows[count-1]
        
        print(f"{'Count:':<22}{count:>8,.2f}")
        print(f"{'Mean:':<22}{mean:>8,.2f}")
        print(f"{'Standard Deviation:':<22}{sd:>8,.2f}")
        print(f"{'Minimum:':<22}{mini:>8,.2f}")
        print(f"{'25th Percentile:':<22}{p25:>8,.2f}")
        print(f"{'50th Percentile:':<22}{p50:>8,.2f}")
        print(f"{'75th Percentile:':<22}{p75:>8,.2f}")
        print(f"{'Maximum:':<22}{maxi:>8,.2f}")
    
    print("Welcome!")
    f = input("Enter the name and location of the file you want opened: ")
    if ".csv" not in f:
        print("Sorry, it looks like we don't have that file. Try again!")
    else:
        f = open(f)
        reader = csv.DictReader(f)
        close_price = []
        open_price = []
        high_price = []
        low_price = []
        change_price = []
        
        for row in reader:
            close_price.append(float(row['Price']))
            open_price.append(float(row['Open']))
            high_price.append(float(row['High']))
            low_price.append(float(row['Low']))
            change_price.append(float(row['Change %'][:-1]))
            
        print("Select which columns you would like to include: 1-Price, 2-Open, 3-High, 4-Low, 5-Change % ")
        column_select = input()
        
        #assigning the variables to values
        if '1' in column_select:
            descStats(close_price)
        if '2' in column_select:
            descStats(open_price)
        if '3' in column_select:
            descStats(high_price)
        if '4' in column_select:
            descStats(low_price)
        if '5' in column_select:
            descStats(change_price)
                
        plot_prompt = input("would you like to receive plots: Y- Yes, N- No: ") 
        
        if '1' in column_select:
             if plot_prompt.lower() == "y":
                plt.plot(close_price)
                plt.show()
        if '2' in column_select:
            if plot_prompt.lower() == "y":
                plt.plot(open_price)
                plt.show()
        if '3' in column_select:
            if plot_prompt.lower() == "y":
                plt.plot(high_price)
                plt.show()
        if '4' in column_select:
            if plot_prompt.lower() == "y":
                plt.plot(low_price)
                plt.show()
        if '5' in column_select:
             if plot_prompt.lower() == "y":
                plt.plot(change_price)
                plt.show()
                
        hist_prompt = input("click enter to receive your histogram:")
        if hist_prompt == "":
            plt.hist(change_price, bins=15)
            plt.show()
analyzer()
