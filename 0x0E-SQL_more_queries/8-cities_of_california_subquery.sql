-- A script which lists all the cities of California registered in the database
SELECT 
	id, name 
FROM 
	cities
WHERE 
	state_id = ( 
      SELECT id
      FROM 
	states
      WHERE
	name = "California");
