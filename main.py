import streamlit as st
import pandas as pd

header = st.container()
dataset = st.container()

with header:
	st.title('Welcome to my awesome data science project!')
	st.text('In this project I look into the titanic passengers. ...')


with dataset:
	st.header('Titanic dataset')
	st.text('I found this dataset on a free course, ...')

	titanic = pd.read_csv('Data/titanic.csv')
	st.write(titanic.head())

	st.subheader('Age of the titanic passenger')
	age = pd.DataFrame(titanic['age'].value_counts())
	st.bar_chart(age)

	st.subheader('Class of the titanic passenger')
	pclass = pd.DataFrame(titanic['pclass'].value_counts())
	st.bar_chart(pclass)

	st.subheader('Fare of the titanic passenger')
	fare = pd.DataFrame(titanic['fare'].value_counts())
	st.bar_chart(fare)





