# ⚽ Ballzzi - 축구 선수 & 회사 정보 통합 챗봇
## 👥 팀 소개

<table>
  <tr>
    <td align="center">
      <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQQsaj4eUsVLHnn85Em20Eu8YtTtMBRkfdPaw&s" width="120px"><br/>
      <b>김도윤</b>
    </td>
    <td align="center">
      <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0ThDAyobh6HspAwP91xEkg6_-XSo4ylRPCg&s" width="120px"><br/>
      <b>최요섭</b>
    </td>
    <td align="center">
      <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTw-qEBHjbTHF8n3Nn2KVZllOSGS2-z4jYa_g&s" width="120px"><br/>
      <b>김재현</b>
    </td>
    <td align="center">
      <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTB4gKOx2vxnDDrLDNDAsHzx-rzc_l0ZeO-tA&s" width="120px"><br/>
      <b>이석원</b>
    </td>
    <td align="center">
      <img src="https://mblogthumb-phinf.pstatic.net/MjAyMjExMTZfMTQz/MDAxNjY4NjAxNTQzNDYw.dZzc1TIxWmITM_5uildryLFGXFwgjx0ahbrf9DXCEZ0g.xTwwfY8Je-4zuVM3FbIm2WDtEY0b9YSimgX4RM6MCsEg.JPEG.gngnt2002/%EF%BB%BF%EC%9A%B0%EB%8A%94_%EA%B3%A0%EC%96%91%EC%9D%B4_%EC%A7%A4_%EB%AA%A8%EC%9D%8C_(4).jpg?type=w800" width="120px"><br/>
      <b>윤권</b>
    </td>
  </tr>
</table>

---

<div align="center"><h1>📚 STACKS</h1></div>

<div align="center"> 
  <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> 
  <img src="https://img.shields.io/badge/streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"> 
  <img src="https://img.shields.io/badge/sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white"> 
  <img src="https://img.shields.io/badge/faiss-0099CC?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjMDA5OUM4IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciLz4=&logoColor=white" alt="faiss"> 
  <img src="https://img.shields.io/badge/openai-412991?style=for-the-badge&logo=openai&logoColor=white"> 
  <img src="https://img.shields.io/badge/langchain-4BAF50?style=for-the-badge"> 
  <img src="https://img.shields.io/badge/huggingface-FFD21F?style=for-the-badge&logo=huggingface&logoColor=black">
  <br>
  <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white"> 
  <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white">
</div>


## 📋 프로젝트 개요

Ballzzi은 축구 선수 정보와 회사 내부 정보를 모두 처리할 수 있는 통합 챗봇 시스템입니다. 질문 라우팅을 통해 축구 관련 질문은 FM(Football Manager) 모듈로, 회사 관련 질문은 HR 모듈로 자동 분류하여 처리합니다.

## 🏗️ 시스템 아키텍처

![image](https://github.com/user-attachments/assets/c902a87e-b68c-46b0-b1ec-50e5dfec27dd)


## 🚀 주요 기능

### 1. 질문 자동 분류 (Question Routing)
- **모델**: `sentence-transformers/all-MiniLM-L6-v2`
- **기술**: FAISS 기반 벡터 유사도 검색
- **분류**: 'soccer' (축구 관련) / 'company' (회사 관련)

### 2. FM 모듈 (축구 선수 정보)
- **자연어 → SQL 변환**: GPT-4o-mini 모델 사용
- **데이터베이스**: SQLite (players_position.db)
- **이미지 검색**: Bing 이미지 크롤링 (Selenium)
- **응답 형식**: JSON 배열로 구조화된 선수 정보

### 3. HR 모듈 (회사 정보)
- **RAG 시스템**: FAISS 벡터 데이터베이스 활용
- **다중 검색 도구**: 
  - 통합 검색 (내부+외부)
  - 회사 전용 검색
  - 네이버 뉴스/웹 검색
  - 퇴직금 계산기
- **LLM 지원**: OpenAI GPT 및 HyperCLOVAX

## 📁 디렉토리 구조

```
AJR/
├── app.py                          # 메인 Streamlit 애플리케이션
├── question_Routing.py             # 질문 분류 시스템
├── requirements.txt                # Python 패키지 의존성
│  
├── FM/                           # Football Manager 모듈
│   ├── FM_GetData_LLM.py         # 메인 축구 정보 처리
│   ├── tools/
│   │   ├── create_prompt.py      # SQL/자연어 프롬프트 생성
│   │   ├── SQL_create.py         # SQL 쿼리 생성 체인
│   │   ├── SQL_execute.py        # SQL 실행 체인
│   │   └── image_craper.py       # Bing 이미지 크롤링
│   ├── data/
│   │   ├── players_position.db   # 축구 선수 데이터베이스 (788KB)
│   │   └── training_dataset.jsonl # 학습 데이터셋 (14MB)
│   ├── code/                     # 추가 코드
│   └── finetuning/               # 파인튜닝 관련
│
└── HR/                           # Human Resources 모듈
    ├── agents/
    │   └── agent_executor.py     # Langchain Agent 실행기
    ├── tools/
    │   └── rag_tool.py          # RAG 도구 모음  
    └── data/
        ├── faiss_win/           # 사내 규정 FAISS 인덱스
        └── faiss_org_hr/        # 인사 구조 FAISS 인덱스
 
 
```

## 🔧 사용 기술 스택

### 머신러닝 & AI
- **Lang일
