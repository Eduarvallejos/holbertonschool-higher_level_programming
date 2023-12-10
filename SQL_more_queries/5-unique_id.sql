-- Este script crea una tabla de nombre unique_id.
-- Tendra un valor predeterminado y unico en la columna id.

CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT '1' UNIQUE,
	name VARCHAR(256)
);
