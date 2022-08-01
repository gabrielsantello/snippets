--SQL
--Concerning about SQL, we don't have to load all the dataset locally to make queries.
--When we think about Pandas, we have to.
SELECT *
FROM df
LIMIT 10 --First 10 entries

SELECT name, age
FROM df --Returns 'name' and 'age' columns

SELECT *
FROM df
WHERE city = 'New York'
AND salary >= 10000 --Query 'WHERE'

SELECT country, COUNT(*)
FROM df
GROUP BY country --Group By and Count