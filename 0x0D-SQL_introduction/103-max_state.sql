-- displays the max temprature of each state ordered by ststename
-- source temperatures.sql;
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state ASC;
