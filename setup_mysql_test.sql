-- A script to do things that should be done
CREATE DATABASE IF NOT EXISTS 'hbnb_dev_db';
CREATE USER IF NOT EXISTS 'hbnb_text'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
