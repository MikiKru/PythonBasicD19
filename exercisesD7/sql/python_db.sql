# utworzenie db
create database python_db;
use python_db;

# uworzenie nowego użytkownika na serwerze lokalnym
create user 'python_user'@'localhost' identified by 'qwe123';

# przypisanie uprawnien do użytkownika
grant INSERT, SELECT, DELETE, UPDATE 
	on python_db.* 
    to 'python_user'@'localhost';
    
# DDL for project PYTHON DATABASE
create table user(
	user_id int primary key auto_increment,
    email varchar(55) unique not null,
    password varchar(255) not null,
    name varchar(55) not null,
    lastname varchar(55) not null,
    gender enum('M','K')
);
create table task (
	task_id int primary key auto_increment,
    name varchar(255) not null,
    description text not null,
    status enum('nowe','w toku', 'wykonane') default 'nowe',
    date_start datetime default now(),
    date_stop date not null,
    user_id int,
	foreign key (user_id) references user (user_id)
);
create table subtask(
	subtask_id int primary key auto_increment,
    detail_description text not null,
    deadline date not null,
    status enum('otwarte','wykonane') default 'otwarte',
	task_id int,
    foreign key (task_id) references task(task_id)
);











