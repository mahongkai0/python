import re
import sys


def code_o(port):

##########################遍历 遇到换行打断 分成一段一段 开始正则开头的单词 如果不是继续走 是的话 正则你需要用的东西
    #提取一段内容
    f = open("c:/Users/Administrator/Desktop/test/正则开始/day02/1.txt")
    # data = f.read().decode()
    while True:
        data =''
        for line in f:
            if line != '\n':
                data += line
               
            else:
                break
        
        #经过一段时间累加已经到了文件的结尾
        if not data:
            return "Not Found"
      

        #匹配手单词 查看是否为目标段落
        try:
            PORT = re.match(r'\S+',data).group()
        except Exception as e:
            print(e)
            continue

        if PORT == port:    ###)
            patten =r"address is ([0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4})"
            address = re.search(patten,data).group()
            
            # patten =r"address is ((\d{1,3}\.){3}\d{1,3}/\d+|Unknow)"
            # address = re.search(patten,data).group(1)
            return address


if __name__ == "__main__":
    port = sys.argv[1]
    addr = code_o(port)
    print(addr)










