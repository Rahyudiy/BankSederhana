from rich.table import Table
from rich.console import Console

class BankAccount:


    def __init__(self, account_number: str, name: str, saldoAwal: float = 0.0):
        # Encapsulation: attribute private
        self.__account_number = account_number
        self.__name = name
        self.__saldo = float(saldoAwal)

    @property
    def account_number(self):
        return self.__account_number

    @property
    def name(self):
        return self.__name

    def getBalance(self) -> float:
        return self.__saldo

    def setBalance(self, value: float):
        self.__saldo = float(value)

  #deposit uang
    def deposit(self, jumlah: float):
        console = Console();
        if jumlah > 0:
            self.__saldo += jumlah
            console.print(f"[green italic]✅ Setoran berhasil. Saldo sekarang: Rp{int(self.__saldo)}")
        else:
            console.print("[red italic]❌ Jumlah setoran harus lebih dari 0.")

  #tarik uang
    def withdraw(self, jumlah: float):
        console = Console();
        if jumlah <= 0:
            console.print("[red italic]❌ Jumlah penarikan tidak valid.")
            return
        if jumlah <= self.__saldo:
            self.__saldo -= jumlah
            console.print(f"[green italic]✅ Penarikan berhasil. Sisa saldo: Rp{int(self.__saldo)}")
        else:
            console.print("[red italic]❌ Penarikan gagal. Saldo tidak cukup.")
  #lihat uang
    def see_balance(self):
        print(f"💰 Saldo ({self.__account_number}) : Rp{int(self.__saldo)}")
        return self.__saldo

    def info(self) -> str:

        console = Console()

        table = Table(title="[bold italic green] User Account", expand="True")

        table.add_column("No", style="green", justify='center')
        table.add_column("Name", style='green', justify='center')
        table.add_column("Saldo", style='green', justify='center')
        table.add_row(f'{self.__account_number}',f'{self.__name}', f'Rp{int(self.__saldo)}')
        console.print(table)
