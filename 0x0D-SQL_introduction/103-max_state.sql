--- Write a script that displays the max temperature of each state
SELECT state, MAX(value) as maximum_temp
FROM temperatures GROUP BY state
ORDER BY maximum_temp
