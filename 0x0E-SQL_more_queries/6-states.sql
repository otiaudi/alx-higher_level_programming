-- Script that creates the database hbtn_0d_usa and the table states
-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- use the databases.
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states ( 
	id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
	name VARCHAR(256) NOT NULL);
