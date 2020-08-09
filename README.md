# API_capstone
Repositori ini bertujuan untuk melengkapi Data Analytics Course, dengan pemilihan case Deploying Application Programming Interface (API).

**Data source** : chinook.db

**Static Endpoints 1** (.../chinook): Static Endpoints 1 akan menunjukkan kolom ArtistName, Title, Country (customers), GenreName, MediaType, DatePurchased, Total, dan MonthPurchased. Contohnya digunakan untuk melihat penjualan secara general per bulannya. 

**Static Endpoints 2** (.../mediatype):
Static Endpoints 2 dibuat bertujuan untuk melihat total jumlah penjualan musik dengan tipe media per bulannya. Static Endpoints 2 akan menunjukkan kolom MediaType (jenis tipe media yang customer beli) sebagai index dan Total (total pembelian) per bulannya. Sebagai contoh, Static Endpoint 2 untuk melihat jenis tipe media apa yang paling sering dibeli per bulannya dan perbandingannya.

**Dynamic Endpoints (Artist Name)** (.../data/get/<artistname>): Dynamic Endpoints akan menunjukkan data dari nama artis yang dipilih saja. Misal ingin melihat di Negara apa lagu dari artis U2 lebih sering dibeli atau pada bulan apa lagu dari artis Aerosmith paling banyak dibeli.
