
from bs4 import BeautifulSoup
import re
import urllib.parse

class HtmlParser(object):

    def _is_chinese(unchar):
        if unchar >= u'\u2E80' and uchar <=  u'\uFE4F':
            return true;
        else:
            return false;

    def _data_process(data):
        result = str()
        for c in data:
            if self._is_chinese(c):
                c = urllib.parse.quote(c)
            result += c;
        return result;

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/view/\d+\.htm"))
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}
        str_data = ""
        res_data['url'] = page_url
        title_node = soup.find('dd', class_ = "lemmaWgt-lemmaTitle-title").find("h1")

        #if(len(title_node)):
        res_data['title'] = title_node.get_text()

        summary_node = soup.find('div', class_="lemma-summary")
        
        #if(len(summary_node)):
        res_data['summary'] = summary_node.get_text()


        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return 'No module named urlparse'

        data = html_cont.decode("utf-8")
        soup = BeautifulSoup(data, "html.parser")
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data