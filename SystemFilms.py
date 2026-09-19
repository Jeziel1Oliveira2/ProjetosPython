import sqlite3

class Film:
    def __init__(self, name, year, genre, rating):
        self.name = name
        self.year = year
        self.genre = genre
        self.rating = rating

    def __str__(self):
        return f"Título do filme: {self.name} \nAno de lançamento: {self.year} \nGênero(s) do filme: {self.genre} \nNota do filme: {self.rating}"


class FilmsManager:
    def printFilms(self, id, film, year, genre, rating):
        print(f"ID: {id} \nTítulo do filme: {film} \nAno de lançamento: {year} \nGênero(s) do filme: {genre} \nNota do filme: {rating}\n {'-' * 30}")

    def __init__(self, database):
        self.database = database
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()
        self.createTable()

    def createTable(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS films(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                year INTEGER NOT NULL,
                genre TEXT NOT NULL,
                rating REAL NOT NULL)
            """)
        self.connection.commit()

    def addFilm(self, film):
        self.cursor.execute("""
            INSERT INTO films (name, year, genre, rating)
            VALUES (?, ?, ?, ?)
        """, (film.name, film.year, film.genre, film.rating))
        self.connection.commit()

    def listFilms(self):
        self.cursor.execute("SELECT * FROM films")
        films = self.cursor.fetchall()
        if not films:
            print("Nenhum filme cadastrado.")
            return

        for film in films:
            self.printFilms(film[0], film[1], film[2], film[3], film[4])

    def searchByGenre(self, genre):
        self.cursor.execute(
            """
            SELECT * FROM films WHERE genre = ?
            """, (genre,))
        films = self.cursor.fetchall()

        if not films:
            print(f"Nenhum filme encontrado do gênero {genre}.\n Tente outro gênero.")
            return

        for film in films:
             self.printFilms(film[0], film[1], film[2], film[3], film[4])

    def searchByAge(self, year):
        self.cursor.execute(
            """                
            SELECT * FROM films WHERE year = ?   
            """, (year,))
        
        films = self.cursor.fetchall()
    
        if not films:
            print(f"Nenhum filme encontrado do ano {year}.\n Tente outro gênero.")
            return
    
        for film in films:
                 self.printFilms(film[0], film[1], film[2], film[3], film[4])

    def searchByName(self, title):
            self.cursor.execute(
                """
                SELECT * FROM films WHERE name = ?
                """, (title,))
            films = self.cursor.fetchall()
    
            if not films:
                print(f"Nenhum filme encontrado com o título {title}.\n Tente outro título.")
                return
    
            for film in films:
                 self.printFilms(film[0], film[1], film[2], film[3], film[4])

    def deleteFilm(self, id):
        self.cursor.execute("""
            DELETE from films WHERE id = ?
        """, (id,))
        self.connection.commit()
        print(f"O filme com o ID {id} foi deletado")

manager = FilmsManager("films.db")
while True:
    print("Bem vindo a nossa biblioteca de filmes")
    print("Escolha uma das opções abaixo:")
    choice = int(input("1 - Cadastrar filme\n2 - Listar filmes\n3 - Buscar filme por gênero\n4 - Buscar filme por ano de lançamento\n5 - Buscar filme por título\n6 - Deletar filme\n7 - Sair\n"))
    match choice:
        case 1:
            name = input("Digite o nome do filme: ")
            year = int(input("Digite o ano de lançamento do filme: "))
            genre = input("Digite o gênero(s) do filme: ")
            rating = float(input("Digite a nota do filme: "))
            filmAdd = Film(name, year, genre, rating)
            manager.addFilm(filmAdd)
        case 2:
            manager.listFilms()
        case 3:
            genre = input("Digite o gênero do filme que deseja buscar:")
            manager.searchByGenre(genre)
        case 4:
            year = int(input("Digite o ano de lançamento do filme que deseja buscar:"))
            manager.searchByAge(year)
        case 5:
            title = input("Digite o título do filme que deseja buscar:")
            manager.searchByName(title)
        case 6:
            id = int(input("Digite o ID do filme que deseja deletar:"))
            manager.deleteFilm(id)
        case 7:
            print("Saindo do programa...")
            break
        case _:
            print("Opção inválida. Tente novamente.")