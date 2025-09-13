import streamlit as st
st.title('나의 첫 웹앱!')
st.write('이걸 내가 만들었다고?!')

import streamlit as st
import pandas as pd
import altair as alt
import os

# 앱 제목
st.title("🌍 MBTI 유형별 국가 TOP10")

# 데이터 불러오기
@st.cache_data
def load_data():
    file_path = "countriesMBTI_16types.csv"
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
    else:
        uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type="csv")
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
        else:
            st.stop()
    return df

df = load_data()

# MBTI 유형 목록
mbti_types = df.columns[1:]  # 첫 번째 열은 Country, 나머지는 MBTI 유형

# 사이드바에서 MBTI 유형 선택
selected_type = st.sidebar.selectbox("MBTI 유형을 선택하세요:", mbti_types)

# 선택된 MBTI 유형 TOP10 국가 추출
top10 = df[["Country", selected_type]].sort_values(by=selected_type, ascending=False).head(10)

# Altair 차트 생성
chart = (
    alt.Chart(top10)
    .mark_bar()
    .encode(
        x=alt.X(selected_type, title=f"{selected_type} 비율"),
        y=alt.Y("Country", sort='-x', title="국가"),
        tooltip=["Country", selected_type]
    )
    .properties(width=600, height=400, title=f"{selected_type} 비율이 가장 높은 국가 TOP10")
    .interactive()
)

st.altair_chart(chart, use_container_width=True)

# 데이터 테이블 표시
st.dataframe(top10.reset_index(drop=True))
