<h1 align="center">
  <br>
  Scraping Data Mobil Bekas
  <br>
  <br>
</h1>

<h4>
  Made By: I Kadek Yuda Budipratama Giri - 13516115
</h2>

### Description
Pada program ini, terdapat web crawler yang akan mengambil data dari <a href="https://www.mobil123.com/">https://www.mobil123.com/</a>. Data yang diambil merupakan data mobil bekas yang ditawarkan oleh website tersbeut. Pada program ini, semua jenis mobil bekas diambil datanya.


### Specifications
Program web crawler ini dibuat dengan spesfisikasi sebagai berikut:
  - __Python 3.6.2__
  - __BeautifulSoup 4.6.0__ sebagai library yang membantu mengambil data dari html</li>
  - __urllib__ sebagai library yang melakukan request kepada web untuk mengunduh web agar dapat dicrawl</li>
  - __JSON__ sebagai media penyimpanan data yang dicrawl</li>

Program web crawler dapat melakukan scraping data dengan mengakses https://www.mobil123.com/mobil-dijual/indonesiatype=used&page_number=X&page_size=Y dengan X adalah jumlah halaman yang ingin dicrawl dan Y adalah jumlah data per halaman. Total data yang diambil adalah X*Y. Pada program contoh, nilai X = 10 dan Y = 50, sehingga total data yang diambil adalah 500 data.

Data yang diambil adalah data harga, spesifikasi, jenis penjual, dan lokasi mobil bekas dijual. Spesifikasi meliputi merk, model, varian, tahun mobil dengan merk, model, dan varian mobil keluar, kapasitas mesin, transmisi, jumlah penumpang, dan warna mobil. Data yang sudah dicrawl akan disimpan dalam JSON dalam format `[Tanggal Crawling]-[Waktu Crawling Selesai]`

### How To Use
<p>
Untuk menggunakan program ini, cukup menjalankan  
  
```
make
```
pada directory yang menyimpan file "Makefile"
</p>

### JSON Structure
<p>File JSON terdiri atas sebuah list yang berisi seluruh data mobil bekas yang dikumpulkan. Elemen list terdiri atas sebuah dictionary yang memiliki struktur sebagai berikut:
  <ul>
    <li>"price" : harga dari mobil bekas</li>
    <li>"make" : merk dari mobil bekas</li>
    <li>"model" : model dari mobil bekas dengan merk yang diberikan</li>
    <li>"variant" : variasi dari mobil bekas dengan model dan merk yang diberikan</li>
    <li>"year": Tahun dari mobil dengan merk, model, dan varian tersbeut keluar</li>
    <li>"engine_cap" : Kapasitas mesin mobil dalam satuan cc </li>
    <li>"transmission" : Sistem transmisi yang digunakan mobil. (Manual/Automatic)</li>
    <li>"passenger_cap" : kapasitas penumpang </li>
    <li>"mileage" : Jarak total yang sudah ditempuh mobil</li>
    <li>"color" : Warna mobil bekas </li>
    <li>"seller" : Pihak yang menjual mobil </li>
    <li>"loc_province" : Provinsi lokasi penjualan mobil </li>
    <li>"loc_city" : Kota lokasi penjualan mobil</li>
  </ul>
</p>

### Screenshots
<img src="https://raw.githubusercontent.com/KadekYuda/Seleksi-2018/master/Tugas1/screenshots/screenshot_process.PNG">
<img src="https://raw.githubusercontent.com/KadekYuda/Seleksi-2018/master/Tugas1/screenshots/screenshot_process2.PNG">

### Reference
<p>Library yang dipakai:
  <ul>
    <li>BeautifulSoup4 https://www.crummy.com/software/BeautifulSoup/bs4/doc/</li>
    <li>JSON https://docs.python.org/2/library/json.html</li>
    <li>urllib https://docs.python.org/2/library/urllib.html</li>
  </ul>
</p>
