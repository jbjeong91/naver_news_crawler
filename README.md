# naver_news_crawler

## Notes
- BeautifulSoup을 활용한 네이버 뉴스 크롤링

- 안티크롤링 해결 및 기사내용 전처리 추가

- CSV(utf-8) 형태로 수집된 파일 도출
## How to use
- 제목 및 기사의 원본 수집
  ~~~
  python main.py
  ~~~
- 정제된 제목 및 기사 수집
  ~~~
  python main.py --clean
  ~~~
## Results
- 검색 조건 입력

  ![ex_screenshot](./img/cmd_new.PNG)
  
- 크롤링 결과

  ~~~
  python main.py
  ~~~    
  
  ![ex_screenshot](./img/csv1_new.PNG)
  
  ~~~
  python main.py --clean
  ~~~    
  
  ![ex_screenshot](./img/csv2_new.PNG)
  
## reference
- https://bumcrush.tistory.com/155
- https://data-newbie.tistory.com/210
- https://book.coalastudy.com/data_crawling/week3/stage3
- csv(utf-8) 파일 excel로 열기
  https://www.lesstif.com/life/ms-excel-utf-8-csv-54952504.html
