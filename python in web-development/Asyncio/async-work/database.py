import psycopg2

SETTINGS = {
    "user": "",
    "password": ""
}

class DataBase:

    conn = psycopg2.connect(database="netologydb", user=SETTINGS['user'], password=SETTINGS['password'])

    def create_tables(self):
        with self.conn.cursor() as cur:
            cur.execute(f"""
            CREATE TABLE IF NOT EXISTS netology (
            id INT not null generated always as identity primary key,
            id_player BIGINT,
            birth_year TEXT,
            eye_color TEXT,
            films TEXT,
            gender TEXT,
            hair_color TEXT,
            height INT,
            homeworld TEXT,
            mass INT,
            name TEXT,
            skin_color TEXT,
            species TEXT,
            starships TEXT,
            vehicles TEXT
            );
            """)

            self.conn.commit()

    def add_player(self, id_player, birth_year, eye_color, films, gender, hair_color, height,
                   homeworld, mass, name, skin_color, species, starships, vehicles):
        with self.conn.cursor() as cur:
            cur.execute(f'''
            INSERT INTO netology (id_player, birth_year, eye_color, films, gender, hair_color, height, homeworld, mass, name, skin_color, species, starships, vehicles)
            VALUES({id_player}, {repr(birth_year)}, {repr(eye_color)}, {repr((" ".join(films)))}, {repr(gender)}, {repr(hair_color)}, {repr(height)}, {repr(homeworld)}, {mass}, {repr(name)}, {repr(skin_color)}, {repr((" ".join(species)))}, {repr((" ".join(starships)))}, {repr((" ".join(vehicles)))});
            ''')


            self.conn.commit()

db = DataBase()
db.create_tables()