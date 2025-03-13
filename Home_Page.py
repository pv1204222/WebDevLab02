import streamlit as st
import info
def homepage():
    st.title("👋WELCOME TO MY HOMEPAGE👋")
    st.header("Patrick Vettickatt")
    st.write("CS 1301 Intro to Computing")
    st.image(info.python, width= 200)  

    st.subheader("Page Descriptions")
    st.markdown("- **My Portfolio:** Information about me! Open the menu bar on the right to meet me!")
    st.markdown("- **Weather:** Search your location or somewhere else based off of longitude and latitude. Get the weather for the next week!")

if __name__ == "__main__":
    homepage()