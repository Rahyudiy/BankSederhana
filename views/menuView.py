#tampilan menu
from rich import print
from rich.console import Console
from rich.table import Table

class MenuView:
    @staticmethod
    def lihatMenu():


        console = Console()

        table = Table(title="[bold italic green]Bank Menu", expand=True)

        table.add_column("No", style="green", justify='center')
        table.add_column("Menu", style='green', justify='center')

        table.add_row('1','Tambah Akun')
        table.add_row('2','Lihat Semua Akun')
        table.add_row('3','Setor Uang')
        table.add_row('4','Tarik Uang')
        table.add_row('5','Keluar', style='red')

        console.print(table)