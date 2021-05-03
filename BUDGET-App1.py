class Budget():
    pass
    def depositFunds(self):
        deposit = int(input("How much would you like to deposit? \n"))
        print('You have successfully deposited #{}'.format(deposit),'into this category')
    def balance(self):
        balance = int(input('''Your balance in this category is #0.00. Would you like to make a deposit now?
        (1) Yes
        (2) No
        '''))
        if balance == 1:
            currentDeposit = int(input('How much would you like to deposit in this category?'))
            print('You have successfully deposited #{}'.format(currentDeposit),'into this category') 
        elif balance == 2:
            budgetOperations()
    def withdrawFunds(self):
        Withdrawal = int(input("How much would you like to withdraw? \n"))
        print('You have successfully withdrawn #{}'.format(Withdrawal),'from this category')
    def transfer(self):
        transferAmount = int(input("How much would you like to transer? \n"))
        
        transferPoint = int(input('''Which category would you like to transfer from? 
        (1) Food 
        (2) Clothing 
        (3) Equipment \n'''))
        if transferPoint == 1:
            transferDestination = int(input('''Which category would you like to transfer to? 
            (1) Clothing 
            (2) Equipment \n'''))
            if transferDestination == 1:
                print('You have successfully transferred #{}'.format(transferAmount),'to category "Clothing"')
            elif transferDestination == 2:
                print('You have successfully transferred #{}'.format(transferAmount),'to category "Equipment"')
            elif transferDestination > 2:
                print('Invalid Option Selected. Please Try Again')
                Budget(self.transfer())
            else:
                print('Invalid Option Selected. Please Try Again')
                Budget(self.transfer())

        
        if transferPoint == 2:
            transferDestination = int(input('''Which category would you like to transfer to? 
            (1) Food 
            (2) Equipment \n'''))
            if transferDestination == 1:
                print('You have successfully transferred #{}'.format(transferAmount),'to category "Food"')
            elif transferDestination == 2:
                print('You have successfully transferred #{}'.format(transferAmount),'to category "Equipment"')
            elif transferDestination > 2:
                print('Invalid Option Selected. Please Try Again')
                Budget(self.transfer())
            else:
                print('Invalid Option Selected. Please Try Again')
                Budget(self.transfer())
                
        if transferPoint == 3:
            transferDestination = int(input('''Which category would you like to transfer to? 
            (1) Food 
            (2) Clothing \n'''))
            if transferDestination == 1:
                print('You have successfully transferred #{}'.format(transferAmount),'to category "Food"')
            elif transferDestination == 2:
                print('You have successfully transferred #{}'.format(transferAmount),'to category "Clothing"')
            elif transferDestination > 2:
                print('Invalid Option Selected. Please Try Again')
                Budget(self.transfer())
            else:
                print('Invalid Option Selected. Please Try Again')
                Budget(self.transfer())

food = Budget()
clothing = Budget()
equipment = Budget()

def budgetOperations():
    categoryOption = int(input('''Welcome to your budget layout.
    Please select a category:
    (1) Food 
    (2) Clothing 
    (3) Equipment
    '''))
    if categoryOption == 1:
        operationOption = int(input('''You have chosen category "Food." What would you like to do?
        (1) Deposit funds
        (2) Withdraw funds
        (3) Compute Balance
        (4) Transfer available balance to another category
        '''))
        if categoryOption == 1:
            food.depositFunds()
        elif categoryOption == 2:
            food.withdrawFunds()
        elif categoryOption == 3:
            food.balance()
        elif categoryOption == 4:
            food.transfer()
        else:
            print("Invalid Option selected")
    elif categoryOption == 2:
        operationOption = int(input('''You have chosen category "Clothing." What would you like to do?
        (1) Deposit funds
        (2) Withdraw funds
        (3) Compute Balance
        (4) Transfer available balance to another category
        '''))
        if operationOption == 1:
            clothing.depositFunds()
        elif operationOption == 2:
            clothing.withdrawFunds()
        elif operationOption == 3:
            clothing.balance()
        elif operationOption == 4:
            clothing.transfer()
        else:
            print("Invalid Option Selected")

    elif categoryOption == 3:
        operationOption = int(input('''You have chosen category "Equipment." What would you like to do?
        (1) Deposit funds
        (2) Withdraw funds
        (3) Compute Balance
        (4) Transfer available balance to another category
        '''))
        if operationOption == 1:
            clothing.depositFunds()
        elif operationOption == 2:
            clothing.withdrawFunds()
        elif operationOption == 3:
            clothing.balance()
        elif operationOption == 4:
            clothing.transfer()
        else:
            print("Invalid Option Selected")

budgetOperations()