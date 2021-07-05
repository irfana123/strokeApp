import numpy as np
import pickle
import pandas as pd
import streamlit as st 
 

 
# loading the trained model
f1 = open("stroke-model.pkl","rb") 
model = pickle.load(f1)


def welcome():
    return "WELCOME ALL"



def user_prediction(gender,age,
             hypertension,heart_disease,
             ever_married,work_type,
             Residence_type,avg_glucose_level,
             bmi,smoking_status):
    
    d = {"gender":gender,"age":age,
             "hypertension":hypertension,"heart_disease":heart_disease,
             "ever_married":ever_married,"work_type":work_type,
             "Residence_type":Residence_type,"avg_glucose_level":avg_glucose_level,
             "bmi":bmi,"smoking_status":smoking_status}
    data = pd.DataFrame(d,index=[0])

    pred = model.predict(data)

        #return pred

    if pred==1:
        score= " You will have stroke"
    else:
        score= " You wont have stroke"
    return score



# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    #st.title("Stroke Predictor")
    html_temp = """ 
    <div style ="background-color:pink;padding:15px"> 
    <h1 style ="color:black;text-align:center;">Stroke Prediction ML App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    gender = st.selectbox('GENDER',("Male","Female"))
    age=st.number_input("APPLICANT'S AGE")
    hypertension = st.selectbox('HYPERTENSION',("Yes","No")) 
    heart_disease = st.selectbox('HEART DISEASE',("Yes","No")) 
    ever_married = st.selectbox('MARITAL STATUS',("Yes","No")) 
    work_type=  st.selectbox('WORK TYPE STSTUS',("Govt_job" ,"Private","Self-employed"))                        
    Residence_type = st.selectbox('RESIDENCE TYPE STATUS',("Urban" ,"Rural"))  
    avg_glucose_level = st.number_input("AVERAGE GLUCOSE LEVEL")
    bmi = st.number_input("BMI")
    smoking_status = st.selectbox('SMOKING STATUS',("formerly smoked", "never smoked","smokes", "Unknown"))
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = user_prediction(gender,age,
             hypertension,heart_disease,
             ever_married,work_type,
             Residence_type,avg_glucose_level,
             bmi,smoking_status)
        st.success('Your result is {}'.format(result))
        #print(LoanAmount)
     
if __name__=='__main__': 
    main()
