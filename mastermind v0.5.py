#!/usr/bin/env python
# coding: utf-8

# In[16]:


result = []
plr_inp = []
num_moves = 0
#win_cond = 0
import math
import random

class Regulygry:
    def __init__(self, win_cond):
        self.win_cond = cond
    def result(self):
        for i in range(4):
            if (result[i] == plr_inp[i]):
                win_cond += 1
            for j in range(4):

class Prawidlowe(Regulygry):
    pass
    
class Oszukancze(Regulygry):
    pass
    
def randomise(result):
    for i in range(4):
        result.append(random.randint(1,6))
    print (result)
    return result

def inputdata():
    for i in range (4):
        while True:
            try:
                plr_inp.insert(i,(int(input("Podaj wartosc liczby: "))))
            except ValueError:
                print("Podaj prawidlowa wartosc ")
                continue
            else:
                break
##
##def check(win_cond = 1):
##    for i in range(4):
##        if (result[i] == plr_inp[i]):
##            win_cond += 1
##    return(win_cond)

randomise(result)
while (num_moves < 12):
    inputdata()
    if(check(win_cond) == 4):
        print("wygrles!")
        break
 #   print(result[0],plr_inp[0])
 #   print(result[1],plr_inp[1])
 #   print(result[2],plr_inp[2])
 #   print(result[3],plr_inp[3])
    num_moves += 1
    print(num_moves)
if (num_moves >= 12):
    print("koniec gry, za duzo ruchow")


# In[2]:


a = int(3)
b = str(3)
print(a)
print (b)
print(abs(b - a))
if(b == a):
    print("YOOOOOO")

