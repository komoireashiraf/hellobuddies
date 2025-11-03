# Define class Movie
class Movie:
    def __init__(self, title, seats):
        self.title = title
        self.seats = seats

    def book_seat(self):
        """Decrease seat count if available"""
        if self.seats > 0:
            self.seats -= 1
            return True
        else:
            return False

    def __str__(self):
        return f"{self.title} ({self.seats} seats left)"


# Define BookingSystem class
class BookingSystem:
    def __init__(self):
        self.movies = {}

    def add_movie(self, movie):
        """Add a movie to the system"""
        self.movies[movie.title] = movie

    def book_seat(self, title):
        """Try booking a seat for the given movie title"""
        if title in self.movies:
            if self.movies[title].book_seat():
                print(f"✅ Seat booked for '{title}'")
            else:
                print(f"❌ No seats left for '{title}'")
        else:
            print(f"❌ Movie '{title}' not found.")

    def available_movies(self):
        """Show movies with seats available"""
        print("\n🎬 Available Movies:")
        for movie in self.movies.values():
            if movie.seats > 0:
                print(movie)


# --- Steps in action ---
# 1. Add 3 movies
m1 = Movie("Mr. Bean's Holiday", 3)
m2 = Movie("Interstellar", 2)
m3 = Movie("The Dark Knight", 1)

system = BookingSystem()
system.add_movie(m1)
system.add_movie(m2)
system.add_movie(m3)

# 2. Book several seats
system.book_seat("Inception")
system.book_seat("Inception")
system.book_seat("Interstellar")
system.book_seat("The Dark Knight")
system.book_seat("The Dark Knight")  # trying when full

# 3. Show available movies
system.available_movies()

