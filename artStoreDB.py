import sqlite3

db = 'artStore.sqlite'

class Artist:

    def __init__(self, name, email, id=None):
        self.name = name
        self.email = email
        self.id = id

        self.artistdb = ArtworkStoreDB()

    def save(self):
        self.artistdb.add_artist(self)

    def delete(self):
        self.artistdb.delete_artist(self)
    
    def __str__(self):
        return f'ID: {self.id} | Name: {self.name} | Email: {self.email}'
    

class Artwork:
    def __init__(self, name, title, price, available=True, id=None):
        self.name = name
        self.title = title
        self.price = price
        self.available = available
        self.id = id

        self.artworkdb = ArtworkStoreDB()

    def save(self):
        self.artworkdb.add_artwork(self)

    def delete(self):
        self.artworkdb.delete_artwork(self)

    def __str__(self):
        availability_status = 'yes' if self.available else 'no'
        return f'ID: {self.id} | Artist: {self.name} | Artwork Name: {self.title} | Price: {self.price} | Available: {availability_status}'
    
    # def __repr__(self):
    #     return f'ID {self.id} Title: {self.title} Author: {self.author} Read: {self.read}'


def create_table():
    with sqlite3.connect(db) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS Artist (ArtistName TEXT PRIMARY KEY NOT NULL UNIQUE, Email TEXT NOT NULL UNIQUE)')

    with sqlite3.connect(db) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS Artwork (ArtistName TEXT NOT NULL, ArtworkName TEXT NOT NULL UNIQUE, Price FLOAT NOT NULL, Available BOOLEAN, FOREIGN KEY (ArtistName) REFERENCES Artist (ArtistName))')
    conn.close()

class ArtworkStoreDB():

    def add_artist(self, artist):

        try:
            with sqlite3.connect(db) as conn:
                query = conn.execute('INSERT INTO Artist VALUES (?, ?)', (artist.name, artist.email))
                new_id =query.lastrowid
                artist.id = new_id 
        except sqlite3.IntegrityError as e:
            print('Error - Artist already exists in the database. ', e)
        finally:
            conn.close()


    def add_artwork(self, artwork):
        try:
            with sqlite3.connect(db) as conn:
                query = conn.execute('INSERT INTO Artwork VALUES (?, ?, ?, ?)', (artwork.name, artwork.title, artwork.price, artwork.available))
                new_id =query.lastrowid
                artwork.id = new_id 
        except sqlite3.IntegrityError as e:
            print('Error - Artwork already exists in the database. ', e)
        finally:
            conn.close()
    

    def delete_artwork(self, artwork):
        if not artwork.id:
            print('Artwork does not have ID')

        with sqlite3.connect(db) as conn:
            query = conn.execute('DELETE FROM Artwork WHERE rowid = ?', (artwork.id, ))
            deleted_count = query.rowcount 
        conn.close()

        if deleted_count == 0:
            print(f'Artwork with id {id} not found in store.')  


    def get_all_artworks(self, term):
        search = f'%{term}%'

        conn = sqlite3.connect(db)
        conn.row_factory = sqlite3.Row
        results = conn.execute('SELECT rowid, * FROM Artwork WHERE UPPER (ArtistName) like UPPER(?)', (search, ))
        artworks = []
        for row in results:
            artwork = Artwork(row['ArtistName'], row['ArtworkName'], row['Price'], row['Available'], row['rowid'])
            artworks.append(artwork)
        conn.close()

        return artworks


    def get_available_artwork(self, artist):
        conn = sqlite3.connect(db)
        results = conn.execute('SELECT * FROM Artwork WHERE available = ?', (artist,))
        artworks = [Artwork(*row) for row in results.fetchall()]
        conn.close()

        return artworks


    def get_artwork_id(self, id):
        get_book_by_id_sql = 'SELECT rowid, * FROM Artwork WHERE rowid = ?'

        con = sqlite3.connect(db)
        con.row_factory = sqlite3.Row 
        rows = con.execute(get_book_by_id_sql, (id,))
        results = rows.fetchone() 
        if results:
            artwork = Artwork(results['ArtistName'], results['ArtworkName'], results['Price'], results['Available'], results['rowid'])

        con.close()

        return artwork


create_table()
