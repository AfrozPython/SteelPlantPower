# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 00:32:05 2023

@author: Appu
"""

import pandas as pd
import numpy as np
import pickle
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt 
from streamlit_option_menu import option_menu

st.set_option('deprecation.showPyplotGlobalUse', False)


# loading in the model to predict on the data
loaded_model = pickle.load(open('df.sav', 'rb'))


# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Steel Plant Load Prediction',
                           ['Introduction  to Steel Plant Load Prediction','Basic EDA','Steel Plant Load Prediction'],
                           icons=['book','kanban','laptop'],
                           default_index=0)
#--------------------------------------------------------------- PAGE  1 -------------------------------------------------------#                       
    
if (selected == 'Introduction  to Steel Plant Load Prediction'):
    

    
    image = open('image.jpg',"rb")
    image = image.read()
    st.image(image,width=1100)

    
    html_temp = """
    <div style ="background-color:white;padding:13px">
    <h1 style ="color:black;text-align:center;font-family:Comic Sans MS; color:Brown; font-size: 34px;">Why should the Steel Companies be worried about the power factor and Lagging Current </h1>
    </div>
    """  
    # this line allows us to display the front end aspects we have 
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)
    
    
    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:left;font-family:Viner Hand ITC; color:#716807; font-size: 28px;">The objectives of this project is to predict the load and  What patterns can we identify in energy usage? </h1>
    </div>
    """  
    # this line allows us to display the front end aspects we have    application information for power-factor problems. The effects of low plant operating power factor could be very bad.
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)
    
    
    title = '<p style="font-family:Lucida Calligraphy;text-align: left; color:Brown; font-size: 28px;">1. Low power factor effect on steel industry</p>'
    st.markdown(title, unsafe_allow_html=True)
    
    
    col1, col2 = st.columns(2)

    with col1:
        st.write("A low power factor can have a number of negative effects on the steel industry. One of the main effects is that it can increase "
                 "the amount of energy required to produce a given amount of steel. This can increase the cost of production "
                 "for steel manufacturers, which can ultimately lead to higher prices for consumers."
                 "Additionally, Low power factor also causes additional loss in transmission and distribution lines. Furthermore,low power factor can cause equipment")

    with col2:
        st.write("low power factor can cause equipment and devices in the steel manufacturing process to work less efficiently, which can lead to additional wear and tear and increase maintenance costs."
                 "Therefore, many steel manufacturers invest in power factor correction equipment to improve power factor and reduce energy costs. "
                 " This equipment helps to improve the efficiency of the manufacturing process and reduce costs associated with low power factor.")
        #--------------------------------------------------------------------------------------------------------------------------------------
        
    title = '<p style="font-family:Lucida Calligraphy;text-align: left; color:Brown; font-size: 28px;">2. Lagging Current reactive power Continuous kVarh  effect on steel industry</p>'
    st.markdown(title, unsafe_allow_html=True)
        
    col1, col2 = st.columns(2)

    with col1:
        st.write("Lagging current, which is caused by inductive loads in the steel manufacturing process, can have a number of negative effects on the steel industry. "
                 "One of the main effects is that it can increase the amount of energy required to produce a given amount of steel, because inductive loads "
                 "consume reactive power which doesn't do any useful work but just circulate between the source and load."
                 "This can increase the cost of production for steel manufacturers, which can ultimately lead to higher prices for consumers."
                 "Furthermore, continuous kvarh consumption leads to higher costs for utilities, which may charge customers based on their consumption of reactive power. This can increase the overall")

    with col2:
        st.write(" operating costs for steel manufacturers,"
                 "which may have to pass on some of these costs to their customers in the form of higher prices.Additionally, lagging current can cause equipment and devices in the steel manufacturing "
                 "process to work less efficiently, due to the increased power loss caused by inductive loads. This can lead to additional wear and tear on equipment and increase maintenance costs. ."
                 "Therefore, steel manufacturers invest in power factor correction equipment to improve power factor and reduce energy costs."
                 "This equipment helps to improve the efficiency of the manufacturing process and reduce costs associated with lagging current and continuous kvarh consumption.")
        
    image = open('image1.png',"rb")
    image = image.read()
    st.image(image,width=1000)
    
    image = open('image2.jpg',"rb")
    image = image.read()
    st.image(image,width=1000)




#--------------------------------------------------------------- PAGE  2 -------------------------------------------------------#

# Diabetes Prediction Page
if (selected == 'Basic EDA'):
    
    html_temp = """
    <div style ="background-color:white;padding:13px">
    <h1 style ="color:black;text-align:center;font-family:Lucida Calligraphy; color:Brown; font-size: 40px;">EDA of Steel Plant Electrical Data set</h1>
    </div>
    """  
    # this line allows us to display the front end aspects we have 
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)

    
    # Import Data
    title = '<p style="font-family:Lucida Calligraphy;text-align: Center; color:Red; font-size: 34px;">Scatter plot of Steel Plant data set</p>'
    st.markdown(title, unsafe_allow_html=True)
    
    selected_x_var = st.selectbox('What do want the x variable to be?', 
      ['Usage_kWh','Lagging_Current_Reactive.Power_kVarh','Leading_Current_Reactive_Power_kVarh','CO2(tCO2)','Lagging_Current_Power_Factor','Leading_Current_Power_Factor','NSM'
]) 
    selected_y_var = st.selectbox('What about the y?', 
      ['Lagging_Current_Reactive.Power_kVarh','Usage_kWh','Leading_Current_Reactive_Power_kVarh','CO2(tCO2)','Lagging_Current_Power_Factor','Leading_Current_Power_Factor','NSM'
]) 


    Steel = pd.read_csv('C:/Users/Appu/Desktop/Streamlit Test/Best Code Streamlit/Z Test Programs/01.Steel Industry Load Prediction/Steel_industry_data.csv')
    
    # Scatter Plot
    
    
    sns.set_style('darkgrid')
    markers = {"Light_Load": "X", "Medium_Load": "s", "Maximum_Load":'o'}
    fig, ax = plt.subplots() 
    ax = sns.scatterplot(data = Steel, x = selected_x_var, 
      y = selected_y_var, hue = 'Load_Type', markers = markers,
      style = 'Load_Type') 
    plt.xlabel(selected_x_var) 
    plt.ylabel(selected_y_var) 
    plt.title("Scatterplot of Steel Plant load") 
    st.pyplot(fig) 
    
    # Load Data
    if st.checkbox("For Vewing Data Please Check this Box"):
        st.dataframe(Steel.head())
    # Descrobe   
    if st.checkbox("Show Summary of Dataset"):
        st.write(Steel.describe())
        
        
    title = '<p style="font-family:Lucida Calligraphy;text-align: Center; color:Red; font-size: 34px;">Count Plot of Load type</p>'
    st.markdown(title, unsafe_allow_html=True)
        
    # Count Plot
    
    st.write(sns.countplot(Steel['Load_Type']))
    	# Use Matplotlib to render seaborn
    st.pyplot()
    
    
    
    title = '<p style="font-family:Lucida Calligraphy;text-align: Center; color:Red; font-size: 34px;">Show Correlation Plots </p>'
    st.markdown(title, unsafe_allow_html=True)
    
    # Correlation
    st.write(sns.heatmap(Steel.corr(),annot=True,cmap='copper'));
    st.pyplot()
    
    

#--------------------------------------------------------------- PAGE  3 -------------------------------------------------------#

if (selected == 'Steel Plant Load Prediction'):
    
    
    
    
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:pink;padding:13px">
    <h1 style ="color:black;text-align:center;font-family:Lucida Calligraphy; color:Brown; font-size: 30px;">Steel Plant Load Prediction With Artificial Intelligence</h1>
    </div>
    """  
    # this line allows us to display the front end aspects we have 
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)
    
    # Usage_kWh
    if st.checkbox("Show/Hide (Usage_KWH Range)"):
        title = '<p style="font-family:Times New Roman;text-align: justify; color:Blue; font-size: 24px;">Usage_kWh Industry Energy Consumption Continuous kWh .(Minimum Value 0 & Maximum Value 160)</p>'
        st.markdown(title, unsafe_allow_html=True)
    
    Usage_kWh = st.number_input('Usage_KWH')
    
    # Lagging_Reactive_Power_kVar
    if st.checkbox("Show/Hide (Lagging_Reactive_Power_kVarh)"):
        title = '<p style="font-family:Times New Roman;text-align: justify; color:Blue; font-size: 24px;">Lagging Current reactive power Continuous kVarh .(Minimum Value 0 & Maximum Value 97)</p>'
        st.markdown(title, unsafe_allow_html=True)
    Lagging_Reactive_Power_kVarh = st.number_input("Lagging_Reactive_Power_kVarh")
    
    
    # Leading_Reactive_Power_kVarh
    if st.checkbox("Show/Hide (Leading_Reactive_Power_kVarh)"):
        title = '<p style="font-family:Times New Roman;text-align: justify; color:Blue; font-size: 24px;">Leading Current reactive power Continuous kVarh .(Minimum Value 0 & Maximum Value 28)</p>'
        st.markdown(title, unsafe_allow_html=True)
    Leading_Reactive_Power_kVarh = st.number_input("Leading_Reactive_Power_kVarh")
    
    # CO2
    if st.checkbox("Show/Hide (CO2)"):
        title = '<p style="font-family:Times New Roman;text-align: justify; color:Blue; font-size: 24px;">CO2 Continuous ppm .(Minimum Value 0.00 & Maximum Value 0.07)</p>'
        st.markdown(title, unsafe_allow_html=True)
    CO2 = st.number_input("CO2")
    
    # Lagging_Power_Factor
    if st.checkbox("Show/Hide (Lagging_Current_Power_Factor)"):
        title = '<p style="font-family:Times New Roman;text-align: justify; color:Blue; font-size: 24px;">Lagging_Current_Power_Factor(Minimum Value 0.00 & Maximum Value 100)</p>'
        st.markdown(title, unsafe_allow_html=True)
             
    Lagging_Power_Factor = st.number_input("Lagging_Power_Factor")
    
    # Leading_Current_Power_Factor
    if st.checkbox("Show/Hide (Leading_Current_Power_Factor)"):
        title = '<p style="font-family:Times New Roman;text-align: justify; color:Blue; font-size: 24px;">Lagging_Current_Power_Factor(Minimum Value 0.00 & Maximum Value 100)</p>'
        st.markdown(title, unsafe_allow_html=True)
    Leading_Power_Factor = st.number_input("Leading_Power_Factor")
    
    # Leading_Current_Power_Factor
    if st.checkbox("Show/Hide (NSM)"):
        title = '<p style="font-family:Times New Roman;text-align: justify; color:Blue; font-size: 24px;">NSM Number of Seconds from midnight Continuous S(Minimum Value 900 & Maximum Value 85500 @ with the increment of each step with +900 for ex: 900 ,1800, 2700 ,3600)</p>'
        st.markdown(title, unsafe_allow_html=True)
        
    NSM = st.number_input("NSM")
    
    # WeekStatus
    if st.checkbox("Show/Hide (WeekStatus)"):
        title = '<p style="font-family:Times New Roman;text-align: justify; color:Blue; font-size: 24px;">Week status Categorical (Weekend (0) or a Weekday(1))</p>'
        st.markdown(title, unsafe_allow_html=True)
        
    WeekStatus = st.number_input("WeekStatus")
    
    # Day_of_week
    if st.checkbox("Show/Hide (Day_of_week)"):
        title = '<p style="font-family:Times New Roman;text-align: justify; color:Blue; font-size: 24px;">Day of week Categorical Sunday, Monday : Saturday(from 0 to 7)</p>'
        st.markdown(title, unsafe_allow_html=True)
    Day_of_week = st.number_input("Day_of_week")
    
    
    
    # code for Prediction
    load = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        load_prediction = loaded_model.predict([[Usage_kWh, Lagging_Reactive_Power_kVarh, Leading_Reactive_Power_kVarh, CO2, Lagging_Power_Factor, Leading_Power_Factor, NSM, WeekStatus, Day_of_week]])

        if (load_prediction[0] == 0):
            load = 'Light Load'
        elif (load_prediction[0] == 1):
            load = 'Medium Load'
        else:
            load = 'Maximum Load'
        
    st.success(load)
        
                          



