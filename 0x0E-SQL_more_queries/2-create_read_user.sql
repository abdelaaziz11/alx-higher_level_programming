-- creates the database hbtn_0d_2 and the user user_0d_2

CREATE DATABASE
	IF NOT EXISTS hbtn_0d_2
	IDENTIFIED BY user_0d_2_pwd;
CREATE USER
	SELECT PRIVILEGES
	IF NOT EXISTS 'user_0d_2'@'hbtn_0d_2';
