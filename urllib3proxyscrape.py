import urllib3
from lxml import html

user_agent_header = urllib3.make_headers(user_agent="<USER AGENT>")
pool = urllib3.ProxyManager(f'<PROXY IP>', headers=user_agent_header)
r = pool.request('GET', 'https://www.google.com/')

# Re-use response from urllib3
data_string = r.data.decode('utf-8', errors='ignore')

# Instantiate tree object from HTML
tree = html.fromstring(data_string)

# run Xpath against this html
# returns array of element
links = tree.xpath('//a')

for link in links:
    # for each element we can easily get back the URL
    print(link.get('href'))
