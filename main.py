import pandas as pd
import streamlit as st

# @st.cache(suppress_st_warning=True)



st.markdown("""
    <h1 style='text-align: center; margin-bottom: -35px;'>
    News Clustering
    </h1>
""", unsafe_allow_html=True
)

st.caption("""
    <p style='text-align: center'>
    proudly brought to you by unsupervised machine learning.
    </p>
""", unsafe_allow_html=True
)

st.write("""
    <h2>
    </h2>
    """,unsafe_allow_html=True
)

df = pd.read_csv("question2.csv")



def clusters_main():
    for i in range(len(df.clusters.unique())):
        cluster = df.clusters.unique()[i]
        st.write(cluster)    
        funct_1(cluster)


def funct_1(clus):
    df_new = df[df["clusters"] == clus]
    title_list = df_new.title.tolist()
    url_list = df_new.url.tolist()
    go_through(title_list, url_list)


def go_through(list1, list2):
    for i in range(len(list1)):
        news_headline = list1[i]
        news_url = list2[i]
        st.write(news_headline)
        st.write(news_url)
        st.write(" ")

clusters_main()





# main()



