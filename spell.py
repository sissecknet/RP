# Account class


#statName = ['Str','Dex','Con','Int','Wis','Cha']

class Spell():
    def __init__(self, Class):
        self.slotsmax = {}
        self.slot = {}
        
        self.sorc = 0
        self.Class = Class
        
    
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
            
            
    def set(self):
        topslot = input('What is the highest spell slot? ')
        
        print(super().super().Name)


