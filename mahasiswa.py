class Mahasiswa:

    def __init__(self, nim: str, nama: str, nomor_hp: str):
        self.__nim = nim
        self.__nama = nama
        self.__nomor_hp = nomor_hp

    def get_nim(self) -> str:
        return self.__nim

    def get_nama(self) -> str:
        return self.__nama

    def get_nomor_hp(self) -> str:
        return self.__nomor_hp

    def __str__(self) -> str:
        return f"{self.__nim} - {self.__nama} ({self.__nomor_hp})"