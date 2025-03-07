import os
import streamlit as st # type: ignore
import sqlite3

# 데이터베이스 파일이 저장될 디렉터리
db_directory = "./"

# 데이터베이스 파일 경로 지정
db_path = os.path.join(db_directory, "data.db")

# 데이터베이스 연결 (파일이 없으면 새로 생성됨)
conn = sqlite3.connect(db_path, check_same_thread=False)
c = conn.cursor()

# 테이블 생성 (없을 경우)
c.execute('''
    CREATE TABLE IF NOT EXISTS user_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        message TEXT
    )
''')
conn.commit()

# 사용자 입력 받기
st.header("데이터 입력 폼")
name = st.text_input("이름 입력")
message = st.text_area("메시지 입력")

if st.button("저장"):
    # 입력 데이터를 데이터베이스에 저장
    c.execute("INSERT INTO user_data (name, message) VALUES (?, ?)", (name, message))
    conn.commit()
    st.success("데이터가 저장되었습니다!")
