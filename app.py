from flask import Flask, request 
import sqlite3
import pandas as pd 
app = Flask(__name__) 

# static endpoint 1 :
@app.route('/chinook')
def chinook():
    conn = sqlite3.connect('data_input/chinook.db')
    data = pd.read_sql_query(
    '''
    SELECT artists.Name AS ArtistName, albums.Title,
    customers.Country, genres.Name AS GenreName,
    media_types.Name AS MediaType, invoices.InvoiceDate AS DatePurchased,
    invoices.Total AS Total
    FROM customers
    LEFT JOIN invoices
    ON customers.CustomerId = invoices.CustomerId
    LEFT JOIN invoice_items
    ON invoices.InvoiceId = invoice_items.InvoiceId
    LEFT JOIN tracks
    ON invoice_items.TrackId = tracks.TrackId
    LEFT JOIN genres
    ON tracks.GenreId = genres.GenreId
    LEFT JOIN media_types
    ON tracks.MediaTypeId = media_types.MediaTypeId
    LEFT JOIN albums
    ON tracks.AlbumId = albums.AlbumId
    LEFT JOIN artists
    ON albums.ArtistId = artists.ArtistId
    ORDER BY Total DESC
    ''',
    conn,
    parse_dates='DatePurchased')
    data['MonthPurchased'] = data['DatePurchased'].dt.month_name()
    return (data.to_json())

# static endpoint 2:
@app.route('/mediatype') 
def mediatype():
    conn = sqlite3.connect('data_input/chinook.db')
    data = pd.read_sql_query(
    '''
    SELECT artists.Name AS ArtistName, albums.Title,
    customers.Country, genres.Name AS GenreName,
    media_types.Name AS MediaType, invoices.InvoiceDate AS DatePurchased,
    invoices.Total AS Total
    FROM customers
    LEFT JOIN invoices
    ON customers.CustomerId = invoices.CustomerId
    LEFT JOIN invoice_items
    ON invoices.InvoiceId = invoice_items.InvoiceId
    LEFT JOIN tracks
    ON invoice_items.TrackId = tracks.TrackId
    LEFT JOIN genres
    ON tracks.GenreId = genres.GenreId
    LEFT JOIN media_types
    ON tracks.MediaTypeId = media_types.MediaTypeId
    LEFT JOIN albums
    ON tracks.AlbumId = albums.AlbumId
    LEFT JOIN artists
    ON albums.ArtistId = artists.ArtistId
    ORDER BY Total DESC
    ''',
    conn,
    parse_dates='DatePurchased')
    data['MonthPurchased'] = data['DatePurchased'].dt.month_name()
    data_mediatype = data.groupby(['MediaType', 'MonthPurchased']).sum().\
    sort_values(by='Total', ascending=False).unstack().fillna(0)
    return (data_mediatype.to_json())

#static endpoints 3: (checking artist name)
@app.route('/artistlist')
def artistlist():
    conn = sqlite3.connect('data_input/chinook.db')
    artist_list = pd.read_sql_query(
    '''
    SELECT artists.Name as ArtistName, albums.Title, genres.Name as GenreName 
    FROM artists
    LEFT JOIN albums  
    ON artists.ArtistId = albums.ArtistId
    LEFT JOIN tracks
    ON albums.AlbumId = tracks.AlbumId
    LEFT JOIN genres
    ON tracks.GenreId = genres.GenreId
    ''',
    conn )
    return (artist_list.to_json())

# dynamic endpoint:
@app.route('/data/get/<artistname>', methods=['GET'])
def get_data(artistname):
    conn = sqlite3.connect('data_input/chinook.db')
    data = pd.read_sql_query(
    '''
    SELECT artists.Name AS ArtistName, albums.Title,
    customers.Country, genres.Name AS GenreName,
    media_types.Name AS MediaType, invoices.InvoiceDate AS DatePurchased,
    invoices.Total AS Total
    FROM customers
    LEFT JOIN invoices
    ON customers.CustomerId = invoices.CustomerId
    LEFT JOIN invoice_items
    ON invoices.InvoiceId = invoice_items.InvoiceId
    LEFT JOIN tracks
    ON invoice_items.TrackId = tracks.TrackId
    LEFT JOIN genres
    ON tracks.GenreId = genres.GenreId
    LEFT JOIN media_types
    ON tracks.MediaTypeId = media_types.MediaTypeId
    LEFT JOIN albums
    ON tracks.AlbumId = albums.AlbumId
    LEFT JOIN artists
    ON albums.ArtistId = artists.ArtistId
    ORDER BY Total DESC
    ''',
    conn,
    parse_dates='DatePurchased' )
    data['MonthPurchased'] = data['DatePurchased'].dt.month_name()
    artist = data[data['ArtistName'] == artistname]
    return (artist.to_json())


#untuk dokumentasi
@app.route("/docs")
def documentation():
    return '''
        <h1> Documentation </h1>
        <p> Repositori ini bertujuan untuk melengkapi Data Analytics Course, dengan pemilihan case Deploying Application Programming Interface (API).
        <p> Dalam repositori ini ada tiga (3) Static Endpoint dan satu (1) Dynamic Endpoint yang akan dijelaskan di point dibawah. 
        <p> Data source : `chinook.db`
        <h2> Static Endpoints 1 (apiccapstone.herokuapp.com/chinook) :</h2>
                <p> Static Endpoints 1 bertujuan untuk melihat total penjualan keseluruhan genre dengan artis siapa serta tipe media yg dibeli. 
                <p> Static Endpoints 1 akan menunjukkan kolom ArtistName, Title, Country (customers), GenreName, MediaType,
                <p> DatePurchased, Total, dan MonthPurchased. Sebagai contoh digunakan untuk melihat penjualan secara general per bulannya.

        <h2> Static Endpoints 2 (apiccapstone.herokuapp.com/mediatype) :</h2>
                <p> Static Endpoints 2 dibuat bertujuan untuk melihat total jumlah penjualan musik dengan tipe media per bulannya.
                <p> Static Endpoints 2 akan menunjukkan kolom MediaType (jenis tipe media yang customer beli) sebagai index dan Total (total pembelian) per bulannya.  
                <p> Sebagai contoh, Static Endpoint 2 untuk melihat jenis tipe media apa yang paling sering dibeli per bulannya dan perbandingannya.

        <h2> Static Endpoints 3 (apiccapstone.herokuapp.com/artistlist): </h2>
                <p> Static Endpoints 3 dibuat bertujuan agar user dapat melihat daftar nama artis yang berada
                <p> pada data `chinook.db` dan user dapat mengecek apakah data artis pilihannya berada didalam 
                <p> data `chinook.db`. Static Endpoints 3 akan menunjukkan kolom ArtistName (nama artis yang dipilih),
                <p> Title (judul album dari masing-masing artis), dan GenreName (genre dari artis tersebut). 

        <h2> Dynamic Endpoints (Artist Name) (apiccapstone.herokuapp.com/data/get/&lt;artistname&gt;) :</h2>
                <p> Dynamic Endpoints akan menunjukkan data dari nama artis yang dipilih saja. 
                <p> Misal ingin melihat di Negara apa lagu dari artis U2 lebih sering dibeli atau pada bulan apa lagu dari artis Aerosmith paling banyak dibeli.

        <p> Untuk mengecek data-data tersebut, anda bisa copy tautan link dibawah ini :
        <li> Static Endpoints 1 : https://apiccapstone.herokuapp.com/chinook
        <li> Static Endpoints 2 : https://apiccapstone.herokuapp.com/mediatype
        <li> Static Endpoints 3 : https://apiccapstone.herokuapp.com/artistlist
        <li> Dynamic Endpoint   : https://apiccapstone.herokuapp.com/data/get/&lt;artistname&gt;
        <p> Contoh khusus untuk Dynamic Endpoint : https://apiccapstone.herokuapp.com/data/get/Queen 

    '''


if __name__ == '__main__':
    app.run(debug=True, port=5000) 