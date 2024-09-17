import streamlit as st
import pandas as pd
import numpy as np

from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler,OneHotEncoder,OrdinalEncoder

from sklearn.compose import ColumnTransformer

import pickle


st.title("Sustainability Rating prediction")

with st.form("rating_prediction"):
    Age = st.number_input("Enter Age", value=35) 
    Location =  st.selectbox("pick Location", ['Urban', 'Suburban', 'Rural'])
    DietType = st.selectbox("pick DietType", ['Mostly Plant-Based', 'Balanced', 'Mostly Animal-Based'])
    LocalFoodFrequency = st.selectbox("pick LocalFoodFrequency", ['Often', 'Sometimes', 'Rarely', 'Always'])
    TransportationMode =  st.selectbox("pick TransportationMode", ['Bike', 'Public Transit', 'Car', 'Walk'])
    EnergySource =  st.selectbox("pick EnergySource", ['Renewable', 'Mixed', 'Non-Renewable'])
    HomeType = st.selectbox("pick HomeType", ['Apartment', 'House', 'Other'])
    HomeSize = st.number_input("Enter HomeSize", value = 800) 
    ClothingFrequency =  st.selectbox("pick ClothingFrequency", ['Rarely', 'Sometimes', 'Often', 'Always'])
    SustainableBrands = st.selectbox("pick SustainableBrands", [True, False])
    EnvironmentalAwareness = st.selectbox("pick EnvironmentalAwareness", [5, 4, 2, 3, 1])
    CommunityInvolvement = 'High' or  st.selectbox("pick CommunityInvolvement", ['High', 'Moderate', 'Low',])
    MonthlyElectricityConsumption = st.number_input("Enter MonthlyElectricityConsumption", value = 291) 
    MonthlyWaterConsumption = st.number_input("Enter MonthlyWaterConsumption", value = 3139) 
    Gender = 'Male' or st.selectbox("pick Gender", ['Female', 'Male', 'Non-Binary', 'Prefer not to say'])
    UsingPlasticProducts = st.selectbox("pick UsingPlasticProducts", ['Rarely', 'Sometimes', 'Often', 'Never'])
    DisposalMethods = st.selectbox("pick DisposalMethods", ['Composting', 'Recycling', 'Landfill', 'Combination'])
    PhysicalActivities = st.selectbox("pick PhysicalActivities", ['High', 'Moderate', 'Low', ])
    # Rating = st.selectbox("pick Rating", [5, 4, 1, 3, 2])
    submit_btn = st.form_submit_button('Submit')
    

        
        

    
    
if submit_btn:
    user_input = [
            Age,
            Location,
            DietType,
            LocalFoodFrequency,
            TransportationMode,
            EnergySource,
            HomeType,
            HomeSize,
            ClothingFrequency,
            SustainableBrands,
            EnvironmentalAwareness,
            CommunityInvolvement,
            MonthlyElectricityConsumption,
            MonthlyWaterConsumption,
            Gender,
            UsingPlasticProducts,
            DisposalMethods,
            PhysicalActivities
        ]
    user_input_df = pd.DataFrame([user_input], columns=[
            'Age', 'Location', 'DietType', 'LocalFoodFrequency', 'TransportationMode', 
            'EnergySource', 'HomeType', 'HomeSize', 'ClothingFrequency', 
            'SustainableBrands', 'EnvironmentalAwareness', 'CommunityInvolvement', 
            'MonthlyElectricityConsumption', 'MonthlyWaterConsumption', 
            'Gender', 'UsingPlasticProducts', 'DisposalMethods', 'PhysicalActivities'
        ])
    # Path to your pickle file
    file_path = './sustainability_rating_predictor.pkl'

    # Open the pickle file in binary read mode and load the object
    with open(file_path, 'rb') as file:
        model = pickle.load(file)
        prediction = model.predict(user_input_df)
        # Display the prediction
        st.write(f"Predicted Sustainability Rating: {prediction}")