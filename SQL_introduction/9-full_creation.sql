-- Este script creara una tabla llamada second_table.

CREATE TABLE IF NOT EXISTS second_table (
	id INT AUTO_INCREMENT,
	name VARCHAR(256),
	score INT
);
INSERT INTO second_table (name, score) VALUES ('Jhon', 10), ('Alex', 3), ('Bob', 14), ('George', 8);
