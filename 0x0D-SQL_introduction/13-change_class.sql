-- A script that removes all records with a score <= 5 
-- Query will delete all records with score<= 5

DELETE 
FROM
	second_table
WHERE
	score<= 5;
