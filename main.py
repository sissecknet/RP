from char import *
import os
import pickle
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

#by defining file types, only relevant files are shown in the dialogs for loading and saving characters
fTypes = (('character files ', '*.dnd'), ('character files ', '*.DND'))

path = os.getcwd()
filename=path +'\\shelve.out'

#Defining the types and order of stats now ensures it is always the same

statName = ['Str','Dex','Con','Int','Wis','Cha']


#Help function
def help():
        #trying to make a help function, but adjusting left rightWidth
        #is not working like i want
        
        
        #code block to generate help text
        hTitle = 'Help info for DnD py'
        
        dFuncs = {}
        sFuncs = {}
        dFuncs['var = gentest()'] = 'generate a test character'
        dFuncs['var = genchar()'] = 'Generate new character'
        dFuncs['savechar(Var)'] = 'Save character to file'
        dFuncs['var = loadchar()'] = 'Load character into var'
        
        sFuncs['.name'] = 'Name of character'
        sFuncs['.HP'] = 'Health'
        sFuncs['.HPmax'] = 'Max health'
        sFuncs['.Str'] = 'Strength stat, works for other stats also'
        sFuncs['.Class'] = 'Class of character'
        sFuncs['.Level'] = 'Level of character'
        
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
        
        print(hTitle.center(leftWidth + rightWidth, '-'))
        for i in dFuncs:
            lw = leftWidth
            print(i.ljust(lw, '-'), dFuncs[i].rjust(rightWidth,'-'))    
        print()
        for i in sFuncs:
            lw = leftWidth
            print(i.ljust(lw, '-'), sFuncs[i].rjust(rightWidth,'-'))    
      


#generate a test character, function could be removed later on but great for quickly getting a character to test out features
# character name, health, class and level are predefined and all stats are 8
def gentest():
    statblock = {}
    for c, i in enumerate(statName):
        statblock[i] = 8 + c
    res = Char('Bimp', 50, statblock, {'Warlock':8})
    res.inv.add(Sword=1, Dagger=1, Health_potion=2)
    return res

#Function for generating a character instead of having to type it in as a list of data
def genchar():
    
    combClass = {}
    statblock = {}
    print('Let us create a character')
    print()
    cName = input('What is the nick of the character? ')
    print()
    while True:
        
        cClass = input('What class would you like to add? ') or 0
        if cClass == 0:
            break
        print()
        cLevel = int(input('What level is this class? '))
        print()
        combClass[cClass] = int(cLevel)
    
    
    for i in statName:
        statblock[i] = int(input('What is your '+ i+ ' score? '))
    print()
    HP = int(input('What is your HP? '))
    return Char(cName, HP, statblock, cClass, cLevel)
    
    

#function with GUI to save character, requires input in function of what the character variable is
def savechar(charVar):
    filename = asksaveasfilename(
        initialdir = path,
        title = 'Save character',
        filetypes = fTypes) 
        
    #use lowercase to avoid trouble with mismatch in case of file type
    filename.lower()
    if not filename.endswith('dnd'):
        filename = filename + '.dnd'
    
    with open(filename, 'wb') as pickle_file:
        pickle.dump(charVar, pickle_file)
    
#Function to load character
def loadchar():
    filename = askopenfilename(
        initialdir = path,
        title = 'Select your character',
        filetypes = fTypes)    
    with open(filename, 'rb') as file:
        loaded_data = pickle.load(file)
    return loaded_data
    
test = gentest()
test.show()



#test.help()
#bimp = loadchar('bimp')
