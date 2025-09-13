import streamlit as st
st.title('나의 첫 웹앱!')
st.write('이걸 내가 만들었다고?!')

import streamlit as st
import time

st.set_page_config(page_title="MBTI 영어 공부 추천", page_icon="📚", layout="centered")

# 🎨 스타일 효과
st.markdown(
    """
    <style>
    .big-font {
        font-size:30px !important;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🎉 제목
st.title("✨ MBTI로 알아보는 영어 공부법 ✨")
st.write("👉 자신의 **MBTI**를 선택하면, 딱 맞는 영어 공부법을 알려줄게요! 🥳")

# MBTI 목록
mbti_types = [
    "ENFP", "ENTP", "INFP", "INFJ", "ENFJ", "ENTJ",
    "INTP", "INTJ", "ESFP", "ESTP", "ISFP", "ISTP",
    "ESFJ", "ESTJ", "ISFJ", "ISTJ"
]

# 📌 사용자 입력
choice = st.selectbox("MBTI를 골라보세요 🧩", mbti_types)

# 추천 공부법 딕셔너리
recommendations = {
    "ENFP": "🎤 노래 따라 부르기 + 친구랑 롤플레잉! (재미있게 하면서 기억해요!)",
    "ENTP": "🗣 토론식 영어! 친구랑 말싸움(?) 하듯이 연습해보세요 😆",
    "INFP": "📖 영어 일기 쓰기 ✍️ → 감정을 담아서 쓰면 실력이 쑥쑥!",
    "INFJ": "🌌 조용히 영어 소설 읽기 + 명언 필사 ✨",
    "ENFJ": "👫 친구 가르치기! 영어 선생님이 되어보세요 🎓",
    "ENTJ": "📊 계획표 세우고 영어 목표 달성하기! (게임처럼 레벨업 💪)",
    "INTP": "🧩 퍼즐·퀴즈로 영어 단어 배우기! 두뇌 풀가동 🧠",
    "INTJ": "📚 영어 공부 계획 + 꾸준한 독서 📖 (전략적으로!)",
    "ESFP": "🎶 뮤직비디오 보면서 춤추며 영어 가사 외우기 💃",
    "ESTP": "🎮 게임하면서 영어 배우기! (마이크 켜고 외국인 친구랑!)",
    "ISFP": "🎨 그림 그리며 영어 단어 적기 ✏️ (감각적으로 배워요!)",
    "ISTP": "🛠 만들기·실험하면서 영어 설명 따라하기 ⚡",
    "ESFJ": "👯 그룹 스터디에서 친구랑 대화 연습하기 🗨️",
    "ESTJ": "✅ 체크리스트 만들고 하루하루 달성하기! (성취감 업 🏆)",
    "ISFJ": "💌 좋아하는 캐릭터에게 영어 편지 쓰기 📮",
    "ISTJ": "📑 단어장 정리하고 매일 복습하기 📘 (꾸준함이 답!)",
}

# 버튼 누르면 결과 보여주기
if st.button("🎁 나만의 영어 공부법 보기!"):
    with st.spinner("두구두구... 🤔 최고의 방법을 찾고 있어요..."):
        time.sleep(2)

    st.success("짜잔! 🥳")
    st.markdown(f"<p class='big-font'>{recommendations[choice]}</p>", unsafe_allow_html=True)

    st.balloons()  # 🎈 풍선 효과
