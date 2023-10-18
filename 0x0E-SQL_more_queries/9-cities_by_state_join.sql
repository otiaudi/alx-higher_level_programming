-- This script lists all cities contained in the database
-- Query that provides a list of cities
SELECT cities.id, cities.name, states.name -- Query to join cities and states
FROM cities
JOIN states ON cities.state_id = states.id;

