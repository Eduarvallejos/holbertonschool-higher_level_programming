-- Enumera todad las ciudades de california que se puededan encontrar dentro de la database 'hbtn_0d_usa'.

USE hbtn_0d_usa;

SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY cities.id ASC;
