import os

class Client:
    def __init__(self, client_id, name):
        self.client_id = client_id
        self.name = name
        self.accounts = {}

class BankAccount:
    def __init__(self, currency, balance=0):
        self.currency = currency
        self.balance = balance
        self.is_active = True

class Bank:
    def __init__(self):
        self.clients = {}
        self.accounts = {}

    def open_account(self, client_id, currency):
        if client_id not in self.clients:
            print("Клиент не найден")
            return

        client = self.clients[client_id]
        if currency in client.accounts:
            print("Счет в этой валюте уже есть")
            return

        account_number = f"{client_id}_{currency}"
        new_account = BankAccount(currency)

        client.accounts[currency] = new_account
        self.accounts[account_number] = new_account
        print(f"Счет {account_number} открыт")

    def close_account(self, account_number, client_id):
        if account_number not in self.accounts:
            print("Счет не найден")
            return

        account = self.accounts[account_number]

        if not account_number.startswith(client_id + "_"):
            print("Это не ваш счет")
            return

        if account.balance != 0:
            print("Нельзя закрыть счет с деньгами")
            return

        account.is_active = False
        currency = account.currency
        del self.accounts[account_number]
        del self.clients[client_id].accounts[currency]
        print("Счет закрыт")

    def deposit(self, account_number, amount):
        if account_number not in self.accounts:
            print("Счет не найден")
            return

        account = self.accounts[account_number]
        if not account.is_active:
            print("Счет закрыт")
            return

        if amount <= 0:
            print("Сумма должна быть больше 0")
            return

        account.balance += amount
        print(f"Пополнено: {amount} {account.currency}")

    def withdraw(self, account_number, amount, client_id):
        if account_number not in self.accounts:
            print("Счет не найден")
            return

        account = self.accounts[account_number]

        if not account_number.startswith(client_id + "_"):
            print("Это не ваш счет")
            return

        if not account.is_active:
            print("Счет закрыт")
            return

        if amount <= 0:
            print("Сумма должна быть больше 0")
            return

        if account.balance < amount:
            print("Недостаточно денег")
            return

        account.balance -= amount
        print(f"Снято: {amount} {account.currency}")

    def transfer(self, from_account, to_account, amount, client_id):
        self.withdraw(from_account, amount, client_id)

        if from_account in self.accounts:
            account = self.accounts[from_account]
            if account.balance >= amount:
                if to_account in self.accounts:
                    self.accounts[to_account].balance += amount
                    print(f"Перевод выполнен")
                else:
                    print("Счет получателя не найден")
                    account.balance += amount

    def print_statement(self, client_id):
        if client_id not in self.clients:
            print("Клиент не найден")
            return

        client = self.clients[client_id]
        folder = "C:/Users/pesko/OneDrive/Рабочий стол/laba piton/laba3"
        filename = os.path.join(folder, f"{client_id}_statement.txt")

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"Выписка для {client.name}:\n")
            f.write("=" * 33 + "\n")
            for currency, account in client.accounts.items():
                if account.is_active:
                    f.write(f"{currency}: {account.balance}\n")
            f.write("=" * 33 + "\n")

        print(f"Выписка сохранена в файл: {filename}")
        print("Содержимое выписки:")
        print(f"Клиент: {client.name}")
        for currency, account in client.accounts.items():
            if account.is_active:
                print(f"{currency}: {account.balance}")

bank = Bank()
bank.clients["001"] = Client("001", "Песко Егор Викторович")
bank.clients["002"] = Client("002", "Фролов Андрей Максимович")
bank.clients["003"] = Client("003", "Терещенко Владимир Батькович")
bank.clients["004"] = Client("004", "Дональд Джон Трамп")

def main():
    current_client = None

    while True:
        if current_client is None:
            print("\n=== БАНКОВСКАЯ СИСТЕМА ===")
            print("1 - Войти")
            print("2 - Выйти")

            choice = input("Выберите: ")

            if choice == "1":
                client_id = input("Введите ваш ID: ")
                if client_id in bank.clients:
                    current_client = client_id
                    print(f"Добро пожаловать, {bank.clients[client_id].name}!")
                else:
                    print("Клиент не найден")

            elif choice == "2":
                break

        else:
            print(f"\n=== МЕНЮ ({bank.clients[current_client].name}) ===")
            print("1 - Открыть счет")
            print("2 - Закрыть счет")
            print("3 - Пополнить счет")
            print("4 - Снять деньги")
            print("5 - Перевести деньги")
            print("6 - Выписка по счетам")
            print("7 - Выйти")

            choice = input("Выберите операцию: ")

            if choice == "1":
                currency = input("Введите валюту (RUB/USD/EUR/BYN): ")
                bank.open_account(current_client, currency)

            elif choice == "2":
                currency = input("Введите валюту счета: ")
                account_number = f"{current_client}_{currency}"
                bank.close_account(account_number, current_client)

            elif choice == "3":
                currency = input("Введите валюту счета: ")
                account_number = f"{current_client}_{currency}"
                amount = float(input("Сумма пополнения: "))
                bank.deposit(account_number, amount)

            elif choice == "4":
                currency = input("Введите валюту счета: ")
                account_number = f"{current_client}_{currency}"
                amount = float(input("Сумма снятия: "))
                bank.withdraw(account_number, amount, current_client)

            elif choice == "5":
                from_currency = input("Ваша валюта: ")
                to_account = input("Счет получателя (формат: ID_ВАЛЮТА): ")
                amount = float(input("Сумма перевода: "))
                from_account = f"{current_client}_{from_currency}"
                bank.transfer(from_account, to_account, amount, current_client)

            elif choice == "6":
                bank.print_statement(current_client)

            elif choice == "7":
                current_client = None
main()
