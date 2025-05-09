#importing libraries
import pickle
import pandas as pd
import streamlit as slt
import numpy as np
import os




# Page settings
slt.set_page_config(layout="wide")
slt.image(r"C:\vs\carprice\cardekho.jpg")
# Option menu
page = slt.sidebar.selectbox("Select a Page", ["CarDekho-Price Prediction", "User Guide"])


# CarDekho-Price Prediction Page
if page == "CarDekho-Price Prediction":
    slt.header(':blue[Cardheko-Price Prediction]')
   
   
    # Load data
    df = pd.read_csv("c:\Car\car_dekho_cleaned_dataset.csv")
    
    col1, col2 = slt.columns(2)
    with col1:
        Ft = slt.selectbox("Fuel type", ['Petrol', 'Diesel', 'Lpg', 'Cng', 'Electric'])
        Bt = slt.selectbox("Body type", ['Hatchback', 'SUV', 'Sedan', 'MUV', 'Coupe', 'Minivans',
                                           'Convertibles', 'Hybrids', 'Wagon', 'Pickup Trucks'])
        Tr = slt.selectbox("Transmission", ['Manual', 'Automatic'])
        Owner = slt.selectbox("Owner", [0, 1, 2, 3, 4, 5])
        Brand = slt.selectbox("Brand", options=df['Brand'].unique())
        filtered_models = df[(df['Brand'] == Brand) & (df['bt'] == Bt) & (df['ft'] == Ft)]['model'].unique()
        Model = slt.selectbox("Model", options=filtered_models)
        Model_year = slt.selectbox("Model Year", options=sorted(df['modelYear'].unique()))
        IV = slt.selectbox("Insurance Validity", ['Third Party insurance', 'Comprehensive', 'Third Party',
                                                   'Zero Dep', '2', '1', 'Not Available'])
        Km = slt.slider("Kilometers Driven", min_value=100, max_value=100000, step=1000)
        ML = slt.number_input("Mileage", min_value=5, max_value=50, step=1)
        seats = slt.selectbox("Seats", options=sorted(df['Seats_1'].unique()))
        color = slt.selectbox("Color", df['Color'].unique())
        city = slt.selectbox("City", options=df['City'].unique())

    with col2:
        Submit = slt.button("Predict")
        if Submit:
            

            file_path = "C:\\Car\\pipeline.pkl"

            if os.path.exists(file_path):
                with open(file_path, "rb") as files:
                 pipeline = files.read()
            else:
                print(f"File not found: {file_path}")

            #with open("c:\\Car\\pipeline.pkl",'rb') as files:
               # pipeline = pickle.load(files)

            # input data
            new_df = pd.DataFrame({
                'Fuel_type': Ft,
                'body_type': Bt,
                'transmission': Tr,
                'ownerNo': Owner,
                'Brand' :Brand,
                "model": Model,
                'modelYear': Model_year,
                'Insurance Validity': IV,
                'Kms Driven': Km,
                'Mileage': ML,
                'Seats': seats,
                'Color': color,
                'City': city
            }, index=[0])

            # Display the selected details
            data = [Ft, Bt, Tr, Owner, Model, Model_year, IV, Km, ML, seats, color, city]
            slt.write(data)

            # FINAL MODEL PREDICTION
           # prediction = pipeline.predict(new_df)
            #slt.write(f"The price of the {new_df['Brand'].iloc[0]} car is: {round(prediction[0], 2)} lakhs")

# User Guide Page
elif page == "User Guide":
    slt.header('User Guide for Streamlit-based CarDekho Price Prediction Application') 
    slt.write("""
    This guide explains how to interact with the CarDekho-Price Prediction application built using Streamlit. 
    The app allows users to input car details and predict the price based on various features like brand, model, fuel type, etc.
    
    **Steps to Use:**
    
    **STEP_1 Input Fields (Left Column):**
    In the first column, users will provide the following details about the car:
    - **Fuel Type:** Select the fuel type of the car from options like Petrol, Diesel, LPG, CNG, Electric.
    - **Body Type:** Choose the body type of the car. Options include Hatchback, SUV, Sedan, MUV, Coupe, etc.
    - **Transmission:** Choose whether the car has a Manual or Automatic transmission.
    - **Owner:** Select how many previous owners the car has had, ranging from 0 to 5.
    - **Brand:** Select the car brand from the available list of brands in the dataset.
    - **Model:** After selecting the brand, the app will automatically filter and display the relevant car models. Choose the model from the dropdown.
    - **Model Year:** Choose the year when the car was manufactured.
    - **Insurance Validity:** Select the insurance type (e.g., Third Party, Comprehensive, Zero Dep, etc.).
    - **Kilometers Driven:** Use the slider to enter how many kilometers the car has been driven (between 100 and 100,000 km).
    - **Mileage:** Enter the car's mileage using the number input (range 5–50 km/litre).
    - **Seats:** Select the number of seats in the car from the dropdown.
    - **Color:** Choose the color of the car.
    - **City:** Select the city where the car is located from the dropdown list.
    
    **STEP_2. Prediction Button (Right Column):**
    - **Submit Button:** Once all input fields are filled, press the Predict button in the second column to trigger the price prediction.
    
    **Output:**
    The predicted price of the car will appear on the screen in the format: The price of the [Brand] car is: [Price] lakhs.

    **Example Workflow:**
    1. Select Fuel type as Petrol.
    2. Choose Body type as Sedan.
    3. Pick Automatic transmission.
    4. Select that the car has had 3 previous owners.
    5. Choose BMW as the Brand.
    6. After selecting the brand, a filtered list of models will appear. Choose the BMW 5 Series model.
    7. Choose 2011 for the Model Year.
    8. Select Third Party insurance for Insurance Validity.
    9. Use the slider to set Kilometers Driven to 100000 km.
    10. Enter the Mileage as 18 km/litre.
    11. Choose 5 seats for the car.
    12. Select Bangalore as the color.
    13. Choose Delhi as the city.
    14. Press Predict.
    
    """)