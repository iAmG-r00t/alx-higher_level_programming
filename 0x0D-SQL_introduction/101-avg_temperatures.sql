-- import database dump temperatures.sql to hbtn_0c_0 database
-- then lists average temp by city ordered by temp (desc)
-- source temperatures.sql;
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
