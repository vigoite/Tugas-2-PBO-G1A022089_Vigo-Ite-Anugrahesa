# Tugas-2-PBO-G1A022089_Vigo-Ite-Anugrahesa


Kelas Mahasiswa:

__init__(self, nama, nim, jurusan): Metode ini adalah konstruktor untuk kelas Mahasiswa. Itu menginisialisasi objek Mahasiswa dengan atribut nama, nim, dan jurusan.

nama(self): Metode ini mengembalikan nilai dari atribut _nama (nama mahasiswa).

nim(self): Metode ini mengembalikan nilai dari atribut _nim (NIM mahasiswa).

jurusan(self): Metode ini mengembalikan nama jurusan dari objek mahasiswa dengan mengakses atribut nama_jurusan dari objek jurusan yang terkait.

__str__(self): Metode ini mengembalikan representasi string dari objek Mahasiswa. Menampilkan nama, NIM, dan jurusan mahasiswa.



Kelas Jurusan:

__init__(self, nama_jurusan): Metode ini adalah konstruktor untuk kelas Jurusan. Itu menginisialisasi objek Jurusan dengan atribut nama_jurusan dan daftar_mahasiswa yang awalnya kosong.

nama_jurusan(self): Metode ini mengembalikan nilai dari atribut _nama_jurusan (nama jurusan).

daftar_mahasiswa(self): Metode ini mengembalikan daftar mahasiswa yang terdaftar dalam jurusan ini.

tambah_mahasiswa(self, mahasiswa): Metode ini digunakan untuk menambahkan objek Mahasiswa ke dalam daftar mahasiswa jurusan ini.

__str__(self): Metode ini mengembalikan representasi string dari objek Jurusan. Jika ada mahasiswa terdaftar, metode ini akan menampilkan daftar mahasiswa yang terdaftar dalam jurusan ini. Jika tidak ada mahasiswa, akan ditampilkan pesan yang sesuai.


Kelas Universitas:

__init__(self, nama_universitas): Metode ini adalah konstruktor untuk kelas Universitas. Itu menginisialisasi objek Universitas dengan atribut nama_universitas dan daftar_jurusan yang awalnya kosong.

nama_universitas(self): Metode ini mengembalikan nilai dari atribut _nama_universitas (nama universitas).

daftar_jurusan(self): Metode ini mengembalikan daftar jurusan yang terdaftar dalam universitas ini.

tambah_jurusan(self, jurusan): Metode ini digunakan untuk menambahkan objek Jurusan ke dalam daftar jurusan universitas ini.

__str__(self): Metode ini mengembalikan representasi string dari objek Universitas. Jika ada jurusan terdaftar, metode ini akan menampilkan daftar jurusan yang terdaftar dalam universitas ini. Jika tidak ada jurusan, akan ditampilkan pesan yang sesuai.

Selanjutnya, kode membuat objek universitas_xyz dari kelas Universitas dengan nama "XYZ University". Kemudian, objek jurusan_ti dibuat dari kelas Jurusan dengan nama "Teknik Informatika" kemudian ditambahkan ke objek universitas_xyz menggunakan metode tambah_jurusan(jurusan).

Setelah itu, objek mahasiswa_andi dibuat dari kelas Mahasiswa dengan parameter nama "Andi", NIM "G1a022089", dan objek jurusan_ti sebagai jurusan. Kemudian, objek mahasiswa_andi ditambahkan ke objek jurusan_ti menggunakan metode tambah_mahasiswa(mahasiswa).

Terakhir, dilakukan cetak (print) untuk objek universitas_xyz dan objek jurusan_ti. Ini akan memanggil metode __str__() untuk masing-masing objek dan mencetak informasi yang relevan.

Hasil output yang diharapkan adalah:

Daftar Jurusan di XYZ University:

Teknik Informatika


Daftar Mahasiswa di Jurusan Teknik Informatika:

Nama: Andi

NIM: G1a022089

Jurusan: Teknik Informatika
