
import urllib.request

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        respone = urllib.request.urlopen(url)

        if respone.getcode() != 200:
            return None

        return respone.read()