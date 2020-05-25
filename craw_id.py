from urllib.request import urlopen
import csv
import re
from bs4 import BeautifulSoup
import requests
import pandas as pd

def crawl_id():
    # define url for crawling
    url = 'https://en.wikipedia.org/wiki/Main_Page'
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

    # newline='' 參數，這是為了讓資料中包含的換行字元可以正確被解析
    with open ('ID_reference_.csv','r',newline='') as csvfile:
        # 讀取 CSV 檔案內容
        # reader = csv.reader(csvfile)
        reader = csv.DictReader(csvfile)
        column = [row['mlb_name'] for row in reader]

        for name in column:
            a = name.replace('.', '._')
            input_keyword=a.replace(' ','_')
            keyword_link = "https://en.wikipedia.org/wiki/"+input_keyword
            # print(keyword_link)
            res = requests.get(keyword_link, headers=headers)
            soup = BeautifulSoup(res.text, 'html.parser')
            # content = soup.find(name='div', attrs={'id':'mw-content-text'}).find_all(name='a')
            # print(content)

            # html = urlopen("https://en.wikipedia.org/wiki/"+input_keyword)
            # soup = BeautifulSoup(keyword_link,'html.parser')
            # 以"/wiki/"开始
            # (?!)是不包含:的意思
            regex = re.compile(r"^(https:\/\/twitter\.com\/)((?!:).)*$")
            for link in soup.find('div', {'id': 'mw-content-text'}).find_all('a', href=regex):
                if 'href' in link.attrs:
                    screen_name_str=link.attrs['href'].split('/')[-1]
                    print(name,screen_name_str)


            # with open('screen_name.csv', 'w') as f:
            #     writer = csv.writer(f)
            #     table=[column,screen_name_str]
            #     writer.writerow(['mlb_name',"screen_name"])
            #     writer.writerows(table)
            #     df_tweet = pd.DataFrame(table,columns=['mlb_name',"screen_name"])
            #     # 顯示所有列
            #     pd.set_option('display.max_columns', None)
            #     # 顯示所有行
            #     pd.set_option('display.max_rows', None)
            #     # 設置顯示的寬度為2000，防止輸出內容被換行
            #     pd.set_option('display.width', 2000)
            #     print(df_tweet.head())
            #             # for row in screen_name_str:
            #             #     writer.writerows(row)

        return 'screen_name'




crawl_id()