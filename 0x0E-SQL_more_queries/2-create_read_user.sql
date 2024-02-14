-- creates the database hbtn_0d_2 and the user user_0d_2

/*CREATE DATABASE
	IF NOT EXISTS `hbtn_0d_2`
CREATE USER
	IF NOT EXISTS 'user_0d_2'@'hbtn_0d_2'
	IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT
	ON `hbtn_0d_2`.*
	TO 'user_0d_2'@'hbtn_0d_2'
	IDENTIFIED BY 'user_0d_2_pwd';*/
-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege to the user on the database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
