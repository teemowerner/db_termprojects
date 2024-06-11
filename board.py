import streamlit as st
import os
import streamlit.components.v1 as components
from query import actor_info
from query import generation_movie


st.set_page_config(
    page_title="데이터베이스설계 Term Projects",
    page_icon="👋",
)
st.markdown('<p class="big-font">DB Term Project</p>', unsafe_allow_html=True)
st.markdown('<p class="big-font">김하연, 김동건, 조영휘! 👋</p>', unsafe_allow_html=True)
st.markdown(""" * * * """)

st.markdown(
"""
# 주요 기능
"""
)
st.markdown(
"""
* ### 별점 확인, 제작사, 장르, 시리즈, 출연진 확인

"""
)
st.markdown("""<br><br>""", unsafe_allow_html=True)
st.markdown(
"""
## 개봉한 새로운 영화를 추가하는 기능 확장예정
"""
)
st.markdown(
"""
* ### 5개의 페이지로 구성 
"""
)
st.markdown(""" * * * """)

st.markdown("""
<style>
.big-font {
    font-size:60px !important;
}
</style>
""", unsafe_allow_html=True)
select_tab =  st.sidebar.selectbox(
    "어떤 기준으로 보고싶으신가요 ?",
    ('연도별', '배우별', '제작사별', 'genre', 'series', 'castings')                      
    )

if select_tab == '배우별':
    st.markdown(
    """
    # 🎬 배우 이름을 입력해 주세요 ! 🕺💃🏻
    ## 예시 ) ANGELINA JOLIE, TOM HANKS
    ## BRAD PITT, ROBIN WILLIAMS
    """
    )
    title = st.text_input("배우 이름", "TOM CRUISE")
    for i in range(len(actor_info(title))):
        st.write(actor_info(title)[i][0])


if select_tab == '연도별':
    """
    ## 🎬 보고싶은 영화의 연도를 입력해 주세요 ! 🕺💃🏻
    """
    st.markdown("""
    <style>
    .big-font {
        font-size:60px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    select_tab =  st.selectbox(
    "어떤 연도로 확인할까요?",
    ('60s', '70s', '80s', '90s')                      
    )
    if select_tab == '60s':
        # for i in range(len(generation_movie(6))):
        # st.write(generation_movie(6))
        length = len(generation_movie(6))
        for i in range(length):
            st.write(generation_movie(6)[i])
        st.markdown("""
                    ## 이상{} 평점 높은 영화
                    """.format('60s'))
    
    if select_tab == '70s':
        # for i in range(len(generation_movie(6))):
        # st.write(generation_movie(6))
        length = len(generation_movie(7))
        for i in range(length):
            st.write(generation_movie(7)[i])
        st.markdown("""
                    ## 이상{} 평점 높은 영화
                    """.format('70s'))
        
    if select_tab == '80s':
        # for i in range(len(generation_movie(6))):
        # st.write(generation_movie(6))
        length = len(generation_movie(8))
        for i in range(length):
            st.write(generation_movie(8)[i])
        st.markdown("""
                    ## 이상{} 평점 높은 영화
                    """.format('80s'))
        
    if select_tab == '90s':
        # for i in range(len(generation_movie(6))):
        # st.write(generation_movie(6))
        length = len(generation_movie(9))
        for i in range(length):
            st.write(generation_movie(9)[i])
        st.markdown("""
                    ## 이상{} 평점 높은 영화
                    """.format('90s'))
if select_tab == 'production':
    st.markdown(
        """
        # production : 
        """
    )



   

        

        

