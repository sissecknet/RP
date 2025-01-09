# Account class
from inventory import *
from money import *
from spell import *

statName = ['Str','Dex','Con','Int','Wis','Cha']

#This class takes a predefined set of data or use the call from main.py
#to create a new character. Level of character is summed from Class vars


class Char():
    def __init__(self, name, HP, stat, Class):
        
        self.inv = Inv()
        self.name = name
        self.HP = int(HP)
        self.HPmax = int(HP)
        self.Str = int(stat['Str'])
        self.Dex = int(stat['Dex'])
        self.Con = int(stat['Con'])
        self.Int = int(stat['Int'])
        self.Wis = int(stat['Wis'])
        self.Cha = int(stat['Cha'])
        self.Class = Class
        lev = 0
        for k in Class:
            lev += int(Class[k])
        
        self.Level = lev
        #update to calculate total leel
        self.money = Money(0)
        #self.spell = Spell(Class)
    
    def help(self):
        #trying to make a help function, but adjusting left rightWidth
        #is not working like i want
        
        
        #code block to generate help text
        dFuncs = {}
        sFuncs = {}
        dFuncs['takeDamage(amount)'] = 'Character takes damage'
        dFuncs['healDamage(amount)'] = 'Character is healed'
        dFuncs['abilityMod(stat)'] = 'Get ability mod for given stat'
        dFuncs['show()'] = 'Show character info'
        
        sFuncs['.inv'] = 'Inventory submenu'
        sFuncs['.money'] = 'Money submenu'
        
        #try and generate adaptive lw rw based on text
        lw = []
        rw = []
        for i in dFuncs:
            lw.append(len(i))
            rw.append(len(dFuncs[i]))
        
        for i in sFuncs:
            lw.append(len(i))
            rw.append(len(sFuncs[i]))
            
        leftWidth = max(lw)+5
        rightWidth = max(rw)

        
        
        print('functions in character'.center(leftWidth + rightWidth, '-'))
        for i in dFuncs:
            lw = leftWidth
            print(i.ljust(lw, '-'), dFuncs[i].rjust(rightWidth,'-'))    
        print()
        for i in sFuncs:
            lw = leftWidth
            print(i.ljust(lw, '-'), sFuncs[i].rjust(rightWidth,'-'))    
            
    
#function to remove hp when taking damage, or dead if needed    
#Also warns when player goes down
    def takeDamage(self, amountDamage):
        
        if amountDamage < 0:
            print('You cannot take negative damage')
            return None

        self.HP -= amountDamage
        
        if self.HP <= 0:
            self.HP = 0
            print('You go down!')
        return self.HP
#Healing function, checks so healing is not done negative
#warns of overhealing        
    def healDamage(self, amountHeal):
        if amountHeal < 0:
            print('You cannot heal a negative amount')
            return None

        self.HP += amountHeal
        
        
        if self.HP > self.HPmax:
            print('!!Overheal!! ', self.HP - self.HPmax, ' !!Overheal!!')
            self.HP = self.HPmax
            
        return self.HP
    
#function to return ability modifier according to dnd standard rules    
    def abilityMod(self, stat):
    
        
        stat = stat.capitalize() #Capital to match data
        
        stat = stat[:3] #only use first 3 letters
        s_range=[9,11,13,15,17,19,21] #values for DnD table
        mod = -1 #standard return value on errors
        
        
        
        if stat in statName: #check if correct stat
            x = getattr(self, stat) #get ability value    
            if ((x < 8) or (x > 20)): #code only valid from scores of 8 to 20
                print('score out of range, mod set to -1')
        
            else:
                for i in s_range: #run through dnd table
                    if x > i: #if char stat is higher
                        mod += 1 #add 1 to mod score
                    else: #otherwise break
                        break
    
        else: #catch if user inputs non-standard stat value, returns -1
            print('Ability not recognized')
            print('score set to -1')
            
                
        return mod

  
#Function outputting relevant info about character        
    def show(self):
        print('Name:', self.name)
        print('Classes:', self.Class)
        print('HP:', self.HP)
        print('     stat    mod')
        for i in statName:
            amod = self.abilityMod(i)
            print(i, '= ',getattr(self, i),'    ',amod)
            
        
        print()


