import re
import requests
from bs4 import BeautifulSoup


url = "http://www.qiushibaike.com/text/page/1/"
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) "
                             "Chrome/22.0.1207.1 Safari/537.1"}
def withBs():
    """ 使用 BeautifulSoup 解析 """
    r = requests.get(url, headers=headers).text
    try:
        authors = BeautifulSoup(r, 'lxml').find_all('h2')
        contents = BeautifulSoup(r, 'lxml').find_all('div', class_='content')
        votes = BeautifulSoup(r, 'lxml').find_all('span', class_='stats-vote')
    except Exception as e:
        print(e)
    else:
        for i, value in enumerate(authors):
            author = value.get_text()  # 作者
            vote = votes[i].get_text().split(" ")[0]  # 点赞数
            content = contents[i].get_text()  # 段子正文
            result = "\n>> author: {}\n   vote: {}\n   content: {}".format(author, vote, content.lstrip())
            print(result)

    def withRe(self):
        """ 使用正则表达式解析 """
        r = requests.get(url, headers=headers).text
        authors = re.findall(r'<h2>(.*?)</h2>', r)
        votes = re.findall(r'"stats-vote"><i class="number">(\d*)</i>', r)
        contents = [c.replace("<br/>", "") for c in
                    re.findall(r"contentHerf' >\n<div class=\"content\">\s+<span>([\S ]+[\n\S]*)</span>", r)]
        for i, value in enumerate(authors):
            result = "\n>> author: {}\n   vote: {}\n   content: {}".format(value, votes[i], contents[i].lstrip())
            print(result)

if __name__ == "__main__":
   withBs()