import pickle
import streamlit as st
import pandas as pd
import numpy as np
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


st.image('inno logo.jpeg')
st.title("Fedex Delivery Tracker")
model = pickle.load(open(r"./Fedex.pkl","rb"))

carrier_name = pickle.load(open(r'./Carrier_Name.pkl','rb'))
destination = pickle.load(open(r'./Destination.pkl','rb'))
source = pickle.load(open(r'./Source.pkl','rb'))


data = { 
        "Month" : st.selectbox(label='Enter the month (1-6): ', options=[1, 2, 3, 4, 5, 6]),
        
        "DayofMonth" : st.date_input(
        "Select the date:", 
        value=None,  # Default to None or set a specific date like pd.Timestamp('2024-01-01')
        min_value=pd.Timestamp('2008-01-01'),  # Set the minimum date, adjust as needed
        max_value=pd.Timestamp('2008-12-31')  # Set the maximum date, adjust as needed
    ),
        
     "DayOfWeek" : st.number_input(
        "Enter the day of the week (1 for Monday, 7 for Sunday): ", 
        min_value=1, max_value=7, value=1, step=1, format='%d'
    ),
    
    "Actual_Shipment_Time" : st.number_input(
        "Enter the actual shipment time (1-10000): ",
        min_value=1, max_value=10000, value=1, step=1, format='%d'
    ),
    
    "Planned_Shipment_Time" : st.number_input(
        "Enter the planned shipment time (1-10000): ",
        min_value=1, max_value=10000, value=1, step=1, format='%d'
    ),
    
    "Planned_Delivery_Time" : st.number_input(
        "Enter the planned delivery time (1-10000): ",
        min_value=1, max_value=10000, value=1, step=1, format='%d'
    ),

    "Carrier_Name" : st.selectbox("Enter the carrier name: ",options=carrier_name),
    
    "Carrier_Num" : st.number_input(
        "Enter the carrier number: ",
        min_value=1, max_value=10000, value=1, step=1, format='%d'
    ),
    
    "Planned_TimeofTravel" : st.number_input(
        "Enter the planned time of travel in hours: ",
        min_value=1, max_value=2000, value=1, step=1, format='%d'
    ),
    
    "Shipment_Delay" : st.number_input(
        "Enter the shipment delay in hours: ",
        min_value=0, max_value=2000, value=0, step=1, format='%d'
    ),
    
    "Source" : st.selectbox("Enter the source location: ", options=source),
    
    "Destination" : st.selectbox("Enter the destination location: ", options=destination),
    
    "Distance" : st.number_input(
        "Enter the distance in kilometers: ",
        min_value=1, max_value=10000, value=1, step=1, format='%d'
    ),

}

data['DayofMonth'] = data['DayofMonth'].day

input_data = pd.DataFrame([data])

if st.button('Submit'):
    
  Delivery_Status = model.predict(input_data)[0]
  if Delivery_Status == 0.0:
    # st.header(f"The predicted delivery status is: {Delivery_Status}")
        st.header(f"  delivery not done {Delivery_Status}")
  else:
        st.header(f"  delivery done {Delivery_Status}")

  
