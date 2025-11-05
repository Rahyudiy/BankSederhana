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
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"✅ Setoran berhasil. Saldo sekarang: Rp{int(self.__saldo)}")
        else:
            print("❌ Jumlah setoran harus lebih dari 0.")

  #tarik uang
    def withdraw(self, jumlah: float):
        if jumlah <= 0:
            print("❌ Jumlah penarikan tidak valid.")
            return
        if jumlah <= self.__saldo:
            self.__saldo -= jumlah
            print(f"✅ Penarikan berhasil. Sisa saldo: Rp{int(self.__saldo)}")
        else:
            print("❌ Penarikan gagal. Saldo tidak cukup.")
  #lihat uang
    def see_balance(self):
        print(f"💰 Saldo ({self.__account_number}) : Rp{int(self.__saldo)}")
        return self.__saldo

    def info(self) -> str:
        return f"Akun: {self.__account_number} | Nama: {self.__name} | Saldo: Rp{int(self.__saldo)}"
