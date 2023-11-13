import streamlit

streamlit.title('Hello world')

streamlit.header('Here is my new resume')
streamlit.text('Basic')
streamlit.text('dBase III+')
streamlit.text('Delphi')
streamlit.text('Python')
streamlit.text('🥑The end')
streamlit.header('The learning never ends')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
