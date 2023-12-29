
#encoding: utf-8
from bs4 import BeautifulSoup

html_doc = """<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <script type= "text/javascript" src="xxxx.js"></script>                                
        <link href="xxx.css" rel="stylesheet" type="text/css" />                                
        <title>index.html</title>
    </head>
    <body>
        <p class="title1">The Dormouse's story1</b></p>
        <p class="title2">The Dormouse's story2</b></p>
    </body>
    </html>"""

soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')

print u"获取所有的链接"
links = soup.find_all('p');
for link in links:
    print link.name, link.get_text()

print u"获得带有指定字符串的连接"
link_node = soup.find('p', class_= "title2")
print link_node.name, link_node.get_text()