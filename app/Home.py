import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def run():

    st.header("Fleetio Metrics")

    st.write(f"<a style='text-decoration: none; margin:0px;' target='_self' href='{st.secrets['base_url']}/Page_1?param=1'>Page 1</a>", unsafe_allow_html=True)
    st.write(f"<a style='text-decoration: none; margin:0px;' target='_self' href='{st.secrets['base_url']}/Page_2?param=1'>Page 2</a>", unsafe_allow_html=True)
    st.write(f"<a style='text-decoration: none; margin:0px;' target='_self' href='{st.secrets['base_url']}/Page_3?param=1'>Page 3</a>", unsafe_allow_html=True)

if __name__ == "__main__":
    run()
