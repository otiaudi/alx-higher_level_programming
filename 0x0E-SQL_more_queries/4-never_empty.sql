-- A script that creates a table id_not_null
-- The query to create the table  in MySQL server
CREATE TABLE IF NOT EXISTS 
	id_not_null (
       id INT DEFAULT 1,
       name VARCHAR(256));
