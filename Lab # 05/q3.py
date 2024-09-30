class Account:
    def __init__(self, account_no, account_bal, security_code):
        self.__account_no = account_no
        self.__account_bal = account_bal
        self.__security_code = security_code

    def show_data(self):
        self.account_bal = 3904
        self.account_no = 89003
        self.security_code = 990088483

        print(
            f"the Account Number is :{self.account_no}\nAccount Balance is : {self.account_bal}\nSecurity Code is : {self.security_code}")


myacc = Account(0, 0, 0)
myacc.show_data()
