# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 17:30:39 2017

@author: Pradeep
"""

def ask():
    while True:    
        try: 
            val = int(input("Please enter an integer: "))
        except:
            print ("Look like non-int, Try again")
            continue
        else:
            break
        
    print ('Square is:',val**2)
    
ask()