import streamlit as st
import numpy as np
from pandas import DataFrame
from keybert import KeyBERT
# For Flair (Keybert)
import seaborn as sns
# For download buttons
from functionforDownloadButtons import download_button
import os
import json

st.set_page_config(
    page_title="Review Analyzer |Topic Modeling",
    page_icon="🎈",
)


def _max_width_():
    max_width_str = f"max-width: 1800px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )

_max_width_()

c30, c31, c32 = st.columns([2.5, 1, 3])

with c30:
    # st.image("logo.png", width=400)
    st.title("🔑 Review Analyzer")
    st.header("")

with st.expander("ℹ️ - About this app", expanded=True):
    st.write(
        """     
-   Cette Application est pour le Topic Modeling 
- Ecrire votre avis et regarde la magie ! 	    """
    )

    st.markdown("")

st.markdown("")
st.markdown("## **📌 Paste document **")
with st.form(key="my_form"):
    ce, c1, ce, c2, c3 = st.columns([0.07, 1, 0.07, 5, 0.07])
    with c1:
        ModelType = st.radio(
            "Quel texte analyser ?",
            ["Avis dataset", "Texte libre"],
            help="At present, you can choose between 2 models (Flair or DistilBERT) to embed your text. More to come!",
        )



        top_N = st.slider(
            "Mettez le nombre de Topic souhaité",
            min_value=1,
            max_value=15,
            value=10,
            help="You can choose the number that you want between 1 and 15.",
        )

    with c2:
        doc = st.text_area(
            "Paste your text below (max 500 words)",
            height=510,
        )

        MAX_WORDS = 500
        import re

        res = len(re.findall(r"\w+", doc))
        if res > MAX_WORDS:
            st.warning(
                "⚠️ Your text contains "
                + str(res)
                + " words."
                + " Only the first 500 words will be reviewed. Stay tuned as increased allowance is coming! 😊"
            )

            doc = doc[:MAX_WORDS]

        submit_button = st.form_submit_button(label="✨ Donnez moi les topics!")


st.markdown("## **🎈 Check & download results **")

st.header("")

cs, c1, c2, c3, cLast = st.columns([2, 1.5, 1.5, 1.5, 2])


st.header("")






c1, c2, c3 = st.columns([1, 3, 1])

format_dictionary = {
    "Relevancy": "{:.1%}",
}



