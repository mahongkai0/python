
update acct 
set balance = balance + 10000
where acct_no = '622345000001';



练习：编写注销账号的SQL语句（修改状态 余额为0）

update acct
    set status = 4,
        balance = 0
where acct_no = '6223455000003';




create database eshop default charset=utf8

create table orders(
    order_id varchar(32),
    cust_id varchar(32),
    order_date DateTime,
    status enum('1', '2', '3', '4', '5', '6', '9'),
    products_num int,
    amt decimal(16,2)
)default charset=utf8;

insert into orders
values('001', '001', now(), '1',
        3, 650   
),
('002', '002', now(), '3',
        14, 163 
),
('003', '003', now(), '9',
        81, 985 
),
('004', '004', now(), '5',
        17, 416 
),
('005', '005', now(), '4',
        1, 9 
),
('006', '006', now(), '4',
        3, 1561 
),
('007', '007', now(), '6',
        42,98  
),
('008', '008', now(), '2',
        6,26  
),
('009', '005', now(), '3',
        13,64  
);

-- 查找所有代付款订单
select * from orders where status = '1';

-- 查找所有已发货、已收货 申请退货订单
select * from orders where status in('3', '4', '5');

-- 查找某个客户的代发货订单
select * from orders where order_id = '008' and status = '2'; -- 008随意

-- 根据订单编号 查找订单下单日期 订单状态
select order_date, status from orders where order_id = '005'; -- 005随意

--select order_date, status from orders order by order_id;

--select order_date, status from orders where order_id;


-- 查找某个客户所有订单 并按照下单时间倒序排列;'

select * from orders where cust_id = '005' order by order_date desc;-- 005随意

select status,count(*) from orders group by status;

select sum(amt),max(amt) from orders;

select * from orders order by amt desc limit 3;

alter table orders add invoice int;


alter table orders add invoice_date DateTime after invoice;
    -- alter table orders add invoice_date DateTime;
    -- alter table orders drop invoice_date;
update orders set status = '4' where order_id = '001';

delete from orders where status = '9';













































