def read():
	file_instance = open("./textresource.txt")
	content_of_file = file_instance.read()
	print(content_of_file)
	file_instance.close()


read()