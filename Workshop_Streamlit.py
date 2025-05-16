#Workoshop Streamlit
#EXERCICE 1 
import streamlit as st
st.title("Eexercice 1 : BMI Calculator ")
st.write("Enter your weight and height to calculate your BMI")
weight=st.number_input("Weight")
status=st.radio("Select Unité:",('cm','m','ft'))
if(status=='cm'):
    height=st.number_input("Height (cm)")
elif (status=='m'):
    height=st.number_input("Height (m)")
else:
    height=st.number_input("Height (ft)")





def calcul_BMI(weight,height,status):
    if status=='cm':
        bmi=weight/((height/100)**2)
    elif status=='m':
        bmi=weight/(height**2)
    else:
        bmi=weight/((height*0.3048)**2)
    if bmi<16:
        result=st.error("You are extremely Underweight")
    elif 16<=bmi<18.5:
        result=st.warning("You are Underweight")
    elif 18.5<=bmi<25:
        result=st.success("Healthy")
    elif 25<=bmi<30:
        result=st.warning("Overweight")
    else:
        result=st.error("Extremely Overweight")
    return bmi,result


if st.button("Calculate BMI"):
    bmi,result=calcul_BMI(weight,height,status)
    st.write(f"You BMI is :{bmi}")
    st.write(result)

'''
#EXERCICE2 : 
st.title("Eexercice 2 : Temperature Converter ")


conversion=st.selectbox("Select type de conversion","Celsus to Fahren","Fahren to Celsus")
if conversion=="Celsus to Fahren":
    celsus=st.number_input("Enter Temperature in Celsus")
    if st.button("Convertir"):
        fahren=(celsus*9/5)+32
        st.write(f"{celsus} C equivaut à {fahren} F")
else:
    conversion=="Fahren to Celsus"
    fahren=st.number_input("Enter Temperature in Fahren")
    if st.button("Convertir"):
        celsus=(fahren-32)*5/9
        st.write(f"{celsus} C equivaut à {fahren} F")


#EXERCICE 3 : 
st.title("Eexercice 3 : Iris Dataset ")
import streamlit as st 
import seaborn as sns
import matplotlib as plt 
import pandas as pd 
iris=sns.load_dataset("iris")
'''