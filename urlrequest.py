import urllib

def request(url):
	connection = urllib.urlopen(url)
	content_of_url = connection.read()
	connection.close()
	print(content_of_url)


request("http://mengxiangjian.com")