# naverBlogToMarkdown
네이버 블로그를 자동적으로 마크다운 형식으로 변환해주는 파이썬 기반 프로그램입니다.

## 의존성 설치
```shell
pip install selenium
pip install requests
```
크롬버전 74용입니다. 자신에게 맞는 크롬드라이버를 설치해야 합니다. 

## 오류발생시 확인 할 목록
자신이 사용하고 있는 크롬버전에 맞는 chromedriver를 설치하는 것이 중요하다.  
<p align="center"> 
  <img src="https://raw.githubusercontent.com/wnghdcjfe/naverBlogToMarkdown/master/img/a.png" width="700">
</p> 

<p align="center"> 
  <img src="https://raw.githubusercontent.com/wnghdcjfe/naverBlogToMarkdown/master/img/b.gif" width="700">
</p> 

## 실행방법
 - 테스트 : server안에 있는 dist폴더의 index.html을 수정해가며 스크래핑을 테스트할 수 있다. 
 - 스크래핑 항목 : test > test.py를 수정하면 된다. 

## 해야할 사항들
 - [x] 순차적 스크래핑
 - [ ] 웹앱으로 제작
 - [ ] 블로그 자체적 모든 md파일 스크래핑
 - [ ] 블로그 카테고리 별로

## 공지
스타개수 10개 넘어가면 제대로 UX개선해서 만들어 보겠습니다.
