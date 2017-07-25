import os
import time
import webbrowser

current_dir = os.getcwd()
print(current_dir)

def listAllFile():
	all_files = os.listdir(current_dir)
	print(all_files)

# os.rename() rename file

def openWebbrowser(url):
	webbrowser.open(url)

listAllFile()

time.sleep(3)
openWebbrowser("https://www.baidu.com")

