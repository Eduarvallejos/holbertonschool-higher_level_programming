-- Este script creara una tabla de nombre id_not_null.
-- la fila id tendra un valor predeterminado.

CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT '1' NOT NULL,
	name VARCHAR(256)
);
