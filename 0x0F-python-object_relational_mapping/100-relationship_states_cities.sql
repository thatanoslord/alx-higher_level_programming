Create the database
CREATE DATABASE IF NOT EXISTS hbtn_0e_100_usa;
USE hbtn_0e_100_usa;


CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    state_id INT NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);

INSERT INTO states (name) VALUES ('California'), ('Texas'), ('New York');

INSERT INTO cities (name, state_id) VALUES
('Los Angeles', 1),
('San Francisco', 1),
('Austin', 2),
('Dallas', 2),
('New York City', 3),
('Buffalo', 3);

SELECT * FROM states;
SELECT * FROM cities;
