use python_db;

create table stooq(
	stooq_id int primary key auto_increment,
    title text not null,
	content longtext not null,
    date_added varchar(55) not null,
    status bool default 0
);