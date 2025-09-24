class BankAccount:
    def __init__(self, account_holder, balance, pin):
        self.__account_holder = account_holder
        self.__balance = balance
        self.__pin = pin

    def check_balance(self, ip_pin):
        if self.__pin == ip_pin:
            print(f"Dear {self.__account_holder}, your current balance is Rs. {self.__balance}.")
        else:
            print("Sorry! invalid pin you can not check the balance")



ba1 = BankAccount("Nimra", 1000, 1234)
ba1.check_balance(2233)
ba1.check_balance(1234)


    