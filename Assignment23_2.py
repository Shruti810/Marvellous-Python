class BankAccount:
    ROI = 10.5

    def __init__(self,Name,InitialAmount):
        self.Name = Name
        self.InitialAmount = InitialAmount

    def Display(self):
        print("Account holder name is",self.Name,"and current balance is",self.InitialAmount)

    def Deposit(self,Amount):
        self.InitialAmount = self.InitialAmount + Amount
        Amount = print("Amount deposited:", Amount)

    def Withdraw(self,WithdrawAmount):
        if WithdrawAmount <= self.InitialAmount:
            self.InitialAmount = self.InitialAmount - WithdrawAmount
            print("Amount withdrawn:", WithdrawAmount)
        else:
            print("Insufficient Balance")

    def CalculateInterest(self):
        Interest = (self.InitialAmount * BankAccount.ROI) / 100
        print("Interest is:",Interest)

obj1 = BankAccount("Shruti",5000)
obj1.Display()
obj1.Deposit(2000)
obj1.Withdraw(6000)
obj1.CalculateInterest()


