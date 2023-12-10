-- Este script creara una nueva databae.
-- Creara una nueva tabla dentro de esta database.
-- Tendra 2 columnas (id, name).
-- ID : tendra un valor unico.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states (
	id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	name VARCHAR(256) NOT NULL
);
