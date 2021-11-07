# 졸업 프로젝트 JUMO 추천작업을 위한 API 서버 프로젝트입니다.

<img src="https://img.shields.io/badge/python3-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"> <img src="https://img.shields.io/badge/flask-000000?style=for-the-badge&logo=flask&logoColor=white"> <img src="https://img.shields.io/badge/beautifulsoup-11303d?style=for-the-badge&logo=beautifulsoup&logoColor=white">

# API

### 실시간 주가 가져오기
네이버 증권에서 크롤링하여 실시간 주가 제공

GET /predict/MACD
```json
res
{
  "time" : "(time)",
  "price" : "(number)"
}
```
### 요청 종목의 전체 기록과 해당 날짜에 대한 추천 여부 리스트
pandas ewm 이용하여 이동평균선 계산 후, macd 값 계산

GET /predict/MACD
```json
res
{
  "0": {
        "code": "005930.KS",
        "name": "삼성전자",
        "time": "2017-01-02T00:00:00.000Z",
        "Close": 36100,
        "year": 2017,
        "month": 1,
        "day": 2,
        "macd": 0.0,
        "signalLine": 0.0,
        "isLongTermFullmaesu": "STAY",
        "isShortTermFullmaesu": "STAY"
    },
    "1": {
        "code": "005930.KS",
        "name": "삼성전자",
        "time": "2017-01-03T00:00:00.000Z",
        "Close": 36480,
        "year": 2017,
        "month": 1,
        "day": 3,
        "macd": 30.3133903134,
        "signalLine": 6.0626780627,
        "isLongTermFullmaesu": "BUY",
        "isShortTermFullmaesu": "BUY"
    },
    ...
}
```
### 요청 종목의 현재 추천여부
가장 최신 순으로 타임 윈도우 사이즈 안의 기록들을 macd 지표로 하여 추천 계산
GET /predict/MACD
```json
res
{
    "code": "005930.KS",
    "name": "삼성전자",
    "time": "2021-10-21T00:00:00.000Z",
    "Close": 70400,
    "year": 2021,
    "month": 10,
    "day": 21,
    "macd": -1634.4106484813,
    "signalLine": -1572.6266366414,
    "isLongTermFullmaesu": "SELL",
    "isShortTermFullmaesu": "SELL"
}
```
