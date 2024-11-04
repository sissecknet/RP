

class Inv():
    def __init__(self):
        
        self.inv = {}
    
        
    def addinv(self, i_type, i_num):
        #Check if the item already exists in the bag, if so just add new number
        if i_type in self.inv:
            self.inv[i_type] += i_num
        #if not, add the type and num of item
        else:
            self.inv[i_type] = i_num
            
    def reminv(self, i_type, i_num):
        if i_type in self.inv:
            self.inv[i_type] -= i_num
            if self.inv[i_type] == 0:
                #always nicec to know when you use your last of something
                print('That was your last ' + i_type)
                self.inv.pop(i_type)
            
        else:
            print('You do not carry any ' +i_type)
            
            
    def printinv(self):
        leftWidth = 10
        rightWidth = 15
        print('Your items are'.center(leftWidth + rightWidth, '-'))
        
        
        for k in self.inv.keys():
            print(self.inv[k], ' ', k)
            
    


