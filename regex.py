import re

html_content = '<p>Price : 19.99$</p>'

m = re.match('<p>(.+)<\/p>', html_content)
if m:
    print(m.group(1))
