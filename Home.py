import streamlit as st
import streamlit.components.v1 as components
from config import *

st.set_page_config(
    page_title="AniBase Docs",
    page_icon=":book:",
)

st.title("Welcome to AniBase Docs")

st.write("""
Here you will find the terms, the privacy policy and other documents related to AniBase.
""")

st.write(f"""
<style>
    a {{
        text-decoration: none !important;
    }}

    .container {{
        display: flex;
        flex-direction: column;
        gap: 1.5rem;
        margin-top: 1.5rem;
    }}
    .link {{
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-between; 
        border-width: 1px; 
        border-color: {THEME_SECONDARY_BACKGROUND_COLOR}; 
        transition: .150s; 
        border-style: solid; 
        border-radius: 5px; 
        padding: 1.25rem;
    }}
    .link:hover {{
        border-color: {THEME_PRIMARY_COLOR};
    }}
    .link-title {{
        font-family: {THEME_FONT.replace(' ', '-')};
        color: {THEME_TEXT_COLOR};
        font-size: 1.2rem;
        font-weight: 600;
        line-height: 1;
    }}
    .arrow-icon {{
        height: 1.5rem;
        width: 1.5rem;
        color: {THEME_TEXT_COLOR};
    }}
</style>
<dic class="container">
    <a class="link" href="/Privacy_Policy" target="_self">
        <div class="link-title">
            Privacy Policy
        </div>
        <svg class="arrow-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
    </a>
    <a class="link" href="/Terms_and_Conditions" target="_self">
        <div class="link-title">
            Terms and Conditions
        </div>
        <svg class="arrow-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
    </a>
</div>
""", unsafe_allow_html=True)