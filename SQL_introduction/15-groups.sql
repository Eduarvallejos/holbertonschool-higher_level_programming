-- Este script enumera la cantidad de registros con la misma puntacion de tabla second_table.

SELECT score, COUNT(*) AS number
from second_table
GROUP BY score
ORDER BY number DESC;
