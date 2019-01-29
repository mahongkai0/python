




# show variables like 'secure_file%'

# C:\Users\Administrator\Documents\Tencent Files\2435086463\FileRecv\dict


# load data infile 'C:\Users\Administrator\Documents\Tencent Files\2435086463\FileRecv\dict'
# into table words
# fields terminated by ' '
# lines terminated by ' '


import pymysql

f = open('c:/Users/Administrator/Desktop/test/网络编程/day10/dict.txt')
db = pymysql.connect('localhost','root','123456','dict_tcp')


cursor = db.cursor()  #创建游标
for line in f:
    tmp = line.split(' ')
    word = tmp[0]
    interpret = ' '.join(tmp[1:]).strip()
    # print(word)
    # print(interpret)

    sql = '''insert into words (word,interpret)
        values ("%s","%s")'''% (word,interpret)
       
    try:
        cursor.execute(sql)
        db.commit()
    except Exception:
        db.rollback()
        
f.close()













