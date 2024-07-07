import streamlit as st
from utils import generate_redbook_scheme

st.header("小红书标题+内容生成")
with st.sidebar:
    openai_api_key = st.text_input('请输入您的OpenAI API密钥', type='password')
    st.markdown("[获取OpenAI API密钥](https://platform.openai.com/api-keys)")

theme = st.text_input("主题")
start = st.button("启动！")

if start:
    warning_msg = ""
    if not openai_api_key:
        warning_msg = "请输入您的OpenAI API 密钥！"
    elif not theme:
        warning_msg = "请输入您的主题"

    if warning_msg:
        st.info(warning_msg)
        st.stop()
    else:
        with st.spinner("AI思考中..."):
            result = generate_redbook_scheme(theme, openai_api_key)
        st.divider()
        l_column, r_column = st.columns(2)
        with l_column:
            for i in range(5):
                st.markdown(f"##### 标题{i+1}")
                st.write(result.titles[i])
        with r_column:
            st.markdown(f"##### 正文")
            st.write(result.content)
