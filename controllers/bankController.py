# controllers/bank_controller.py
from models.bankAcc import BankAccount
from models.premiumAcc import PremiumAccount

class BankController:
    def __init__(self):
        self.register = []

  #tambah akun
    def addAccount(self, acc_type: str, account_number: str, name: str, saldo: float):
        if acc_type.strip().lower() == "premium":
            acc = PremiumAccount(account_number, name, saldo)
        else:
            acc = BankAccount(account_number, name, saldo)
        self.register.append(acc)
        print(f"✅ Akun '{name}' ({account_number}) berhasil dibuat sebagai '{acc_type}'.")

  #tampilan semua akun
    def showAllAccounts(self):
        if not self.register:
            print("📭 Belum ada akun terdaftar.")
            return
        print("\n📋 Daftar Akun:")
        for acc in self.register:
            print(" -", acc.info())
            
  #cari akun
    def cariAccount(self, account_number: str):
        for acc in self.register:
            if acc.account_number == account_number:
                return acc
        return None

  #cari akun lalu deposit uang
    def deposit(self, account_number: str, jumlah: float):
        acc = self.cariAccount(account_number)
        if acc:
            acc.deposit(jumlah)
        else:
            print("❌ Akun tidak ditemukan.")
  
  #cari akun lalu tarik uang
    def withdraw(self, account_number: str, jumlah: float):
        acc = self.cariAccount(account_number)
        if acc:
            acc.withdraw(jumlah)
        else:
            print("❌ Akun tidak ditemukan.")
