-- Script that count the number of scores with same score

SELECT
	score,
	COUNT(*) AS number
FROM
	second_table
GROUP BY
	score
ORDER BY
	number DESC;
