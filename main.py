import pickle
from pathlib import Path

import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth

names = ["Jonathan Rigottier", "Maxence Rigottier"]
usernames = ["jrigo", "mrigo"]

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
	hashed_passwords = pickle.load(file)

credentials = {"usernames":{}}

for un, name, pw in zip(usernames, names, hashed_passwords):
    user_dict = {"name":name,"password":pw}
    credentials["usernames"].update({un:user_dict})

authenticator = stauth.Authenticate(credentials, "titanic_data", "abcdeefgh", cookie_expiry_days=30)

name, authentiction_status, username = authenticator.login("Login", "main")

if authentiction_status == False:
	st.error("Nom/mot de passe incorrect(s)")

if authentiction_status == None:
	st.warning("Veuillez entrer votre nom et votre mot de passe")

if authentiction_status:


	st.title(f"Bienvenue {name}")
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

authenticator.logout("Logout", "main")



