-- Este script creara una nueva database llamada hbtn_0d_2.
-- Creara un nuevo usuario llamado user_0d_2.
-- Este usuario solo tendra el privilegio de SELECT.

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
