

class Inv():
    def __init__(self):
        
        self.inv = {}
    
    def help(self):
        
        leftWidth =15
        rightWidth = 10
        
        dFuncs = {}
        dFuncs['add(kwars)'] = 'add items to inventory add(sword=1)'
        dFuncs['rem(kwars)'] = 'remove items from inventory rem(sword=1)'
        dFuncs['show'] = 'show inventory'
        
        print('functions in inventory'.center(leftWidth + rightWidth, '-'))
        for i in dFuncs:
            lw = leftWidth - len(i)
            print(i.ljust(lw, '.') + dFuncs[i].rjust(rightWidth))    
    
    
    def add(self, *args):
        
        if not bool(args):
            i_type = input('What item did you find? ').title()
            i_num = int(input('How many did you find? '))
            itemAdd = {i_type:i_num}
            #Check if the item already exists in the bag, if so just add new number
        else:
            itemAdd = dict(args[0])
            itemAdd = {k.title():v for k,v in itemAdd.items()}
        
        
        for i_type in itemAdd:
            
            i_cap = i_type.title()
            if i_cap in self.inv:
                self.inv[i_cap] += itemAdd[i_type]
            else:
                self.inv[i_cap] = itemAdd[i_type]
            
    def rem(self, *args):
        if not bool(args):
            self.show()
            i_type = input('What item would you like to remove? ').title()
            i_num = int(input('How many of the item to remove? '))
            itemRem = {i_type:i_num}
        else:
            itemRem = dict(args[0])
            itemRem = {k.title():v for k,v in itemRem.items()}
        
        
        for i_type in itemRem:
            
            i_cap = i_type.title()
            if i_cap in self.inv:
                if self.inv[i_cap] < itemRem[i_type]:
                    print('Trying to use more than you have')
                
                else:
                    self.inv[i_cap] -= itemRem[i_type]
                    print('You used ', i_cap)
                    if self.inv[i_cap] == 0:
                        #always nicec to know when you use your last of something
                        print('That was your last ' + i_cap)
                        self.inv.pop(i_cap)
            
            else:
                print('You do not carry any ' +i_cap)
            
            
    def show(self):
        leftWidth = 10
        rightWidth = 15
        print('Your items are'.center(leftWidth + rightWidth, '-'))
        
        
        for k in self.inv.keys():
            print(self.inv[k], ' ', k)
            
    


