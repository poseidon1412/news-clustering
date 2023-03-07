import pandas as pd
import streamlit as st

# @st.cache(suppress_st_warning=True)



st.markdown("""
    <h1 style='text-align: center; margin-bottom: -35px;'>
    Product Image Description Clustering
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

df = pd.read_csv("question3.csv")
# df["img_src"]=df["img_src"].values.astype('string')




def clusters_main():
    for i in range(len(df.cluster.unique())):
        clusta = df.cluster.unique()[i]
        st.write(clusta) 
        # print(clusta)   
        funct_1(clusta)


def funct_1(clus):
    df_new = df[df["cluster"] == clus]
    image_s = df_new.img_src.tolist()
    description = df_new.img_decription.tolist()
    go_through(image_s, description)


def go_through(list1, list2):
    for i in range(len(list1)):
        image_source = list1[i]
        image_ds = list2[i]
        st.image(image_source)
        st.write(image_ds)
        st.write(" ")
        

clusters_main()





# main()


