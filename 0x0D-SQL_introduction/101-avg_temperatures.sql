--a script that displays the average temperature by order
SELECT city, AVG(value) as average_temp
FROM temperatures GROUP BY city
ORDER BY average_temp DESC;
