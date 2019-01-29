


-- 连接查询
select a.acct_no, a.acct_name, c.tel_no
from acct a, eshop.customers c     -- 未作条件关联得到笛卡尔积
where a.cust_no = c.cust_no; -- 连接条件




课堂练习 
grant select, insert, update, delete on bank.*
to 'Jerry'@'%'
identified by '123456'

 jerry 下看                          show grants; 查看Jerry的权限
root 下看tom的权限                   show grants for 'Tom'@'localhost';















