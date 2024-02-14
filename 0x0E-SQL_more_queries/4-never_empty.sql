-- creates the table id_not_null on your MySQL server.
SELECT 1 FROM information_schema.tables
WHERE table_schema = DATABASE() AND table_name = 'id_not_null' LIMIT 1;
CREATE TABLE IF NOT EXISTS id_not_null
(
	id INT = DEFAULT 1,
	name VARCHAR(256)
);
