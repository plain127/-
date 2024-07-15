# 날 데려 가시개

## 유기반려견 입양가능성 판별 분류기

## Project

![detection](https://github.com/user-attachments/assets/1dbe9c9b-50dc-407b-9904-f43659638f55)

## Purpose

- 머신러닝 Classification을 이용하여 보호소에서 보호종료된 반려견들의 데이터들을 가지고 입양과 미입양된 반려견들의 사례를 학습시켜 입양 가능성을 높이기 위해 필요한 피처의 상관관계를 추론해본다.

## Model

### XGBoost Classifier

### Pre-Trained Model

[Checkpoint](https://drive.google.com/file/d/1-8JBnXVFP4lwa0cpHpZA96AeOvFS3hd6/view?usp=drive_link)

```
Assets/
├─ ...
├─ StreamingAssets/
│  └─ ML/
│     ├─ data/
|     |   └─ dogs_encoder_data.csv
│     ├─ model/
|     |   └─ dog_adopt_classifier.model
│     └─ run.py
└─ ...
```

## Dataset

- Feature Data : '품종', '색', '성별', '중성화유무', '나이', '지역', '크기'
- Label Data : '상태'
- 전체 43,010 데이터

## EDA

- '품종'
  믹스견, 푸들, 말티즈, 포메라니안, 진도견, 비숑 프리제, 시츄, 치와와, 시바, 기타품종견
- '색'
  백, 흑, 갈, 회, 기타
- '성별'
  '미상' 제거
- 나이
  1년 이하 : '유년'
  1 ~ 7년 이하 : '성년'
  7년 초과 : '노년'
- 지역
  수도권 : 서울, 인천, 경기
  호서 : 충남, 충북, 대전, 세종
  호남 : 전북, 전남, 광주
  영남 : 대구, 경남, 경북, 부산, 울산
  관동 : 강원
  제주 : 제주
- 무게
  0~6kg : '소형'
  6~14kg : '중형'
  14kg~ : '대형'
- 상태
  방사, 반환 결측치 처리
  입양 (입양, 기증)
  미입양 (자연사, 안락사)

## Preprocessing

- Label Encoding

## Train

- classifier_train.ipynb

## UI/UX Client

- Unity UI
- python connect to unity

```
Assets/
├─ ...
├─ Scripts/
│  └─ Classification.cs
└─ ...
```
