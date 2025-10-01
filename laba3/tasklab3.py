class Client:
    
    def __init__(self, client_id, name, surname, passport_number):
        self.client_id = client_id
        self.name = name
        self.surname = surname
        self.passport_number = passport_number
        self.accounts = {} 
    
    def __str__(self):
        return f"Клиент {self.client_id}: {self.name} {self.surname}"


class BankAccount:

    def __init__(self, account_number, client, currency="RUB", balance=0.0):
        self.account_number = account_number
        self.client = client
        self.currency = currency
        self.balance = balance
        self.is_active = True
    
    def __str__(self):
        status = "активен" if self.is_active else "закрыт"
        return f"Счет {self.account_number}: {self.balance} {self.currency} ({status})"


class Bank:
    
    def __init__(self, name):
        self.name = name
        self.clients = {} 
        self.accounts = {}  