from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

# 라벨 정의
examples = [
    ("연차는 어떻게 써요?", "other"),
    ("복지 포인트는 어디서 확인해?", "other"),
    ("퇴사하려면 뭐부터 해야 해?", "other"),
    ("출근 시간은 몇 시인가요?", "other"),
    ("재택근무 신청은 어디서 합니까?", "other"),
    ("회사 노트북 언제 반납해요?", "other"),
    ("연말 정산은 어떻게 처리하나요?", "other"),
    ("부서 이동은 누가 승인해?", "other"),
    ("상여금 지급일 좀 알려줘", "other"),
    ("점심시간 몇 시부터지?", "other"),
    ("야근수당 나와요?", "other"),
    ("복장은 자유복인가요?", "other"),
    ("입사 첫날은 몇 시까지 가야 해요?", "other"),
    ("중식비 지원 돼요?", "other"),
    ("복지몰 어디서 써?", "other"),
    ("연차는 몇 개 있어요?", "other"),
    ("정직원 전환 기준이 뭡니까?", "other"),
    ("지각하면 벌점 있어?", "other"),
    ("출산휴가는 얼마나 주나요?", "other"),
    ("월급날 언제야?", "other"),
    ("성과급은 누가 결정해?", "other"),
    ("회사 행사 일정은 어디서 봐?", "other"),
    ("계좌 변경 어떻게 하지?", "other"),
    ("직원 교육 필수인가요?", "other"),
    ("퇴사 후에 보험은 자동 정산돼요?", "other"),
    ("인사이동은 본인이 신청 가능한가요?", "other"),
    ("외근 시 식비도 나와?", "other"),
    ("오전 반차 쓰고 오후에 출근해도 되죠?", "other"),
    ("휴일 근무하면 대체휴무 주나요?", "other"),
    ("상사한테 직접 말 안 하고 연차 낼 수 있어요?", "other"),
    ("회식비는 누가 계산해요?", "other"),
    ("보안 교육은 어디서 받아요?", "other"),
    ("직원증 분실했는데 어떻게 해요?", "other"),
    ("출장비는 선지급이에요 후지급이에요?", "other"),
    ("회사 주소 변경됐어요?", "other"),
    ("근무지는 본사예요?", "other"),
    ("복지포인트는 언제 들어와요?", "other"),
    ("교육 이수 마감일 언제예요?", "other"),
    ("노트북 대여 연장 가능해요?", "other"),
    ("명함은 어디서 신청해요?", "other"),
    ("사내 메신저는 뭐 써요?", "other"),
    ("정장 입고 가야 하나요?", "other"),
    ("부서 이동하고 싶은데 절차가 어떻게 돼요?", "other"),
    ("성과평가는 누가 해요?", "other"),
    ("코로나로 재택 가능한가요?", "other"),
    ("상반기 보너스는 언제 나와요?", "other"),
    ("직원 건강검진은 언제예요?", "other"),
    ("입사 축하금 있나요?", "other"),
    ("근로계약서 어디서 확인해요?", "other"),
    ("퇴근 후 연락 오면 꼭 받아야 하나요?", "other"),
    ("사내 동호회 뭐 있어요?", "other"),
    ("육아휴직은 얼마나 쓸 수 있어요?", "other"),
    ("이직 시 추천서 써주시나요?", "other"),
    ("근태 기록 수정 가능해요?", "other"),
    ("사내식당 운영 시간 알려주세요.", "other"),
    ("정시 출근 안 하면 불이익 있나요?", "other"),
    ("초과근무 승인 방식이 궁금해요.", "other"),
    ("신입사원 교육은 몇 일이에요?", "other"),
    ("동료와 갈등 있으면 누구에게 말해야 해요?", "other"),
    ("노조 가입 가능한가요?", "other"),
    ("복직 절차가 어떻게 되나요?", "other"),
    ("퇴사 전에 인수인계 문서는 꼭 써야 해요?", "other"),
    
    ("손흥민은 어떤 선수야?", "soccer"),
    ("이강인 패스 능력 어때?", "soccer"),
    ("황희찬은 골결정력이 좋아?", "soccer"),
    ("수비 잘하는 미드필더 추천해줘", "soccer"),
    ("패스 정확도 높은 선수 누구야?", "soccer"),
    ("K리그에서 유망한 수비수는?", "soccer"),
    ("아스날 선수 중 유망주 알려줘", "soccer"),
    ("스피드 빠른 공격수 추천해줘", "soccer"),
    ("득점력 좋은 미드필더는 누구야?", "soccer"),
    ("벤제마와 호날두 중 누가 더 좋아?", "soccer"),
    ("최근에 성장세인 선수는?", "soccer"),
    ("드리블 좋은 선수 추천해줘", "soccer"),
    ("수비력 뛰어난 센터백 알려줘", "soccer"),
    ("공중볼 강한 선수는 누구야?", "soccer"),
    ("EPL에서 떠오르는 유망주 있어?", "soccer"),
    ("피지컬 좋은 공격수 추천해줘", "soccer"),
    ("이승우는 요즘 어떤 스타일이야?", "soccer"),
    ("김민재 수비 성능 분석해줘", "soccer"),
    ("기동력 좋은 윙백 누구 있어?", "soccer"),
    ("슛 정확도 높은 선수 알려줘", "soccer"),
    ("키 큰 수비수 추천해줘", "soccer"),
    ("골 결정력 좋은 스트라이커는?", "soccer"),
    ("정교한 킥 가진 선수 알려줘", "soccer"),
    ("박지성과 비슷한 스타일 누구야?", "soccer"),
    ("어린 선수 중에서 기대되는 선수는?", "soccer"),
    ("침투 잘하는 공격수 추천해줘", "soccer"),
    ("K리그에서 득점왕 후보는?", "soccer"),
    ("손흥민과 비교할 만한 선수 있어?", "soccer"),
    ("아시안게임에서 활약한 선수 추천", "soccer"),
    ("스피드와 체력 좋은 선수는?", "soccer"),
    ("세트피스에 강한 선수 알려줘", "soccer"),
    ("몸싸움 강한 수비수 추천해줘", "soccer"),
    ("왼발 잘 쓰는 공격수 있어?", "soccer"),
    ("기술 뛰어난 윙어 알려줘", "soccer"),
    ("1대1 수비에 강한 선수는 누구야?", "soccer"),
    ("멀티 포지션 가능한 선수 추천해줘", "soccer"),
    ("중거리슛 잘하는 선수 있어?", "soccer"),
    ("키퍼와 1대1에 강한 선수는?", "soccer"),
    ("유로 대회에서 주목받은 선수는?", "soccer"),
    ("챔피언스리그에서 활약한 신예는?", "soccer"),
    ("멘탈 좋은 선수는 누구야?", "soccer"),
    ("리더십 있는 주장감 선수 추천해줘", "soccer"),
    ("최근 몸값 오른 선수 있어?", "soccer"),
    ("U-20 대표팀에서 잘한 선수는?", "soccer"),
    ("드리블 돌파 잘하는 유망주 알려줘", "soccer"),
    ("유망한 한국 수비수 추천해줘", "soccer"),
    ("라리가 유망주 알려줘", "soccer"),
    ("PL에서 가장 핫한 유망주 누구야?", "soccer"),
    ("유럽에서 뛰는 한국 유망주 있어?", "soccer"),
    ("최근 폼 좋은 공격수 누구야?", "soccer"),
    ("올 시즌 도움 많이 한 선수는?", "soccer"),
    ("헤딩 잘하는 스트라이커 추천", "soccer"),
    ("수비형 미드필더 중 눈에 띄는 선수는?", "soccer"),
    ("골키퍼 중 세이브 능력 뛰어난 선수?", "soccer"),
    ("발재간 뛰어난 선수는 누구야?", "soccer"),
    ("측면 크로스 잘하는 선수 추천", "soccer"),
    ("포스트 플레이 잘하는 공격수는?", "soccer"),
    ("몸싸움 약하지만 기술 좋은 선수?", "soccer"),
    ("기복 없는 안정적인 선수는?", "soccer"),
    ("성장 가능성 높은 어린 선수는?", "soccer"),
    ("피파 랭킹 높은 선수 알려줘", "soccer"),
    ("기술 위주의 플레이하는 선수 추천", "soccer")
]


# 임베딩
texts, labels = zip(*examples)
model = SentenceTransformer("jhgan/ko-sroberta-multitask")
embeddings = model.encode(texts)

# FAISS 인덱스
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

def classify(text: str) -> bool:
    vec = model.encode([text])
    D, I = index.search(np.array(vec), k=1)
    return labels[I[0][0]] == "other"
