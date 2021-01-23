# naver_news_crawler

## Notes
- 네이버 뉴스를 크롤링 하는 코드

- 안티크롤링 해결 및 기사내용 전처리 추가

- CSV 형태로 수집된 파일 도출
## How to use
- 제목 및 기사의 원본 수집
  ~~~
  python main.py
  ~~~
- 전처리된 제목 및 기사 수집
  ~~~
  python main.py --clean
  ~~~
## Results
- 검색 조건 입력

  ![ex_screenshot](./img/cmd_.PNG)
  
- 크롤링 결과

  ~~~
  python main.py
  ~~~    
  
  ![ex_screenshot](./img/csv1.PNG)
  
  ~~~
  python main.py --clean
  ~~~    
  
  ![ex_screenshot](./img/csv2.PNG)
  
## reference
- https://bumcrush.tistory.com/155
- https://data-newbie.tistory.com/210
- https://book.coalastudy.com/data_crawling/week3/stage3
