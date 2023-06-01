class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self._nama = nama
        self._nim = nim
        self._jurusan = jurusan

    def nama(self):
        return self._nama

    def nim(self):
        return self._nim

    def jurusan(self):
        return self._jurusan.nama_jurusan

    def __str__(self):
        return f"Nama: {self.nama}\nNIM: {self.nim}\nJurusan: {self.jurusan}"


class Jurusan:
    def __init__(self, nama_jurusan):
        self._nama_jurusan = nama_jurusan
        self._daftar_mahasiswa = []

    def nama_jurusan(self):
        return self._nama_jurusan

    def daftar_mahasiswa(self):
        return self._daftar_mahasiswa

    def tambah_mahasiswa(self, mahasiswa):
        self._daftar_mahasiswa.append(mahasiswa)

    def __str__(self):
        if self._daftar_mahasiswa:
            daftar_mhs = "\n".join(str(mahasiswa) for mahasiswa in self._daftar_mahasiswa)
            return f"Daftar Mahasiswa di Jurusan {self._nama_jurusan}:\n{daftar_mhs}"
        else:
            return f"Belum ada mahasiswa terdaftar di jurusan {self._nama_jurusan}"


class Universitas:
    def __init__(self, nama_universitas):
        self._nama_universitas = nama_universitas
        self._daftar_jurusan = []

    @property
    def nama_universitas(self):
        return self._nama_universitas

    @property
    def daftar_jurusan(self):
        return self._daftar_jurusan

    def tambah_jurusan(self, jurusan):
        self._daftar_jurusan.append(jurusan)

    def __str__(self):
        if self._daftar_jurusan:
            daftar_jur = "\n".join(jurusan.nama_jurusan for jurusan in self._daftar_jurusan)
            return f"Daftar Jurusan di {self._nama_universitas}:\n{daftar_jur}"
        else:
            return f"Belum ada jurusan terdaftar di {self._nama_universitas}"


universitas_xyz = Universitas("XYZ University")

jurusan_ti = Jurusan("Teknik Informatika")
universitas_xyz.tambah_jurusan(jurusan_ti)

mahasiswa_andi = Mahasiswa("Andi", "G1a022089", jurusan_ti)
jurusan_ti.tambah_mahasiswa(mahasiswa_andi)

print(universitas_xyz)
print(jurusan_ti)

