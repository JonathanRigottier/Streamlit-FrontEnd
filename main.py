import streamlit as st
import pandas as pd

header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

with header:
	st.title('Welcome to my awesome data science project!')
	st.text('In this project I look into the transactions of taxis in NYC. ...')


with dataset:
	st.header('NYC taxi dataset')
	st.text('I found this dataset on blablable.com, ...')

	titanic = pd.read_csv('Data/titanic.csv')
	st.write(titanic.head())

	st.subheader('Age of the titanic passenger')
	age = pd.DataFrame(titanic['age'].value_counts())
	st.bar_chart(age)


with features:
	st.header('The features I created')

	st.markdown('* **first feature** I created this feature to calculate age')


with model_training:
	st.header('Time to train the model!')
	st.text('Here you can get what you want')

	sel_col, disp_col = st.columns(2)

	user_input = sel_col.slider('What should be the max_depth of the model?', 
		min_value=0, max_value=150, value=10, step=10)
	
	n_estimators = sel_col.selectbox('How many trees should there be?', options=[100,200,300,'No limit'], 
		index = 0)

	input_feature = sel_col.text_input('which feature should be used as the input feature?','PU')


