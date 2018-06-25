import os
import requests
import time

def requestAppHome():
	url = "http://test2.m.letv.com/android/dynamic.php?mod=mob&ctl=home55&act=index&isnew=0&devid=370B3ADA-C840-4B4B-87A4-83C30736079A&history=30068478-27886856-30507638-30505783-30222341-27736008-27840450-29119550-27537975-2067499&allow_risk_album=true&country=CN&provinceid=1&districtid=9&citylevel=1&location=北京市|朝阳区&pcode=010210000&version=7.11&lang=chs&region=CN"
	try:
		s = requests.get(url)
		dname = "contemt"
		d = os.path.join("",dname)
		if os.path.exists(d) == False :
			os.mkdir(d)

		f = open(os.path.join(dname, "apphome.txt"), "wb")
		sb = s.content
		f.write(sb)
		f.close()
	except Exception as e:
		print("fetch last activities fail. " + url)
		raise e


for i in range(1,11):
	requestAppHome()
	print(("这是第%d次请求" % i))
	time.sleep(5)