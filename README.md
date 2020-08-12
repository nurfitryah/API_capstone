# Documentation
Repositori ini bertujuan untuk melengkapi Data Analytics Course, dengan pemilihan case Deploying Application Programming Interface (API).
Dalam repositori ini ada dua (2) Static Endpoint dan satu (1) Dynamic Endpoint yang akan dijelaskan di point dibawah.

**Data source** : chinook.db

**Static Endpoints 1** (apiccapstone.heroku.com/chinook): 

Static Endpoints 1 bertujuan untuk melihat total penjualan keseluruhan genre dengan artis siapa serta tipe media yg dibeli. Static Endpoints 1 akan menunjukkan kolom ArtistName, Title, Country (customers), GenreName, MediaType, DatePurchased, Total, dan MonthPurchased. Sebagai contoh digunakan untuk melihat penjualan secara general per bulannya.

**Static Endpoints 2** (apiccapstone.heroku.com/mediatype):

Static Endpoints 2 dibuat bertujuan untuk melihat total jumlah penjualan musik dengan tipe media per bulannya. Static Endpoints 2 akan menunjukkan kolom MediaType (jenis tipe media yang customer beli) sebagai index dan Total (total pembelian) per bulannya. Sebagai contoh, Static Endpoint 2 untuk melihat jenis tipe media apa yang paling sering dibeli per bulannya dan perbandingannya.

**Dynamic Endpoints (Artist Name)** (apiccapstone.heroku.com/data/get/<artistname>): 
  
Dynamic Endpoints akan menunjukkan data dari nama artis yang dipilih saja. Misal ingin melihat di Negara apa lagu dari artis U2 lebih sering dibeli atau pada bulan apa lagu dari artis Aerosmith paling banyak dibeli.



Untuk mengecek data-data tersebut, anda bisa copy tautan link dibawah ini :
- Main               : https://apiccapstone.herokuapp.com/
- Static Endpoints 1 : https://apiccapstone.herokuapp.com/chinook
- Static Endpoints 2 : https://apiccapstone.herokuapp.com/mediatype
- Dynamic Endpoint   : https://apiccapstone.herokuapp.com/data/get/<artistname>

Contoh khusus untuk Dynamic Endpoint : https://apiccapstone.herokuapp.com/data/get/Queen 
