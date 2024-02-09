from data import data

movies = data()

def category(genre):
    has = False
    for movie in movies:
        if movie["category"] == genre:
            has = True
            print(movie)
    if not has:
        print("sorry we don't have this category of movie")

name = input("what kind of movie do you wanna watch?\n")
category(name)