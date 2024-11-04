coinTypes = ['copper', 'silver', 'gold', 'platinum']



class Money():
    def __init__(self, amount):
        self.amount = amount
    
        
    
    
    def help(self):
        
        leftWidth =15
        rightWidth = 10
        
        dFuncs = {}
        dFuncs['add'] = 'add money to character'
        dFuncs['rem'] = 'remove money from character'
        dFuncs['show'] = 'show money, round largest denomimation'
        
        print('functions in money'.center(leftWidth + rightWidth, '-'))
        for i in dFuncs:
            lw = leftWidth - len(i)
            print(i.ljust(lw, '.') + dFuncs[i].rjust(rightWidth))

        
        

    def add(self):
        
        income = 0 #working var
        #take user input for different coins
        for count, i in enumerate(coinTypes):
            
            inAmount = int(input('Amount of ' + i + ' ') or 0)
            while inAmount < 0:
                print('Negative values not allowed, set to zero')
                inAmount = int(input('Amount of ' + i + ' ') or 0)
            
            income += inAmount*(10**count) #calculate working war in cp
            

        self.amount += income #update money
        


    def rem(self):
        #borderline identical to above
        income = 0
        for count, i in enumerate(coinTypes):
            
            inAmount = int(input('Amount of ' + i + ' ') or 0)
            while inAmount < 0:
                print('Negative values not allowed, set to zero')
                inAmount = int(input('Amount of ' + i + ' ') or 0)
            income += inAmount*(10**count)
        if self.amount - income < 0:
            print('Oy don\'t spend money you don\'t have')
        
        else:
            self.amount -= income 
    
    
    def show(self):
        current = self.amount #get current amount
        
        expList = list(range(0,len(coinTypes))) #list of exponents to use
        expList.reverse() #reverse to do highest coin type first
        res=[] #var for division results
        
        #calculate floor division for each coin type
        for count, i in enumerate(expList):
            res.append(current // (10**i)) #list of types of coins
            current -= res[count] * (10**i) #remove found coins
            #for instance, floor division gives 2 platinum coins
            #therefore remove 2 plat coins 2 * (10**3) copper from current
            
        res.reverse() #reverse list so copper comes first    
        
        #print out coins
        for count, i in enumerate(res):
            print('You have ', i, ' ', coinTypes[count])
        
    


