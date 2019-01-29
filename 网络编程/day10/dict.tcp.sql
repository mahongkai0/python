



create database dict_tcp default charset = utf8

create table user(
    dict_id int primary key auto_increment,
    dict_name  varchar(32) not null,
    password varchar(16) default '000000' );
-- 数据库四大类型  数字 事件 枚举 字符串
create table hist(
    dict_id int primary key auto_increment,
    dict_name varchar(32) not null,
    word varchar(32) not null,
    time varchar(64)
);

create table words(
    dict_id int primary key auto_increment,
    word varchar(32),
    interpret text
);


























