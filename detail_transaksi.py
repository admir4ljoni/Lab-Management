from alat import Alat


class DetailTransaksi:
    def __init__(self, alat: Alat):
        self.__alat = alat
        self.__tanggal_kembali = None
        self.__kondisi = None
        self.__status = "Belum Kembali"

    def get_alat(self) -> Alat:
        return self.__alat

    def is_sudah_kembali(self) -> bool:
        return self.__status == "Sudah Kembali"

    def proses_kembali(self, tanggal: str, kondisi: str) -> None:
        self.__tanggal_kembali = tanggal
        self.__kondisi = kondisi
        self.__status = "Sudah Kembali"

    def update_status_transaksi(self) -> None:
        if self.is_sudah_kembali():
            self.__status = "Sudah Kembali"
        else:
            self.__status = "Belum Kembali"

    def __str__(self) -> str:
        if self.is_sudah_kembali():
            return (
                f"Alat: {self.__alat} | "
                f"Status: {self.__status} | "
                f"Tanggal Kembali: {self.__tanggal_kembali} | "
                f"Kondisi: {self.__kondisi}"
            )
        else:
            return (
                f"Alat: {self.__alat} | "
                f"Status: {self.__status}"
            )
