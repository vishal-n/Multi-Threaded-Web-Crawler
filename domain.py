from urllib.parse import urlparse

# Get sub-domain name (name.example.com)
def get_sub_domain_name(url):
	try:
		return urlparse(url).netloc
	except:
		return ''

#print(get_sub_domain_name("https://www.google.com/"))
#print(get_sub_domain_name("https://github.com/buckyroberts/Spider/blob/master/domain.py"))
#print(get_sub_domain_name("https://www.youtube.com/watch?v=XjNm9bazxn8"))


# Get domain name
def get_domain_name(url):
	try:
		results = get_sub_domain_name(url).split('.')
		return results[-2] + '.' + results[-1]
	except:
		return ''

#print(get_domain_name("https://www.youtube.com/watch?v=XjNm9bazxn8"))
#print(get_domain_name("https://www.google.com/"))
#print(get_sub_domain_name("https://github.com/buckyroberts/Spider/blob/master/domain.py"))