

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
        
        print('functions in money'.center(leftWidth + rightWidth, '-'))
        for i in dFuncs:
            lw = leftWidth - len(i)
            print(i.ljust(lw, '.') + dFuncs[i].rjust(rightWidth))    
    
    
    def add(self, **kwargs):
        
        if not bool(kwargs):
            i_type = input('What item did you find? ').capitalize()
            i_num = int(input('How many did you find? '))
            kwargs = {i_type:i_num}
            #Check if the item already exists in the bag, if so just add new number
            
        for i_type in kwargs:
            i_cap = i_type.capitalize()
            if i_cap in self.inv:
                self.inv[i_cap] += kwargs[i_type]
            else:
                self.inv[i_cap] = kwargs[i_type]
            
    def rem(self, **kwargs):
        if not bool(kwargs):
            self.show()
            i_type = input('What item would you like to remove? ').capitalize()
            i_num = int(input('How many of the item to remove? '))
            kwargs = {i_type:i_num}
        
        for i_type in kwargs:
            i_cap = i_type.capitalize()
            if i_cap in self.inv:
                if self.inv[i_cap] < kwargs[i_type]:
                    print('Trying to use more than you have')
                
                else:
                    self.inv[i_cap] -= kwargs[i_type]
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
            
    


