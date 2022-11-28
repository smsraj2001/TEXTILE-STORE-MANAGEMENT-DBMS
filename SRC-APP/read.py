import pandas as pd
import streamlit as st
import plotly.express as px
from database import *


def cu_read():
    result = cu_view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns = ['C_ID', 'First_Name','Last Name','Qualification','Address','Locality','City','Email','Phone_NO','DOP','E_ID','Order_C_ID','Item_ID','Price','Quantity','O_Date','O_Amount'])
    with st.expander("View all Customers"):
        st.dataframe(df)
    with st.expander("Name"):
        task_df = df['First_Name'].value_counts().to_frame()
        task_df = task_df.reset_index()
        task_df.columns = ['First_Name', 'Count']
        st.dataframe(task_df)
        p1 = px.pie(task_df, names = 'First_Name', values = 'Count')
        st.plotly_chart(p1)        

#############################################################################################################

def em_read():
    result = em_view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns = ['E_ID', 'First_Name','Last_Name','MGR_ID','GENDER','SALARY','DOB','ADDRESS','Phone_NO'])
    with st.expander("View all Employees"):
        st.dataframe(df)
    with st.expander("First_Name"):
        task_df = df['First_Name'].value_counts().to_frame()
        task_df = task_df.reset_index()
        task_df.columns = ['First_Name', 'Count']
        st.dataframe(task_df)
        p1 = px.pie(task_df, names = 'First_Name', values = 'Count')
        st.plotly_chart(p1)

#############################################################################################################

def it_read():
    result = it_view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns = ['Item_ID', 'Item_Name','Gender','Brand','Colour','Size','Quantity','Store_ID','Store_Name'])
    with st.expander("View all Items with their stores"):
        st.dataframe(df)
    with st.expander("Item_ID"):
        task_df = df[['Item_ID','Quantity']].value_counts().to_frame()
        task_df = task_df.reset_index()
        task_df.columns = ['Item_ID', 'Quantity', 'Index']
        st.dataframe(task_df)
        p1 = px.pie(task_df, names = 'Item_ID', values = 'Quantity')
        st.plotly_chart(p1)

#############################################################################################################

def su_read():
    result = su_view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns = ['Supp_ID','Name','Address','Ship_ID','Cost_of_shipping','Mode_of_Travelling','Date_Of_Shipment','Store_ID'])
    with st.expander("View all Suppliers and Ships"):
        st.dataframe(df)
    with st.expander("Name"):
        task_df = df['Name'].value_counts().to_frame()
        task_df = task_df.reset_index()
        task_df.columns = ['Supplier_Name', 'Count']
        st.dataframe(task_df)
        p1 = px.pie(task_df, names = 'Supplier_Name', values = 'Count')
        st.plotly_chart(p1)

#############################################################################################################
