from artStoreDB import Artist, Artwork, ArtworkStoreDB
import re

name_regex = "^(?=.{2,40}$)[a-zA-Z]+(?:[-'\s][a-zA-Z]+)*$"
email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def get_new_artist():
    flag = False
    name = input('Enter artist name: ').title().strip()
    while flag == False:
        if re.search(name_regex, name) is None:
            print('Invalid name. ')
            name = input('Please enter a valid name: ').title().strip()
        else:
            flag = True

    flag = False
    email = input('Enter artist email: ')
    while flag == False:
        if re.search(email_regex, email) is None:
            print('Invalid email. ')
            email = input('Please enter a valid artist email: ')
        else:
            flag = True
    return Artist(name=name, email=email)


def get_new_artwork():

    flag = False
    name = input('Enter artist name: ').title().strip()
    while flag == False:
        if re.search(name_regex, name) is None:
            print('Invalid name. ')
            name = input('Please enter a valid name: ').title().strip()
        else:
            flag = True

    flag = False
    artwork_name = input('Enter artwork name: ').title().strip()
    while flag == False:
        if re.search(name_regex, artwork_name) is None:
            print('Invalid artwork name. ')
            email = input('Please enter a valid artwork name: ')
        else:
            flag = True

    flag = False
    price = 'Enter artwork price: '
    while flag == False:
        art_price = input(price)
        try:
            art_price = float(art_price)
            if art_price <=0:
                print('Please enter whole or decimal price, no spaces. ')
            else:
                flag = True
        except ValueError:
            print('Invalid price entered. ')
        
    return Artwork(name=name, title=artwork_name, price=art_price)


def display_all_artwork(all_artworks):
    if all_artworks:
        for artwork in all_artworks:
            print(artwork)
    else:
        print('No artwork to display')


def get_artwork_id():
    while True:
        try:
            id = int(input('Enter artwork ID: '))
            if id > 0:
                return id
            else:
                print('Please enter a positive number.')

        except ValueError:
            print('Please enter a number.')


def get_availability_status():
    while True:
        response = input('Enter \'yes\' if artwork is available or \'no\' if NOT available. ')
        if response.lower() in ['yes', 'no']:
            return response.lower() == 'yes'
        else:
            print('Type \'yes\' or \'no\'')

            