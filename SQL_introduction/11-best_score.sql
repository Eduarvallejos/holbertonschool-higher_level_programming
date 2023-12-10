-- Este script enumera todos los registros de la tabla second_table que sean >= 10.

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
