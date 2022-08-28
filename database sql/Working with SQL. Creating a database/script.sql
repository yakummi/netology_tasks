create table if not exists genres (
genre_id INT not null generated always as identity primary key,
genre_name VARCHAR(75) unique not null
);

create table if not exists artists (
artist_id INT not null generated always as identity primary key,
artist_name VARCHAR(75) unique not null
);

create table if not exists artists_genres (
artist_genre_id INT not null generated always as identity primary key,
id_genre INT,
id_artist INT,
foreign KEY(id_genre) references genres (genre_id) on delete set null,
foreign KEY(id_artist) references artists (artist_id) on delete set null
);

create table if not exists albums (
album_id INT not null generated always as identity primary key,
album_name VARCHAR(100) not null,
release_year DATE
);

create table if not exists artists_albums (
artist_album_id INT not null generated always as identity primary key,
id_artist INT,
id_album INT,
foreign KEY(id_artist) references artists (artist_id) on delete set null,
foreign key (id_album) references albums (album_id) on delete set null
);

create table if not exists digests (
id_digest INT not null generated always as identity primary key,
digest_name VARCHAR(80) not null,
release_year DATE
);

create table if not exists compositions (
id_composition INT not null generated always as identity primary key,
composition_name VARCHAR(90) not null,
duration DECIMAL(4, 1),
album_id INT,
foreign KEY(album_id) references albums (album_id) on delete set null 
);

create table if not exists compositions_digests (
compositions_digest_id INT not null generated always as identity primary key,
composition_id INT,
digest_id INT,
foreign KEY(composition_id) references compositions (id_composition) on delete set null,
foreign KEY(digest_id) references digests (id_digest) on delete set null 
);