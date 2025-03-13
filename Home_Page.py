import streamlit as st
def homepage():
    st.title("WELCOME TO MY HOMEPAGE")
    st.header("Patrick Vettickatt")
    st.write("CS 1301 Intro to Computing")

    st.subheader("Page Descriptions")
    st.markdown("- **My Portfolio:** ")
    st.markdown("- **Page 2:** ")

if __name__ == "__main__":
    homepage()