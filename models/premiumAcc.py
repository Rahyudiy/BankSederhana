from models.bankAcc import BankAccount


class PremiumAccount(BankAccount):
    # Inheritance
    # mewarisi semua atribut dan method bankAccount
    # lalu menambahkan perilaku baru

    def withdraw(self, jumlah: float):
        if jumlah <= 0:
            print("❌ Jumlah penarikan tidak valid.")
            return
        
        # Polymorphism akun premium bisa tarik saldo dengan tambahan limit sampai 50.000
        uang = self.getBalance()
        limitTambahan = 50000.0
        if jumlah <= uang + limitTambahan:
            self.setBalance(uang - jumlah)
            print(f"💎 Penarikan premium berhasil. Sisa saldo: Rp{int(self.getBalance())}")
        else:
            print("❌ Penarikan gagal. Limit tambahan premium terlampaui.")
