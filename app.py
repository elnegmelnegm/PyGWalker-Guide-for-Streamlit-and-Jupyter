import pygwalker as pyg
import streamlit.components.v1 as components
import pandas as pd
import streamlit as st

# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="DataViz App",
    page_icon=":snake:",
    layout="wide"
)

def load_data(data):
  return pd.read_csv(data)

def main():
  menu = ["Home", "About"]
  choice = st.sidebar.selectbox("Menu", menu)
  st.title("DataViz app")
  if choice == "Home":
    st.subheader("Home")
    with st.form("upload_form"):
      data_file = st.file_uploader("Upload your file", type=["csv", "text"])
      submitted = st.form_submit_button("Submit")
    if submitted:
      df = load_data(data_file)
      st.dataframe(df)
      pyg_html = pyg.walk(df, return_html=True, hideDataSourceConfig=False)
      components.html(pyg_html, height=1000, scrolling=True)
  else:
    image_path = 'https://www.edaegypt.gov.eg/media/wc3lsydo/group-287.png'
    st.image(image_path)
    st.text("This app uses PyGWalker and Streamlit") 
    st.text("PyGWalker is a Python library turning data into a visually interactive interface ")
    st.text("and make your data exploration as intuitive as using Tableau.")
if __name__ == "__main__":
  main()
