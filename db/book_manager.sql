DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS publishers;


CREATE TABLE publishers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    location VARCHAR(255),
    active BOOLEAN
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    publisher_id INT REFERENCES publishers(id), 
    author VARCHAR(255),
    genre VARCHAR(255),
    stock INT,
    cost_price FLOAT,
    sale_price FLOAT,
    markup FLOAT,
    image VARCHAR(255),
    blurb TEXT
);

-- INSERT INTO publishers(name, location, active) VALUES ('Penguin', 'London', True);
-- INSERT INTO publishers(name, location, active) VALUES ('Faber', 'London', True);
-- INSERT INTO publishers(name, location, active) VALUES ('Canongate', 'Edinburgh', True);
-- INSERT INTO publishers(name, location, active) VALUES ('SPAM Press', 'Glasgow', True);
-- INSERT INTO publishers(name, location, active) VALUES ('Wild Hawthorn Press', 'Edinburgh', False);

-- INSERT INTO books(title, publisher_id, author, genre, stock, cost_price, sale_price, markup, blurb) VALUES ('A Little Larger than the Entire Universe', 1, 'Fernando Pessoa', 'poetry', 3, 7.00, 10.99, 3.99, 'The definitive English translation of the iconic Portugeuse poet.');
-- INSERT INTO books(title, publisher_id, author, genre, stock, cost_price, sale_price, markup, blurb) VALUES ('One Hundred Years of Solitude', 1, 'Gabriel Garcia Marquez', 'magical realism', 5, 6.00, 10.99, 4.99, 'One of the greatest novels of the twentieth century - a timeless classic.');
-- INSERT INTO books(title, publisher_id, author, genre, stock, cost_price, sale_price, markup, blurb) VALUES ('PORTS', 4, 'Calum Rodger', 'poetry', 4, 3.00, 5.00, 2.00, 'Classic twentieth century poems reimagined as videogame instructions.');
-- INSERT INTO books(title, publisher_id, author, genre, stock, cost_price, sale_price, markup, blurb) VALUES ('Rapel', 5, 'Ian Hamilton Finlay', 'concrete poetry', 5, 50.00, 150.00, 50.00, 'Scottish poet''s first concrete poetry collection - ultra rare!');


