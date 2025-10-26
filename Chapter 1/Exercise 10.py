#----------------------------Exercise 10------------------------

#This program creates a film dictionary and prints the details using Loop


# Creating a dictionary with film details

film = {
    "Title": "Inception",
    "Director": "Christopher Nolan",
    "Year": 2010,
    "Genre": "Science Fiction"
}


# Show details with loop
print("Film Details:")
for key, value in film.items():
    print(f"{key}: {value}")
