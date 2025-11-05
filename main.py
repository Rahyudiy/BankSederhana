# main.py
from controllers.bankController import BankController
from views.menuView import MenuView
from rich.console import Console
from rich.panel import Panel


def main():
    console = Console()
    controller = BankController()

    # contoh akun awal
    controller.addAccount("biasa", "001", "I Putu", 500000)
    controller.addAccount("premium", "002", "Ni Made", 200000)

    #memilih memu
    while True:
        MenuView.lihatMenu()

        console.print(Panel.fit("[bold blue] Masukan menu pilihan anda"))    
        pilihan = console.input("[bold blue]> Pilih Menu: ").strip()

        if pilihan == "1":
            acc_type = input("Tipe akun (biasa/premium): ").strip()
            acc_no = input("Nomor akun: ").strip()
            name = input("Nama nasabah: ").strip()
            try:
                balance = float(input("Saldo awal: ").strip())
            except ValueError:
                print("❌ Saldo harus berupa angka.")
                continue
            controller.addAccount(acc_type, acc_no, name, balance)

        elif pilihan == "2":
            controller.showAllAccounts()

        elif pilihan == "3":
            acc_no = console.input("[bold blue]Masukkan nomor akun untuk setor: ").strip()
            try:
                jumlah = float(input("Jumlah setor: ").strip())
            except ValueError:
                console.print("[red italic] ❌ Jumlah harus angka.")
                continue
            controller.deposit(acc_no, jumlah)

        elif pilihan == "4":
            acc_no = console.input("[blue bold]Masukkan nomor akun untuk tarik: ").strip()
            try:
                jumlah = float(input("Jumlah tarik: ").strip())
            except ValueError:
                console.print("[red italic]❌ Jumlah harus angka.")
                continue
            controller.withdraw(acc_no, jumlah)

        elif pilihan == "5":
            console.print("[green italic]👋 Terima kasih. Program selesai.")
            break

        else:
            console.print("[red italic]❌ Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()
