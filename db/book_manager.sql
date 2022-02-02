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
