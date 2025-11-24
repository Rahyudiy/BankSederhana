from rich.table import Table
from rich.console import Console
from databases.db_connection import init_db
from databases.db_connection import get_con

class BankAccount:
    def __init__(self, account_number: str, name: str, saldoAwal: float = 0.0, acc_type: str = ""):
        self.__account_number = account_number
        self.__name = name
        self.__saldo = float(saldoAwal)
        self.__acc_type = acc_type  

    @property
    def account_number(self):
        return self.__account_number

    @property
    def name(self):
        return self.__name

    @property
    def acc_type(self):
        return self.__acc_type

    def getBalance(self) -> float:
        return self.__saldo

    def setBalance(self, value: float):
        self.__saldo = float(value)

    def saveToDB(self):
        conn = get_con()
        curs = conn.cursor()

        curs.execute("""
            INSERT OR REPLACE INTO accounts (account_number, name, balance, acc_type)
            VALUES (?, ?, ?, ?)
        """, (
            self.__account_number,
            self.__name,
            self.__saldo,
            self.__acc_type
        ))

        conn.commit()
        conn.close()

    # Deposit uang
    def deposit(self, jumlah: float):
        console = Console()
        if jumlah > 0:

            self.__saldo += jumlah
             # Update database
            conn = get_con()
            curs = conn.cursor()
            curs.execute("""
                UPDATE accounts SET balance = ? WHERE account_number = ?
            """, (self.__saldo, self.__account_number))
            conn.commit()
            conn.close()
            console.print(f"[green italic]✅ Setoran berhasil. Saldo sekarang: Rp{int(self.__saldo)}")
        else:
            console.print("[red italic]❌ Jumlah setoran harus lebih dari 0.")

    # Tarik uang
    def withdraw(self, jumlah: float):
        console = Console()
        if jumlah <= 0:
            console.print("[red italic]❌ Jumlah penarikan tidak valid.")
            return
        if jumlah <= self.__saldo:
            self.__saldo -= jumlah


            # Update database
            conn = get_con()
            curs = conn.cursor()
            curs.execute("""
                UPDATE accounts SET balance = ? WHERE account_number = ?
            """, (self.__saldo, self.__account_number))
            conn.commit()
            conn.close()

          
            console.print(f"[green italic]✅ Penarikan berhasil. Sisa saldo: Rp{int(self.__saldo)}")
        else:
            console.print("[red italic]❌ Penarikan gagal. Saldo tidak cukup.")


    # Lihat saldo
    def see_balance(self):
        print(f"💰 Saldo ({self.__account_number}) : Rp{int(self.__saldo)}")
        return self.__saldo

    # Info akun
    def info(self):
        console = Console()
        table = Table(title="[bold italic green] User Account", expand=True)

        table.add_column("No", style="green", justify='center')
        table.add_column("Name", style='green', justify='center')
        table.add_column("Type", style='green', justify='center')
        table.add_column("Saldo", style='green', justify='center')

        table.add_row(
            f'{self.__account_number}',
            f'{self.__name}',
            f'{self.__acc_type}',
            f'Rp{int(self.__saldo)}'
        )
        console.print(table)
