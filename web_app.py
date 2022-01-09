# Core Pkgs
import streamlit as st
import sklearn
import joblib,os
import numpy as np 

# Loading Models
def load_prediction_model(model_file):
	loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
	return loaded_model

def main():
	"""Rainwater harvesting determining App"""

	st.title("Rainwater harvesting determining App")

	html_templ = """
	<div style="background-color:blue;padding:10px;">
	<h3 style="color:cyan">we will determine the amount of water needed to be harvested as per the need of the family</h3>
	</div>
	"""

	st.markdown(html_templ,unsafe_allow_html=True)

	activity = ["Rainwater harvesting Determination","About"]
	choice = st.sidebar.selectbox("Menu",activity)

# Rainwater harvesting Determination CHOICE
	if choice == 'Rainwater harvesting Determination':

		st.subheader("Rainwater harvesting Determination")

		experience = st.slider("No. of people in the family",1,20)

		#st.write(type(experience))

		if st.button("Determination"):

			regressor = load_prediction_model("models/linear_regression_water.pkl")
			experience_reshaped = np.array(experience).reshape(-1,1)

			#st.write(type(experience_reshaped))
			#st.write(experience_reshaped.shape)

			predicted_waterAmount = regressor.predict(experience_reshaped)

			st.info("The total rainwater required to be harvested for 1 year time for {} people in the family is : {} liters.".format(experience,(predicted_waterAmount[0][0].round(2))))

# About CHOICE
	if choice == 'About':
		st.subheader("About")
		st.markdown("""
			## Rainwater harvesting Determination""")

if __name__ == '__main__':
	main()
