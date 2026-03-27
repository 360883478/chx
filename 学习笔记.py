# 原理：导入Streamlit工具，让Python能生成网页
import streamlit as st

# 原理：设置网页标题和布局（wide=宽屏）
st.set_page_config(page_title="我的学习笔记", layout="wide")

# 原理：在网页顶部显示大标题
st.title("📒 我的智能学习笔记")

# 原理：创建左侧侧边栏（用来写笔记）
with st.sidebar:
    st.header("✍️ 写新笔记")
    # 原理：下拉选择分类
    category = st.selectbox("选择分类", ["金融学习", "考研资料", "创业想法", "生活记录"])
    # 原理：多行文本输入框
    content = st.text_area("笔记内容", height=200)
    # 原理：保存按钮
    if st.button("保存笔记"):
        if content:
            st.success("✅ 保存成功！")
        else:
            st.warning("⚠️ 内容不能为空")

# 原理：主页面显示已保存的笔记
st.header("📚 我的笔记库")
st.write("这里会显示你保存的所有笔记")
#要运行这个网页的话，先搜索cmd，打开cmd，切换D盘（D：），再输入 python -m streamlit run 学习笔记.py，就可以打开了