class Multiply:
    
    def mul(self,a,b=None,c=None,d=None):
        s=0
        if  b!=None and c!=None and d!=None:
            s = a*b*c*d
        elif b!=None and c!=None:
            s= a*b*c
        elif b!=None:
            s= a*b
        else:
            s=a
        
        return s
    
m1=Multiply()
print(m1.mul(5,6,7,2))
            
            
        
        