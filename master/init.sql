/* proxysql user */
CREATE USER IF NOT EXISTS 'monitor'@'%' IDENTIFIED BY 'monitor';

/* mysql exporter user */
CREATE USER IF NOT EXISTS 'exporter'@'%' IDENTIFIED BY 'password' WITH MAX_USER_CONNECTIONS 3;
GRANT PROCESS, REPLICATION CLIENT, SELECT ON *.* TO 'exporter'@'%';

/* slave user */
CREATE USER IF NOT EXISTS 'slave_user'@'%' IDENTIFIED BY 'password';
GRANT REPLICATION SLAVE ON *.* TO 'slave_user'@'%' WITH GRANT OPTION;

FLUSH PRIVILEGES;


create table users
(
	id int auto_increment,
	name varchar(255) null,
	constraint users_pk
		primary key (id)
);

INSERT INTO users VALUES (1, 'dipanjal'), (2, 'shohan');

