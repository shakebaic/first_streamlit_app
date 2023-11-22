import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('Hello world')
streamlit.header('New restaurant offering food!')
streamlit.text('Meat')
streamlit.text('Fruit')
streamlit.text('Dairy')
streamlit.text('Whatever')
streamlit.text('🥑The end')
streamlit.header('Here is the list')

#import panda
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)

# ADd a pick list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruit:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table on the page
streamlit.dataframe(fruits_to_show)

#create the repeatable code block (called a function)
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

#New Section to display fruityvice apt response
streamlit.header('Fruityvice Fruit Advice!')
#New section to display fruityvice api response
#streamlit.header('Fruityvice Fruit Advice!')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
      streamlit.error("Please select a fruit")
  else:
     #fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)     
     #fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
     #streamlit.dataframe(fruityvice_normalized)
     back_from_function = get_fruityvice_data(fruit_choice)
     streamlit.dataframe(back_from_function)

except URLError as e:
    streamlit.error()


streamlit.header("The fruit load list contains:")
#Snowflake-related functions
def get_fruit_load_list():
  with my_cnx.curstor() as my_cur:
       my_cur.execute("select * from fruit_load_list")
    return my_cur.fetchall()

#Add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)

streamlit.write('The user entered', back_from_function)

#import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# don't run anything past here until we troubleshoot
streamlit.stop()

# take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output it to the screen as a table
streamlit.dataframe(fruityvice_normalized)




# lesson 2.12
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

# Allowthe end user to add a fruit to the list
add_my_fruit = streamlit.text_input('What fruit would you like to add?','')
streamlit.write('Thanks for adding', add_my_fruit)

#This will not work correctly, but try
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
