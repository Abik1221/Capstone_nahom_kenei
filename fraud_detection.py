import streamlit as st
import pandas as pd 
import joblib

model = joblib.load("fraud_detection_pipline.pkl")

st.title("fraud detection pridiction app")

st.markdawn("please enter the transaction details and use the predict button ")

st.divider()

transaction_type = st.selectbox("TRANASCTION TYPE", ["PAYMENT, TRANSFER", "CASH_OUT", "DEPOSITE"])

amount = st.number_input("Amount", min_value = 0.0, value = 1000.0)

oldbalanceOrg = st.number_input("Old balance (Sender)", min_value = 0.0, value = 1000.0)
newbalanceOrig = st.number_input("New balance (Sender)", min_value = 0.0, value = 9000.0)
oldbalanceDest = st.number_input("Old balance (Reciever)", min_value = 0.0, value = 0.0)
newbalanceDest = st.number_input("New balance (Reciever)", min_value = 0.0, value = 0.0)

if st.button("predict"):
   input_data = pd.DataFrame([{
       "type" : transaction_type,
       "amount" : amount,
       "oldbalanceOrg": oldbalanceOrg,
       "newbalaneceOrig" : newbalanceOrig,
       "oldbalanceDest": oldbalanceDest,
       "newbalanceDest": newbalanceDest
   }])
   
   pridiction = model.predict(input_data)[0]
   
   st.subheader (f"pridiction : '{int(pridiction)}'")
   
   if pridiction == 1:
       st.error("this transaction can be fraud")
   else:
       st.sucess("this transaction is not fraud")
       