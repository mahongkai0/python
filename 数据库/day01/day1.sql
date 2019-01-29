
--day01.sql
--mysql 第一天的sqk语句

--创建表acct（账户）

create table acct(
    acct_no varchar(32),
    acct_name varchar(128)
) default charset=utf8;


--删除
drop table acct;
--重新创建acct
create table acct(
    acct_no varchar(32),-- 账号,字符串,32 字节
    acct_name varchar(128),-- 户名 ，128字节
    cust_no varchar(32),-- 客户编号
    acct_type int,-- 账户类型 整数型
    reg_date date,-- 日期类型
    status int, -- 账户状态，整数形
    balance decimal(16,2) -- 最长16位，2位小数
) default charset=utf8;


* 需要注意的地方：
  语句中除了注释以外  不能出现中文字符
  括号必须匹配 并且嵌套要正确，最好成对的书写
  date 日期类型  容易携程data
  注意其他的拼写错误
  最后一个分号不要忘记写 
  注释的两个横线必须加空格

-- 插入
insert into acct 
values('622345000001', 'Jerry', 'C0001',
        1, now(), 1, 1000.00
);

-- 查询 
select * from acct

-- 插入多笔数据
insert into acct values
('622345000002', 'Tom', 'C002', 1, now(), 1, 2000.0),
('622345000003', 'Ben', 'C003', 1, now(), 1, 3000.0),
('622345000004', 'ken', 'C004', 1, now(), 1, 4000.0);

-- 指定字段插入
insert into acct(acct_no,acct_name)
values('622345000005', 'may');


-- 指定字段查询
select acct_no, acct_name, balance from acct;

-- 查询指定字段 并且为字段指定别名
select acct_no "账号" , -- 双引号之间为别名 中间还可以加as
       acct_name "户名",
       balance "余额"
from acct; 
-- 或者
select acct_name as "账号" from acct;


-- 条件时计算
select acct_no "账号" , -- 双引号之间为别名 中间还可以加as
       acct_name "户名",
       balance/10000 "余额(万元)"
from acct; 


-- 带条件查询
select * from acct
where acct_no = '622345000001';

-- 带两个个条件查询  两个条件同时满足
select * from acct
where acct_name = 'Jerry' and acct_no = '622345000001';

-- 带两个条件满足一个
select acct_name,acct_no,balance from acct
where acct_name = 'Jerry' or acct_no = '622345000004';

select * from acct
where acct_name = 'Jerry' or acct_name = 'Ben';

-- char和varchar类型示例
create table tmp(
    acct_no char(10),
    acct_name varchar(35)
);
insert into tmp values('0001', 'Jerry');


-- enumerate， set 类型
create table enum_test(
    name varchar(32),
    sex enum('boy','girl'),-- 从两这选一
    course set('music', 'dance', 'paint')
);
-- 在枚举范围内可以插入
insert into enum_test values(
    'Jerry', 'girl', 'music,dance');
-- 在枚举范围之外插入报错  football不在范围内
insert into enum_test values(
    'Jerry', 'girl', 'music,football'
);














