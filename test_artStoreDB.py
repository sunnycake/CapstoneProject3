import sqlite3
import unittest
from unittest import TestCase

import artStoreDB

class TestMileageDB(TestCase):

    test_db_url = 'test_artworkStore.sqlite'

    def setUp(self):
        # Overwrite the artStore db_url with the test database URL
        artStore.sqlite.db_url = self.test_db_url
        with sqlite3.connect(self.test_db_url) as conn:
            conn.execute('CREATE TABLE IF NOT EXISTS Artist (ArtistName TEXT PRIMARY KEY NOT NULL UNIQUE, Email TEXT NOT NULL UNIQUE)')
            conn.execute('CREATE TABLE IF NOT EXISTS Artwork (ArtistName TEXT NOT NULL, ArtworkName TEXT NOT NULL UNIQUE, Price FLOAT NOT NULL, Available BOOLEAN, FOREIGN KEY (ArtistName) REFERENCES Artist (ArtistName))')
        conn.close()

        # drop everything from the DB to always start with an empty database
        with sqlite3.connect(self.test_db_url) as conn:
            conn.execute('DELETE FROM Artist')
            conn.execute('DELETE FROM Artwork')

        conn.close()


    def test_add_new_artist(self):

        artStoreDB.add_artist('John Smith', 'johnsmith@gmail.com')
        expected = { 'John Smith': 'johnsmith@gmail.com' }
        self.compare_db_to_expected(expected)


if __name__ == '__main__':
    unittest.main()