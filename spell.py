

class Inv():
    def __init__(self, bagname):
        self.bagname = bagname
        self.inv = {}
    
        
    def addinv(self, i_type, i_num):
        if i_type in self.inv:
            self.inv[i_type] += i_num
    
        else:
            self.inv[i_type] = i_num
            
    def reminv(self, i_type, i_num):
        if i_type in self.inv:
            self.inv[i_type] -= i_num
            if self.inv[i_type] == 0:
                print('That was your last ' + i_type)
                self.inv.pop(i_type)
            
        else:
            print('You do not carry any ' +i_type)
            
            
    def printinv(self):
        leftWidth = 10
        rightWidth = 15
        print(self.bagname.center(leftWidth + rightWidth, '-'))
        for k, v in self.inv():
            print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
    


