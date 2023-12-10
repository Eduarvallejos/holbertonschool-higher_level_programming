-- Este script enumera todos las ciudades contenidas dentro de la database 'hbtn_0d_usa'

SELECT
    cities.id,
    cities.name,
    states.name
FROM
    cities
JOIN
    states ON cities.state_id = states.id
ORDER BY
    cities.id ASC;
