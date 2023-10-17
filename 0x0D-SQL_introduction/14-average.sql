-- Script that computes the score average of all records in the table
-- Table is second_table in  database hbtn_0c_0

SELECT 
	AVG(score) AS average
FROM
	second_table
