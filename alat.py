class Alat:

    def __init__(self, kode_alat: str, nama_alat: str, kategori: str, kondisi: str = "Baik"):
        self.__kode_alat = kode_alat
        self.__nama_alat = nama_alat
        self.__kategori = kategori
        self.__kondisi = kondisi
        self.__sedang_dipinjam = False

    def is_tersedia(self) -> bool:
        return self.__kondisi == "Baik" and not self.__sedang_dipinjam

    def set_kondisi(self, kondisi_baru: str) -> None:
        self.__kondisi = kondisi_baru
        
    def set_status_pinjam(self, status: bool) -> None:
        self.__sedang_dipinjam = status

    def get_kode(self) -> str:
        return self.__kode_alat

    def get_kategori(self) -> str:
        return self.__kategori

    def get_kondisi(self) -> str:
        return self.__kondisi

    def __str__(self) -> str:
        return f"{self.__kode_alat} - {self.__nama_alat} ({self.__kategori}) - Kondisi: {self.__kondisi}"
