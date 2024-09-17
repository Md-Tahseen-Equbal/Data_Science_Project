import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open(r'C:\Users\91771\Desktop\Innomatic\Machine Learning\Project 1\model.pkl', 'rb') as f:
    model = pickle.load(f)
st.title('Innomatics Research Labs')
st.title('ML Project 1: Estimating the Time of Arrival')

# Input fields for user to enter the values
start_lat = st.number_input('Enter the start latitude:', format="%.4f")
start_lang = st.number_input('Enter the start longitude:', format="%.4f")
end_lat = st.number_input('Enter the destination latitude:', format="%.4f")
end_lang = st.number_input('Enter the destination longitude:', format="%.4f")
dist = st.number_input('Enter the distance:', format="%.2f")
density = st.number_input('Enter the density:', min_value=0, step=1)
weather = st.number_input('Enter the weather value (rainy-1, foggy-2, clear-3):', min_value=1, max_value=3, step=1)
day = st.number_input('Enter the day:', min_value=0, max_value=6, step=1)
hour = st.number_input('Enter the hour:', min_value=0, max_value=23, step=1)

# Button to make prediction
if st.button('Predict'):
    # Make prediction
    input_data = np.array([[start_lat, start_lang, end_lat, end_lang, dist, density, weather, day, hour]])
    estimated_time = model.predict(input_data)[0]
    
    # Display the result
    st.success(f'The estimated time is {estimated_time} minutes.')
