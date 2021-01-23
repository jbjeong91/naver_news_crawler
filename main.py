# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import csv

RESULT_PATH = './'

def get_news(n_url):
    news_detail = []

    # 안티크롤링 우회를 위한 추가 headers={'User-Agent':'Mozilla/5.0'}
    breq = requests.get(n_url, headers={'User-Agent':'Mozilla/5.0'})
    bsoup = BeautifulSoup(breq.content, 'html.parser')

    # 기사 제목
    title = bsoup.select('h3#articleTitle')[0].text  # 대괄호는  h3#articleTitle 인 것중 첫번째 그룹만 가져오겠다.
    news_detail.append(title)

    pdate = bsoup.select('.t11')[0].get_text()[:11]
    news_detail.append(pdate)

    # 기사 내용
    _text = bsoup.select('#articleBodyContents')[0].text.replace('\n', " ")
    #-------------------------------------
    img_desc = bsoup.select('.img_desc')
    for des in img_desc:
        _text = _text.replace(des.text,"")
    #-------------------------------------
    btext = _text.replace("// flash 오류를 우회하기 위한 함수 추가 function _flash_removeCallback() {}", "")
    news_detail.append(btext.strip())
    news_detail.append(n_url)
    pcompany = bsoup.select('#footer address')[0].a.get_text()
    news_detail.append(pcompany)

    return news_detail


def crawler(maxpage, query, s_date, e_date):
    s_from = s_date.replace(".", "")
    e_to = e_date.replace(".", "")
    page = 1
    maxpage_t = (int(maxpage) - 1) * 10 + 1  # 11= 2페이지 21=3페이지 31=4페이지  ...81=9페이지 , 91=10페이지, 101=11페이지
    f = open("./contents_text.csv", 'w', newline='')
    w = csv.writer(f)
    w.writerow(['years', 'company', 'title', 'contents', 'link'])

    while page < maxpage_t:
        print('page_num:',page)
        url = "https://search.naver.com/search.naver?where=news&query=" + query + "&sort=0&ds=" + s_date + "&de=" + e_date + "&nso=so%3Ar%2Cp%3Afrom" + s_from + "to" + e_to + "%2Ca%3A&start=" + str(
            page)

        req = requests.get(url)
        cont = req.content
        soup = BeautifulSoup(cont, 'html.parser')

        #for urls in soup.select("a._sp_each_url"):
        for urls in soup.select('.info_group > a'):
            if urls["href"].startswith("https://news.naver.com"):
                try:
                    news_detail = get_news(urls["href"])
                    w.writerow([news_detail[1], news_detail[4], news_detail[0], news_detail[2],news_detail[3]])  # new style
                except Exception as e:
                    print(e)
                    continue
        page += 10

    f.close()


def main():
    maxpage = input("검색 최대 출력 페이지수: ")
    query = input("검색어: ")
    s_date = input("시작날짜[2021.01.01]:")
    e_date = input("끝날짜[2021.01.23]:")
    crawler(maxpage, query, s_date, e_date)

main()
