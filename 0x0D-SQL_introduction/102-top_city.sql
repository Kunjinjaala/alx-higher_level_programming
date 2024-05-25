--- Write a script that displays the top 3 of cities temperature by temperature
SELECT city, temperatures
FROM temperatures WHERE month IN ('July', 'August')
ORDER BY value DESC LIMIT 3;
