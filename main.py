import ui
from artStoreDB import Artist, Artwork, ArtworkStoreDB

artworkStore = ArtworkStoreDB()


def main():
    while True:
        try:
            display_menu()
            choice = int(input('Enter choice: '))
            if choice == 1:
                add_artist()
            elif choice == 2:
                add_artwork()
            elif choice == 3:
                search_artwork_by_artist()
            elif choice == 4:
                display_available_artwork()
            elif choice == 5:
                change_availability()
            elif choice == 6:
                delete()
            elif choice == 7:
                print('Good bye!')
                break
            else:
                print('\nNot a valid choice.\n')
        except ValueError as e:
            print('\nPlease enter a numeric choice.\n')


def display_menu():
    print('''
    1: Add new artist
    2: Add new artwork
    3: Search artwork by artist
    4: Display available artwork
    5: Change availability
    6: Delete artwork
    7: Exit
    ''')


def add_artist():
    new_artist = ui.get_new_artist()
    new_artist.save()

def add_artwork():
    new_artwork = ui.get_new_artwork()
    new_artwork.save()

def search_artwork_by_artist():
    search_artist = input('Enter artist name: ').title().strip()
    matched_artwork = artworkStore.get_all_artworks(search_artist)
    ui.display_all_artwork(matched_artwork)

def display_available_artwork():
    available_artwork = artworkStore.get_available_artwork(True)
    ui.display_all_artwork(available_artwork)


def change_availability():

    art_id = ui.get_artwork_id()
    try:
        artwork = artworkStore.get_artwork_id(art_id)
        new_status = ui.get_availability_status()
        artwork.available = new_status
        Artwork.save(new_status)
        print('Availability has been changed. ')
    except:
        print('Error - no availability change made. ')


def delete():
    art_id = ui.get_artwork_id()
    try:
        artwork = artworkStore.get_artwork_id(art_id)
        Artwork.delete(artwork)
        print('Artwork has been deleted. ')
    except:
        print('Error - no artwork was deleted with that ID') 


if __name__ == "__main__":
    main()




