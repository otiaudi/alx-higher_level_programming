-- Script that displays the max temperature of each state
-- Order by state name

SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
