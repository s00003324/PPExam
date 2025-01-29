import json

class MovieNotFoundError(Exception):
    pass

class MovieLibrary:
    def __init__(self, json_file):
        self.file_path = json_file
        try:
            with open(json_file, 'r') as file:
                self.movies = json.load(file)
        except FileNotFoundError: 
            print(f"File not found {json_file}")
            self.movies = []

# add - remove - update section

    def add_movie(self, title, director, year, genres): 
        for movie in self.movies:
            if movie["title"].lower() == title.lower():
                print(f"Title '{title}' is already in the library.")
                return
        new_movie = {"title": title, "director": director, "year": year, "genres": genres}
        self.movies.append(new_movie)
        print(f"The movie '{title}' has been added.")
        with open(self.file_path, "w") as file:
            json.dump(self.movies, file, indent=4)

    def remove_movie(self, title): 
        for movie in self.movies:
            if movie["title"].lower() == title.lower():
                self.movies.remove(movie)
                print(f"The movie '{title}' has been deleted.")
                with open(self.file_path, "w") as file:
                    json.dump(self.movies, file, indent=4)
                return
        raise MovieNotFoundError("Movie was not found.") 
    
    def update_movie(self, title, director=None, year=None, genres=None): 
        for movie in self.movies:
            if movie["title"].lower() == title.lower():
                if director is not None:
                    movie["director"] = director
                if year is not None:
                    movie["year"] = year
                if genres is not None:
                    movie["genres"] = genres
                print(f"The movie '{title}' has been updated.")
                with open(self.file_path, "w") as file:
                    json.dump(self.movies, file, indent=4)
                return
        raise MovieNotFoundError(f"Movie '{title}' was not found.")

  #search section / get - count

    def get_movies(self): 
        return self.movies
    
    def get_movie_titles(self): 
        titles = []
        for movie in self.movies:
            titles.append(movie["title"])
        return titles
    
    def count_movies(self): 
        return len(self.movies)
    
    def get_movie_by_title(self, title): 
        for movie in self.movies:
            if movie["title"].lower() == title.lower():
                return movie
        return None
    
    def get_movies_by_little_substring(self, substring):  
        results = []
        for movie in self.movies:
            if substring in movie["title"]:
                results.append(movie)
        return results
    
    def get_movies_by_year(self, year): 
        results = []
        for movie in self.movies:
            if movie["year"] == year:
                results.append(movie)
        return results
    
    def count_movies_by_director(self, director): 
        count = 0
        for movie in self.movies:
            if movie["director"].lower() == director.lower():
                count += 1
        return count
    
    def get_movies_by_genre(self, genre): 
        results = []
        for movie in self.movies:
            for g in movie["genres"]:
                if genre.lower() == g.lower():
                    results.append(movie)
                    break
        return results
    
    def get_oldest_movie_title(self): 
        if not self.movies:
            return None
        oldest_movie = self.movies[0]
        for movie in self.movies:
            if movie["year"] < oldest_movie["year"]:
                oldest_movie = movie
        return oldest_movie["title"]
    
    def get_average_release_year(self): 
        if not self.movies:
            return None
        total_years = 0
        for movie in self.movies:
            total_years += movie["year"]
        return total_years / len(self.movies)
    
    def get_longest_title(self): 
        if not self.movies:
            return None
        longest_movie = self.movies[0]
        for movie in self.movies:
            if len(movie["title"]) > len(longest_movie["title"]):
                longest_movie = movie
        return longest_movie["title"]
    
    def get_titles_between_years(self, start_year, end_year): 
        results = []
        for movie in self.movies:
            if start_year <= movie["year"] <= end_year:
                results.append(movie["title"])
        return results
    
    def get_most_common_year(self): 
        if not self.movies:
            return None
        year_counts = {}
        for movie in self.movies:
            year = movie["year"]
            if year not in year_counts:
                year_counts[year] = 0
            year_counts[year] += 1
        return max(year_counts, key=year_counts.get)
    
    