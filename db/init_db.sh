mysql -uroot -proot -e "
SET CHARSET UTF8;
DROP DATABASE IF EXISTS task_db;;
CREATE DATABASE task_db DEFAULT CHARACTER SET utf8;
SET CHARACTER_SET_CLIENT = utf8;
SET CHARACTER_SET_CONNECTION = utf8;
use task_db;
CREATE TABLE if not exists tasks(id int not null auto_increment primary key, title varchar(100), stack varchar(120), mentors varchar(120));
CREATE TABLE if not exists users(id int not null auto_increment primary key, u_name varchar(100));
GRANT ALL ON *.* TO 'root';
"

