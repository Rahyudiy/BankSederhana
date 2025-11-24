# controllers/bank_controller.py
from models.bankAcc import BankAccount
from models.premiumAcc import PremiumAccount
from rich.console import Console
from rich.table import Table
from databases.db_connection import get_con

class BankController:

    def __init__(self):
        pass

  #tambah akun
    def addAccount(self, acc_type: str, account_number: str, name: str, saldo: float):
        if acc_type.strip().lower() == "premium":
            acc = PremiumAccount(account_number, name, saldo)
        else:
            acc = BankAccount(account_number, name, saldo, acc_type="regular")
     
        console = Console()
        acc.saveToDB()
        console.print(f"[green italic]✅ Akun '{name}' ({account_number}) berhasil dibuat sebagai '{acc_type}'.")

  #tampilan semua akun
    def showAllAccounts(self):
       console = Console()
       conn = get_con()
       sql = conn.cursor()
       sql.execute("SELECT account_number, name, balance, acc_type FROM accounts")
       rows = sql.fetchall()
       conn.close()

       table = Table(title="[bold green]📊 Semua Akun", expand=True)
       table.add_column("Account No", justify="center", style="cyan")
       table.add_column("Name", justify="center", style="green")
       table.add_column("Type", justify="center", style="magenta")
       table.add_column("Balance", justify="center", style="yellow")
       
       if not rows:
           console.print("[yellow italic]📭 Tidak ada akun di database.")
           return
       for account_number, name, balance, acc_type in rows:
           table.add_row(account_number, name, acc_type, f"Rp{int(balance)}")
       console.print(table)
            
    def cariAccount(self, account_number: str):
        conn = get_con()
        curs = conn.cursor()

        curs.execute("""
            SELECT account_number, name, balance, acc_type
            FROM accounts
            WHERE account_number = ?
        """, (account_number,))

        row = curs.fetchone()
        conn.close()

        # Jika tidak ada di database
        if row is None:
            return None

        acc_number, name, balance, acc_type = row

        # Buat objek sesuai jenis akun
        if acc_type == "premium":
            return PremiumAccount(acc_number, name, balance)
        else:
            return BankAccount(acc_number, name, balance, acc_type="regular")


  #cari akun lalu deposit uang
    def deposit(self, account_number: str, jumlah: float):
        console = Console()
        acc = self.cariAccount(account_number)
        if acc:
            acc.deposit(jumlah)
        else:
            console.print("[red italic]❌ Akun tidak ditemukan.")
  
  #cari akun lalu tarik uang
    def withdraw(self, account_number: str, jumlah: float):
        console = Console()
        acc = self.cariAccount(account_number)
        if acc:
            acc.withdraw(jumlah)
        else:
            console.print("[red italic]❌ Akun tidak ditemukan.")

    # hapus akun
    def deleteAccount(self, account_number: str):
        console = Console()
        conn = get_con()
        curs = conn.cursor()

        # Cek apakah akun ada di database
        curs.execute("SELECT * FROM accounts WHERE account_number = ?", (account_number,))
        row = curs.fetchone()

        if row is None:
            console.print("[red italic]❌ Akun tidak ditemukan.")
            conn.close()
            return

        # Hapus akun
        curs.execute("DELETE FROM accounts WHERE account_number = ?", (account_number,))
        conn.commit()
        conn.close()

        console.print(f"[green italic]✅ Akun dengan nomor '{account_number}' telah berhasil dihapus.")
