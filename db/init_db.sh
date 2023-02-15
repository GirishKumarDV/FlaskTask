
docker exec mysql -uroot -proot -e '
use task_db;
CREATE TABLE if not exists tasks(id int not null auto_increment primary key, title varchar(100), stack varchar(120), mentors varchar(120));
CREATE TABLE if not exists users(id int not null auto_increment primary key, u_name varchar(100));'

