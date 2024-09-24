# Import python packages
import streamlit as st
#from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(":cup_with_straw: Customize Your Smoothie! :cup_with_straw:")
st.write(
    "Choose the fruits you want in your custome Smoothie! "
)

import streamlit as st

title = st.text_input("Name on Smoothie :")
#st.write("The Name on your Smoothie will be : ", title)
name_on_order = title;
#option = st.selectbox(
#    "What is Your favorite Fruit?",
#    ("Banana", "Strawberries", "Peaches"),
#)

#st.write("Your favorite fruits is :", option)/

#session = get_active_session()
cnx = st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)
#ingredients_list = st.multiselect ('Choose upto 5 ingredients :',my_dataframe)

ingredients_list = st.multiselect(
    'Choose only 5 ingredients',
    my_dataframe,
    max_selections = 5
)

if ingredients_list:
   #st.write(ingredients_list)
   #st.text(ingredients_list)

   ingredients_string = ''
   for fruit_choosen in ingredients_list:
        ingredients_string += fruit_choosen + ' '
       
#st.write(ingredients_string)    

   my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values ('""" + ingredients_string + """','""" + name_on_order + """')"""
   time_to_submit = st.button ('Submit Order')
   #st.write(my_insert_stmt)
   if time_to_submit:
      session.sql(my_insert_stmt).collect()
       
      st.success('Your Smoothie is ordered!', icon="✅")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#st.text(fruityvice_response.json())
fv_df = st.dataframe(data=fruityvice_response.json(),use_container_width = true)
