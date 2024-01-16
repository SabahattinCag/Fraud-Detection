__author__ = "Sabahattin Cag"

import pandas as pd
import joblib
import streamlit as st

st.markdown("""<p style="background-color:blue; color:floralwhite; font-size:300%; text-align:center; border-radius:10px 10px; font-family:newtimeroman; line-height: 1.4;">Credit Card Fraud Detection</p>""", unsafe_allow_html=True)
st.markdown("""Welcome to the Fraud Detection Project! In this project, we delve into the intricacies of fraud detection using credit card transaction data from September 2013. The dataset encapsulates a two-day period, featuring 492 instances of fraud out of 284,807 transactions. Notably, frauds represent a mere 0.172% of all transactions, making the dataset highly unbalanced.

The challenges encountered in this project include the absence of domain knowledge and the imbalanced class frequencies of the target variable. Without prior knowledge of column names, our focus shifts to understanding the values themselves. The unbalanced nature of the dataset prompts the need for effective techniques to handle class imbalance.

Having overcome these challenges, our fraud detection model showcases remarkable performance metrics – an F1 Score of 0.805, Accuracy at 99.9%, Precision of 0.886, Recall standing at 0.737, and an AUC-ROC score of 0.868. These metrics affirm the model's ability to identify and predict fraudulent transactions with precision.
""")

st.image('data_overview.png', caption='Some samples from data')

st.sidebar.header('Logistic Regression Algorithm')
st.sidebar.subheader('Select the values of the variables')

min_values = {'Time': 0.0, 'V1': -56.408, 'V2': -72.716, 'V3': -48.326, 'V4': -5.683, 'V5': -113.743,
              'V6': -26.161, 'V7': -43.557, 'V8': -73.217, 'V9': -13.434, 'V10': -24.588,
              'V11': -4.797, 'V12': -18.684, 'V13': -5.792, 'V14': -19.214, 'V15': -4.499,
              'V16': -14.130, 'V17': -25.163, 'V18': -9.499, 'V19': -7.214, 'V20': -54.498,
              'V21': -34.830, 'V22': -10.933, 'V23': -44.808, 'V24': -2.837, 'V25': -10.295,
              'V26': -2.605, 'V27': -22.566, 'V28': -15.430, 'Amount': 0.0}

max_values = {'Time': 172792.000, 'V1': 2.455, 'V2': 22.058, 'V3': 9.383, 'V4': 16.875, 'V5': 34.802,
              'V6': 73.302, 'V7': 120.589, 'V8': 20.007, 'V9': 15.595, 'V10': 23.745,
              'V11': 12.019, 'V12': 7.848, 'V13': 7.127, 'V14': 10.527, 'V15': 8.878,
              'V16': 17.315, 'V17': 9.254, 'V18': 5.041, 'V19': 5.592, 'V20': 39.421,
              'V21': 27.203, 'V22': 10.503, 'V23': 22.528, 'V24': 4.585, 'V25': 7.520,
              'V26': 3.517, 'V27': 31.612, 'V28': 33.848, 'Amount': 25691.160}

# Inserting min and max values into number_input calls
Time = st.sidebar.number_input('Time', min_values['Time'], max_values['Time'], value=406.0)
V1 = st.sidebar.number_input('V1', min_values['V1'], max_values['V1'], value=-2.312)
V2 = st.sidebar.number_input('V2', min_values['V2'], max_values['V2'], value=1.952)
V3 = st.sidebar.number_input('V3', min_values['V3'], max_values['V3'], value=-1.610)
V4 = st.sidebar.number_input('V4', min_values['V4'], max_values['V4'], value=3.998)
V5 = st.sidebar.number_input('V5', min_values['V5'], max_values['V5'], value=-0.522)
V6 = st.sidebar.number_input('V6', min_values['V6'], max_values['V6'], value=-1.427)
V7 = st.sidebar.number_input('V7', min_values['V7'], max_values['V7'], value=-2.537)
V8 = st.sidebar.number_input('V8', min_values['V8'], max_values['V8'],  value=1.392)
V9 = st.sidebar.number_input('V9', min_values['V9'], max_values['V9'], value=-2.770)
V10 = st.sidebar.number_input('V10', min_values['V10'], max_values['V10'], value=-2.772)
V11 = st.sidebar.number_input('V11', min_values['V11'], max_values['V11'], value=3.202)
V12 = st.sidebar.number_input('V12', min_values['V12'], max_values['V12'], value=-2.900)
V13 = st.sidebar.number_input('V13', min_values['V13'], max_values['V13'], value=-0.595)
V14 = st.sidebar.number_input('V14', min_values['V14'], max_values['V14'], value=-4.289)
V15 = st.sidebar.number_input('V15', min_values['V15'], max_values['V15'], value=0.390)
V16 = st.sidebar.number_input('V16', min_values['V16'], max_values['V16'], value=-1.141)
V17 = st.sidebar.number_input('V17', min_values['V17'], max_values['V17'], value=-2.830)
V18 = st.sidebar.number_input('V18', min_values['V18'], max_values['V18'], value=-0.017)
V19 = st.sidebar.number_input('V19', min_values['V19'], max_values['V19'], value=0.417)
V20 = st.sidebar.number_input('V20', min_values['V20'], max_values['V20'], value=0.127)
V21 = st.sidebar.number_input('V21', min_values['V21'], max_values['V21'], value=0.517)
V22 = st.sidebar.number_input('V22', min_values['V22'], max_values['V22'], value=-0.035)
V23 = st.sidebar.number_input('V23', min_values['V23'], max_values['V23'], value=-0.465)
V24 = st.sidebar.number_input('V24', min_values['V24'], max_values['V24'], value=0.320)
V25 = st.sidebar.number_input('V25', min_values['V25'], max_values['V25'], value=0.045)
V26 = st.sidebar.number_input('V26', min_values['V26'], max_values['V26'], value=0.178)
V27 = st.sidebar.number_input('V27', min_values['V27'], max_values['V27'], value=0.261)
V28 = st.sidebar.number_input('V28', min_values['V28'], max_values['V28'], value=-0.143)
Amount = st.sidebar.number_input('Amount', min_values['Amount'], max_values['Amount'], value=0.0)


user_input = {
    'Time': Time,
    'V1': V1,
    'V2': V2,
    'V3': V3,
    'V4': V4,
    'V5': V5,
    'V6': V6,
    'V7': V7,
    'V8': V8,
    'V9': V9,
    'V10': V10,
    'V11': V11,
    'V12': V12,
    'V13': V13,
    'V14': V14,
    'V15': V15,
    'V16': V16,
    'V17': V17,
    'V18': V18,
    'V19': V19,
    'V20': V20,
    'V21': V21,
    'V22': V22,
    'V23': V23,
    'V24': V24,
    'V25': V25,
    'V26': V26,
    'V27': V27,
    'V28': V28,
    'Amount': Amount
}

# Creating a DataFrame from user input
user_input_df = pd.DataFrame([user_input])

# Displaying the DataFrame
st.write("User Input:")
st.write(user_input_df)



button_styles = """
    <style>
        div.stButton > button {
            background-color: #3498db;  /* Set your desired background color */
            color: #ffffff;             /* Set your desired text color */
        }
    </style>
"""

# Display the button with custom styles
st.markdown(button_styles, unsafe_allow_html=True)

predict = st.button('Predict the transaction')

model = joblib.load('final_model.joblib')

if predict:
    if model.predict(user_input_df)[0]==1:
        st.error('Fraud detected!',icon="🚨")
    else:
       
        st.success('The transaction is normal!',icon="✅")
    


