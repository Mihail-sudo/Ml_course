import streamlit as st
import pickle

with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

layout = 'centered'
page_title = 'Iris App'
page_icon = ':rose:'

st.set_page_config(page_title=page_title, layout=layout, page_icon=page_icon)

st.title(page_icon + ' ' + page_title)

html_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
"""

st.markdown(html_style, unsafe_allow_html=True)

with st.sidebar:
    st.markdown('## Iris Classificatoin App')

with st.container():
    with st.form(key='my_form'):
        st.text('enter details below')
        sep_len = st.number_input(label='Sepal lenght')
        sep_wid = st.number_input(label='Sepal width')
        pet_len = st.number_input(label='Petal lenght')
        pet_wid = st.number_input(label='Petal width')

        submitted = st.form_submit_button(label='Predict')

    if submitted:
        data = [[sep_len, sep_wid, pet_len, pet_wid]]

        st.text(data)

        flowers = {0: 'Setosa', 
                   1: 'Versicolor', 
                   2: 'Virginica'}
        
        predicted_flower = flowers[model.predict(data)[0]]
        st.text(predicted_flower)

        if predicted_flower == 'Setosa':
            st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Irissetosa1.jpg/413px-Irissetosa1.jpg')
        elif predicted_flower == 'Versicolor':
            st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Iris_versicolor_3.jpg/800px-Iris_versicolor_3.jpg')
        else:
            st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Iris_virginica_2.jpg/330px-Iris_virginica_2.jpg')
