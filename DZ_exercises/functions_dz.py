# Ex 8.1

def display_message():
    """ Show message on the display """

    print("This topic about functions.")
display_message()

# Ex 8.2
my_favorite_book = input("What is the Author and Name of your favorite book? ")

def favorite_book(my_favorite_book):
    """ Show name of book with its author name """

    print(f"Your favorite book is {my_favorite_book.title()}.")
favorite_book(my_favorite_book)

# Ex 8.3

shirt_size = input("Please, tel me, what is size of your shirt? (in number)")
shirt_text = input("What text would do you like on your shirt? ")
shirt_size_int = int(shirt_size)

def make_shirt(size, text):
    """ Show size of the shirt """

    print(f"Your variant: {text}.")
    print(f"Your shirt is {size}.")
make_shirt(shirt_size_int, shirt_text)

# Ex 8.4

def make_shirt_large(size='L', text='I love Python'):
    """ Show size of the shirt """

    print(f"This shirt has {size}.")
    print(f"Text on this shirt - {text}.")

make_shirt_large()

make_shirt_large(size='M')
make_shirt_large(text='I like LINUX a lot')

# Ex 8.5

def describe_city(city_name='Reykjavik', country_name='Iceland'):
    """ Show datain message """

    show_message = f"{city_name.title()} is in {country_name.title()}."
    print(show_message)

describe_city(city_name='London', country_name='Great Britain')
describe_city(city_name='San-Francisco', country_name='USA')
describe_city(city_name='Borgarnes')
describe_city(city_name='Agilsstadir')

# Ex 8.6
def city_country(name_of_the_city, name_of_the_country):
    """ Show the message about name of the city and name of the country of this city """

    print(f"{name_of_the_city.title(), name_of_the_country.title()}")

city_country('leipzig', 'germany')
city_country('lviv', 'ukraine')
city_country('san-francisco', 'usa')

# Ex 8.7

def make_album(author_name, album_name, count_of_songs=None):
    """ Show message about name of the author, name of the song album, and count of the songs """

    album_example = {'author': author_name, 'album_title': album_name}
    if count_of_songs:
        album_example['count_of_songs'] = count_of_songs
    return album_example

album_1 = make_album('Monatik', 'Smart Trees')
print(album_1)

album_2 = make_album('Linkin Park', 'Numb', count_of_songs=15)
print(album_2)

album_3 = make_album('Jay Sean', 'Ride It')
print(album_3)

# Ex 8.8

def make_my_albums(name_of_author, name_of_album, songs_count=None):
    """ Show message about name of the author, name of the album as a get data of the user """

    my_album_example = {'author': name_of_author, 'album_title': name_of_album}
    if songs_count:
        my_album_example['songs_count'] = songs_count
    return my_album_example



get_user_data_album_name = input("What is name of your favorite music album? ")
get_user_data_album_author_name = input("What is author's name of your favorite music album? ")
user_continue = input("Would you like to exit of the program? Write Yes / No")

while True:
    continue_repeat = input(user_continue)
    if continue_repeat != 'Yes':
        break

    user_data_album_name = input(get_user_data_album_name)
    user_album_author_name = input(get_user_data_album_author_name)

    my_album = make_my_albums(get_user_data_album_author_name, get_user_data_album_name)
    print(my_album)

# Ex 8.9
