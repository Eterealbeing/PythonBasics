class Mpesa:
    def __init__(self, account_balance, phone_number):
        self.account_balance = account_balance
        self.phone_number = phone_number

    def send_money(self, amount, recipient):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"Ksh.{amount} has been sent to {recipient}.")
        else:
            print(f"Insufficient funds.")


class PersonalMpesa(Mpesa):
    def __init__(self, account_balance, phone_number, id_number):
        super().__init__(account_balance, phone_number)
        self.id_number = id_number

    def buy_airtime(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
        print(f"You have purchased Ksh.{amount} Airtime.")


class BusinessMpesa(Mpesa):
    def __init__(self, account_balance, phone_number, business_name):
        super().__init__(account_balance, phone_number)
        self.BusinessName = business_name

    def receive_money(self, amount):
        self.account_balance += amount
        print(f"You have received Ksh.{amount} successfully.")


personal = PersonalMpesa(500, '+254714942048', 42775478)
personal.send_money(400, '+254704397948')
personal.buy_airtime(100)

business = BusinessMpesa(500000, '+254714942048', 'kazi')
business.receive_money(100000)
