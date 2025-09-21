class BankAccount:
    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"{amount} so'm qo'shildi. Yangi balans: {self.balance} so'm"
        else:
            return "Qo'shiladigan summa musbat bo'lishi kerak!"

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"{amount} so'm yechildi. Yangi balans: {self.balance} so'm"
        elif amount > self.balance:
            return "Hisobda yetarli mablag' yo'q!"
        else:
            return "Yechildigan summa musbat bo'lishi kerak!"

    def check_balance(self):
        return f"Hisob egasi: {self.account_holder}\nHisob raqami: {self.account_number}\nBalans: {self.balance} so'm"


class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_holder, account_number):
        if account_number not in self.accounts:
            self.accounts[account_number] = BankAccount(account_holder, account_number)
            return f"Hisob {account_holder} uchun muvaffaqiyatli yaratildi!"
        else:
            return "Bu hisob raqami allaqachon mavjud!"

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)


def main():
    bank = BankSystem()
    
    while True:
        print("\nBank Tizimi Menyusi:")
        print("1. Hisob yaratish")
        print("2. Pul qo'shish")
        print("3. Pul yechish")
        print("4. Balansni ko'rish")
        print("5. Chiqish")
        
        choice = input("Tanlovingizni kiriting (1-5): ")
        
        if choice == "1":
            holder = input("Hisob egasining ismini kiriting: ")
            number = input("Hisob raqamini kiriting: ")
            print(bank.create_account(holder, number))
        
        elif choice == "2":
            number = input("Hisob raqamini kiriting: ")
            account = bank.get_account(number)
            if account:
                amount = float(input("Qo'shmoqchi bo'lgan summani kiriting: "))
                print(account.deposit(amount))
            else:
                print("Hisob topilmadi!")
        
        elif choice == "3":
            number = input("Hisob raqamini kiriting: ")
            account = bank.get_account(number)
            if account:
                amount = float(input("Yechmoqchi bo'lgan summani kiriting: "))
                print(account.withdraw(amount))
            else:
                print("Hisob topilmadi!")
        
        elif choice == "4":
            number = input("Hisob raqamini kiriting: ")
            account = bank.get_account(number)
            if account:
                print(account.check_balance())
            else:
                print("Hisob topilmadi!")
        
        elif choice == "5":
            print("Tizimdan chiqildi!")
            break
        
        else:
            print("Noto'g'ri tanlov! Iltimos, 1-5 oralig'ida raqam kiriting.")


if __name__ == "__main__":
    main()