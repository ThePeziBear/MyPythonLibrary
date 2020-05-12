import matplotlib.pyplot as plt

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# Erstelle für die Movies eine numerische liste für die graphische Darstellung
xs = [i for i, _ in enumerate(movies)]

# Erstelle Bar - Chart; xs= X-Achse, num_oscars = Y-Achse
plt.bar(xs, num_oscars)
plt.ylabel("# of Academy Awards")
plt.title("My Favorite Movies")

# numerische Liste mit Movie Titel überschreiben
plt.xticks(xs, movies)

plt.show()
