from logging.config import valid_ident


class Money:
    def __init__(self,val):
        self.val = val
        
    def __eq__(self, other):
        if isinstance(other, Money):
            return self.val == other.val
        return  self.val == other
    
    def __ne__(self, other):
        if isinstance(other, Money):
            return self.val != other.val
        return  self.val != other

m = Money(10)
print( m == 10)
print( m != 11)
    
class PairValue:
    
    def __init__(self, first_val, second_val):
        self.first_val = first_val
        self.second_val = second_val
        
    def __add__(self):
        return self.first_val + self.second_val
    
    def __sub__(self):
        return self.first_val - self.second_val
    
p = PairValue(12,13)
print(p.__add__())
print(p.__sub__())    

       
        