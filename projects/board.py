import streamlit as st
import os
import streamlit.components.v1 as components
from query import actor_info


st.set_page_config(
    page_title="DB Term Projects",
    page_icon="👋",
)
st.markdown("""
<style>
.big-font {
    font-size:60px !important;
}
</style>
""", unsafe_allow_html=True)
select_tab =  st.sidebar.selectbox(
    "어떤 기준으로 보고싶으신가요 ?",
    ('ratings', 'actors', 'production', 'genre', 'series', 'castings')                      
    )
if select_tab == 'actors':
    st.markdown(
    """
    # 🎬 배우 이름을 입력해 주세요 ! 🕺💃🏻
    ## 예시 ) ANGELINA JOLIE, TOM HANKS
    ## BRAD PITT, ROBIN WILLIAMS
    """
    )
    title = st.text_input("배우 이름", "TOM CRUISE")
    # st.write(title + "이 출연한 영화 목록 : ", actor_info(title))
    for i in range(len(actor_info(title))):
        st.write(actor_info(title)[i][0])


if select_tab == 'ratings':
    st.markdown(
        """ 
        # ratings
        """
    )
if select_tab == 'production':
    st.markdown(
        """
        # production : 
        """
    )

st.markdown('<p class="big-font">DB Term Project</p>', unsafe_allow_html=True)
st.markdown('<p class="big-font">김하연, 김동건, 조영휘! 👋</p>', unsafe_allow_html=True)
st.markdown(""" * * * """)

# st.markdown('<style>' + open('./style/side.css').read() + '</style>', unsafe_allow_html=True)
    
print(os.getcwd())


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


   

        

        

