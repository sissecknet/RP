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


#generate a test character, function could be removed later on but great for quickly getting a character to test out features
# character name, health, class and level are predefined and all stats are 8
def gentest():
    statblock = {}
    for i in statName:
        statblock[i] = 8
    return Char('Bimp', 50, statblock, 'Warlock', 8)

#Function for generating a character instead of having to type it in as a list of data
def genchar():
    
    statblock = {}
    print('Let us create a character')
    print()
    cName = input('What is the nick of the character? ')
    print()
    cClass = input('And what might your class be? ')
    print()
    cLevel = int(input('What level are you? '))
    print()
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
    

def loadchar():
    filename = askopenfilename(
        initialdir = path,
        title = 'Select your character',
        filetypes = fTypes)    
    with open(filename, 'rb') as file:
        loaded_data = pickle.load(file)
    return loaded_data
    
test = gentest()
test.inventory.addinv('Scroll of magic stuff', 1)
test.inventory.addinv('Scroll of magic stuff', 1)
test.inventory.printinv()

#test.help()
#bimp = loadchar('bimp')
