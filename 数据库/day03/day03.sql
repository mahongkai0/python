




















-- 非空
create table custtomer(
    cust_no varchar(32) not null,
    cust_name varchar(128) not null,
    tel_no varchar(32) not null
)default charset=utf8;

insert into custtomer(cust_no,cust_name)
values('C0001','Jerry');



-- 唯一约束示例
create table custtomer(
    cust_no varchar(32) unique, -- 唯一约束
    cust_name varchar(128) not null,
    tel_no varchar(32) not null
)default charset=utf8;

-- 插入重复数据 违反唯一性约束
insert into custtomer
values('C0001','Jerry', '1351245678');
insert into custtomer values
('C0001','Jerry', '1351245678')



-- 主键约束

create table custtomer(
    cust_no varchar(32) primary key, -- 主键约束 
    cust_name varchar(128) not null,
    tel_no varchar(32) not null
)default charset=utf8;


insert into custtomer
values(null,'Jerry', '1351245678'); -- 违反非空
insert into custtomer values -- 违反唯一
('C0001','Jerry', '1351245678')

-- 外键
create table account(
    acct_no varchar(32) primary key,
    cust_no values(32) not null,
    -- 在当前表的cust_no上添加外键约束参照customer表中的cust_no字段
    constraint foreign key(cust_no),
    references custtomer(cust_no) 
);
-- 插入customer表中存在的客户
-- 参照完整性正确 可以插入
insert into account values('0001', 'C0001');


-- c0004不存在 参照完整性错误  插入时保存
insert into account values('0002', 'C0004');


-- 删除被参照的值 也会报错
delete from custtomer where cust_no = 'C0001';

 示例1：创建账号交易明细表 并在交易流水号上创建唯一索引
        
-- 账户交易明细表 在交易流水号上创建唯一索引        
create table acct_trans_detail(
    trans_sn varchar(32) not null, -- 交易流水号
    trans_date datetime not null,   -- 交易时间
    acct_no varchar(32) not null, -- 交易账号
    trans_type int, -- 交易类型
                    -- 存款 取款 刷卡 结息
    amt decimal(16,2) not null,
    unique(trans_sn), -- 在trans_sn上创建唯一索引
    index(trans_date) -- 在trans_date上建立普通索引
);                              

-- 查看索引
show index from acct_trans_detail;

-- 插入数据
insert into acct_trans_detail values(
    '201801010001', now(), '622345000001', 1, 1000
);
-- 查询时使用索引字段作为条件 条件就会使用到索引 俗称 踩在索引上
select * from acct_trans_detail where trans_sn = '201801010001';

    -- 删除索引
drop index 索引名称 on 表名
drop index trans_date on acct_trans_detail;


-- 添加索引
create index trans_date on acct_trans_detail(trans_date);
    -- alter table acct_trans_detail add unique index trans_sn(trans_sn);




-- daochu 
select * from acct
into outfile '一捆路径'
fields terminated by ',' -- 指定字段分割符 
lines terminated by '\n'; -- 指定行分割符


-- 查看
sudo cat '一捆路径'


-- 导入
load data infile '一捆路径'
into tables acct
fields terminated by ','    -- 指定字段分割符 
lines terminated by '\n';   -- 指定行分割符




课堂练习
1.修改orders表结构
    1）在order_id上添加主键约束
        --- alter table orders modify order_id varchar(32) primary key;
        alter table orders add primary key(order_id);
    2）在cust_id,order_date,products_num字段上
        添加非空约束
        alter table orders modify cust_id varchar(32) not null;
        alter table orders modify order_date datetime not null;
        alter table orders modify products_num int not null;
    3）在status 字段上添加默认值 默认值为1
    alter table orders modify status enum('1', '2', '3', '4', '5', '6', '9') default 1;
    
    4）在order_date上添加普通索引
    create index order_date on orders(order_date); (idx_order_date)

2.创建客户信息表 customers包含字段有
cust_id 客户编号，字符串 32 主键
cust_tel 客户电话 字符串 32 非空
cust_name 客户姓名 字符串 64 非空
address 送货地址 字符串 128 非空

create table customers(
    cust_id varchar(32) primary key,
    cust_tel varchar(32) not null,
    cust_name varchar(64) not null,
    address varchar(128) not null
) default charset=utf8;


3.为customers表添加数据  要求每个orders表中的cust_id 都有对应的客户信息

    

insert into customers values(
    '001', '15813313189', '张三', '开封'
),
(
    '004', '15813313158', '叶良辰', '上海'
),
(
    '005', '15813313145', '李青', '广州'
),
(
    '006', '15813313199', '张学友', '深圳'
),
(
    '007', '15813313122', '刘德华', '汕头'
),
(
    '008', '15818422323', '孙中山', '陕西'
);


4.在order 表中的cust_id上创建外键约束
参照customers 表中的cust_id字段

alter table orders add constraint foreign key(cust_id)
references customers(cust_id);





























