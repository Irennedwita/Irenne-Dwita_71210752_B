class Karyawan:
    _nama = ""
    _umur = 0
    _jenisKelamin = None
    _upahPerHari = None

    def __init__(self,nama,umur):
        self._nama = nama
        self._umur = umur

    def getNama(self):
        return self._nama

    def getUmum(self):
        return self._umur

    def getJenisKelamin(self):
        return self._jenisKelamin

    def getUpahPerHari(self):
        return self._upahPerHari

    def setNama(self,nama):
        self._nama = nama

    def setUmum(self,umur):
        self._umur = umur

    def setJenisKelamin(self,jenisKelamin):
        self._jenisKelamin = jenisKelamin

    def setUpahPerHari(self,upahPerHari):
        self._upahPerHari = upahPerHari

    def printInfo(self):
        print("=" * 12, "INFO", "=" * 12)
        print("Nama\t\t:", self._nama)
        print("Umur\t\t:", self._umur)
        print("Jenis Kelamin\t:", self._jenisKelamin)
        print("Upah per Hari\t:", self._upahPerHari)

    def hitungGajiBulanan(self,hari):
        if hari != 30: 
            print("ERROR! Upah per Hari belum di inputkan") 
        else:
            total = self._upahPerHari * hari
            print("Gaji Bulan ini\t: Rp",(total))

if __name__ == "__main__":
    orang1 = Karyawan("Haniif", 90)
    orang1.printInfo()

    orang2 = Karyawan("Sindu", 190)
    orang2.setJenisKelamin("Laki-laki")
    orang2.setUpahPerHari(30000)
    orang2.printInfo()

    orang1.hitungGajiBulanan(28)
    orang2.hitungGajiBulanan(30)