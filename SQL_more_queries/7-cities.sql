-- Este script creara la database hbtn_0d_usa si no existe.
-- Creara la tabla 'cities' dentro de esta si no existe.
-- Contara con 3 columnas (id, state_id, name).

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities (
	id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY(state_id) REFERENCES states(id)
);
