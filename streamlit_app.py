import streamlit

streamlit.title('Hello world')

streamlit.header('New restaurant offering food!')
streamlit.text('Meat')
streamlit.text('Fruit')
streamlit.text('Dairy')
streamlit.text('Whatever')
streamlit.text('🥑The end')
streamlit.header('Here is the list')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

# ADd a pick list here so they can pick the fruit they want to include
streamlist.multiselect("Pick some fruit:" list(my_fruit_list.index))

#display the table on the page
streamlit.dataframe(my_fruit_list)
