-- displays the top 3 of cities temp during July and August ordered by temp DESC
-- source temperatures.sql;
 
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month BETWEEN '7' AND '8'
GROUP BY city
ORDER BY avg_temp DESC LIMIT 3;
