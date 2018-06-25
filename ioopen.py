import io

f = io.open("1.doc",'r',encoding="gbk")
c = f.read()
f.close()
print(c)
