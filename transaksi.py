from mahasiswa import Mahasiswa
from alat import Alat
from detail_transaksi import DetailTransaksi

class Transaksi:
    def __init__(self, id_transaksi: str, peminjam: Mahasiswa, tanggal_pinjam: str, batas_kembali: str):
        self.__id_transaksi = id_transaksi
        self.__peminjam = peminjam
        self.__tanggal_pinjam = tanggal_pinjam
        self.__batas_kembali = batas_kembali
        self.__status = "Dipinjam"
        self.__daftar_detail = []

    def tambah_item(self, alat: Alat) -> None:
        detail = DetailTransaksi(alat)
        self.__daftar_detail.append(detail)

    def kembalikan_item(self, kode_alat: str, tanggal: str, kondisi: str) -> bool:
        for detail in self.__daftar_detail:
            if detail.get_alat().get_kode() == kode_alat:
                if detail.is_sudah_kembali():
                    return False
                
                detail.proses_kembali(tanggal, kondisi)
                self.update_status_transaksi()
                return True
        return False

    def update_status_transaksi(self) -> None:
        jumlah_kembali = 0
        for detail in self.__daftar_detail:
            if detail.is_sudah_kembali():
                jumlah_kembali += 1

        if len(self.__daftar_detail) > 0 and jumlah_kembali == len(self.__daftar_detail):
            self.__status = "Selesai"
        elif jumlah_kembali > 0:
            self.__status = "Sebagian dikembalikan"
        else:
            self.__status = "Dipinjam"

    def is_aktif(self) -> bool:
        return self.__status != "Selesai"

    def get_peminjam(self) -> Mahasiswa:
        return self.__peminjam

    def get_daftar_detail(self) -> list:
        return self.__daftar_detail

    def __str__(self) -> str:
        baris = [
            (f"ID Transaksi: {self.__id_transaksi} | "
            f"Peminjam: {self.__peminjam.get_nama()} "
            f"({self.__peminjam.get_nim()})"),
            
            (f"Pinjam: {self.__tanggal_pinjam} | "
            f"Batas Kembali: {self.__batas_kembali} | "
            f"Status: {self.__status}")
        ]
        
        for detail in self.__daftar_detail:
            baris.append(f"  - {detail}")
        return "\n".join(baris)