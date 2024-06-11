import streamlit as st
from query import actor_info

# ANGELINA JOLIE
# TOM HANKS
# BRAD PITT
st.markdown(
"""
# 배우 이름을 입력해 주세요 !
"""
)
title = st.text_input("배우 이름", "TOM CRUISE")
# st.write(title + "이 출연한 영화 목록 : ", actor_info(title))
for i in range(len(actor_info(title))):
    st.write(actor_info(title)[i][0])
