-- A script that lists all records score>10
-- Result should display both  scores and namein this order)

SELECT 
	score, name
FROM
	second_table
WHERE
	score >= 10
ORDER BY
 	score DESC;
