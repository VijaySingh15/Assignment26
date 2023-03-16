class Account:
    def __init__(self,userId,balance):
        self.userId=userId
        self.balance=balance
    
    def __add__(self,other):
        userId=self.userId + other.userId
        balance=self.balance + other.balance
        user3=Account(userId,balance)
        
        return user3
    
    
    
user1=Account(101,10000)
user2=Account(102,100000)
user3=user1+user2
print(user3.userId)
print(user3.balance)