import urllib2


respone = urllib2.urlopen("http://baike.baidu.com/view/21087.htm")

if respone.getcode() == 200:
    print respone.read()