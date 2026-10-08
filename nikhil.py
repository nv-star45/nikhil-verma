class account:
    def __init__(self,acc,bal):
        self.account_no=acc
        self.balance=bal

    def debit(self,amount):
        self.balance-=amount
        print("Rs",amount,"was debited")
        print("total balance=",self.get_balance())

    def credit(self,amount):
        self.balance+=amount
        print("Rs",amount,"was credited")
        print("total amount=",self.get_balance())
        

    def get_balance(self):
        return self.balance

acc1=account(10000,12345)
acc1.credit(10000)
acc1.debit(500)
acc1.credit(4000000)