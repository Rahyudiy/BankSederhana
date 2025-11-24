from models.bankAcc import BankAccount
from rich.console import Console

class PremiumAccount(BankAccount):
    # Inheritance 
    # mewarisi semua atribut dan method bankAccount 
    # lalu menambahkan perilaku baru
    
    def __init__(self, account_number: str, name: str, saldoAwal: float = 0.0):
        super().__init__(account_number, name, saldoAwal, acc_type="Premium")

    def withdraw(self, jumlah: float):
        console = Console()
        if jumlah <= 0:
            console.print("[red italic]❌ Jumlah penarikan tidak valid.")
            return
        
        uang = self.getBalance()
        limitTambahan = 50000.0

        if jumlah <= uang + limitTambahan:
            self.setBalance(uang - jumlah)
            console.print(f"[bold cyan]💎 Penarikan premium berhasil![/] Sisa saldo: Rp{int(self.getBalance())}")
        else:
            console.print("[red italic]❌ Penarikan gagal. Limit tambahan premium terlampaui.")
