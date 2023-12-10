-- Este script creara y dara todos los privilegios a un nuevo usuario llamdado user_0d_1 en el servidor MYSQL.

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
