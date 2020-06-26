#!/usr/bin/env python
# coding: utf-8

# In[9]:


import math
import random
import sys

from tkinter import *
from tkinter import ttk
class Gamerule:
    def __init__(self, win_cond, hint, result, plr_inp):
        self.win_cond = 0
        self.hint = []
        self.rand_set = result
        self.plr_inp = plr_inp

class Fair(Gamerule):
    def __init__(self,win_cond,hint,rand_set,plr_inp):
        super().__init__(win_cond,hint,rand_set,plr_inp)
    
    def input_check(self):
        win_cond = 0
        self.hint.clear()
        for i in range(4):
            if (self.rand_set[i] == self.plr_inp[i]):
                self.hint.append(2)
                self.win_cond += 1
        if(self.win_cond >= 4):
            window.destroy()
            sys.exit("Gratulacje, wygrales")
            

        for i in range(4):
            for j in range(4):
                if(self.rand_set[i] == self.plr_inp[j] and i != j):
                    self.hint.append(1)
                    break;
    def print_out(self):
        print(self.hint)
        #label = Label(window, text = self.hint)
        pass
    
class Fake(Gamerule):
    def __init__(self,win_cond,hint,rand_set,plr_inp):
        super().__init__(win_cond,hint,rand_set,plr_inp)
    
    def input_check(self):
        self.hint.clear()
        for i in range(random.randint(0,3)):
            self.hint.append(random.randint(1,2))
 
    def print_out(self):
        print(self.hint)
        pass
    
def randomise(result):
    for i in range(4):
        result.append(random.randint(1,6))
    #print (result)
    return result

def inputdata(plr_inp):
    for i in range (4):
        while True:
            try:
                plr_inp.insert(i,(int(input("Podaj wartosc liczby: "))))
            except ValueError:
                print("Podaj prawidlowa wartosc ")
                continue
            if plr_inp[i] > 6:
                print("Podaj wartosc mniejsza badz rowna 6 ")
                continue
            if plr_inp[i] < 0:
                print("Podaj wartosc dodatnia ")
                continue
            else:
                break
                
def rule_check(tricker):
    if(tricker == 1):
        window.destroy()
        print(result)
        sys.exit("Tere fere")
        
    
    else:
        window.destroy()
        print(result)
        sys.exit("Zlapales mnie")

        
result = []
plr_inp = []
num_moves = 0
randomise(result)
tricker = random.randint(0,1)

if tricker == 0:
   # print("Fake rules")
    game_test_core = Fake(0,0,result,plr_inp)
else:
   # print("Fair rules")
    game_test_core = Fair(0,0,result,plr_inp)
while (num_moves < 13):
    inputdata(plr_inp)
    
    #######################
    #Rysowanie okna i glowna czesc kodu
    window=Tk()
    window.title("Mastermind")
    mainframe=ttk.Frame(window)
    
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    ttk.Button(mainframe, text="Oszust",
           command=lambda: print(rule_check(tricker)) ).grid(column=1, row=0,)
    ttk.Button(mainframe, text="Sprawdzam",
               command=lambda:  window.destroy() ).grid(column=2, row=0,)
    game_test_core.input_check()
    game_test_core.print_out()
    window.mainloop()
    ##########################
    
    num_moves += 1
    print("wykonana liczba ruchow to ",num_moves)
if (num_moves >= 13):
    print("koniec gry, za duzo ruchow")


# In[ ]:



