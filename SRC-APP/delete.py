import pandas as pd
import streamlit as st
from database import *


def cu_delete():
    result = cu_view_cust_data()
    df = pd.DataFrame(result, columns = ['C_ID', 'First_Name','Last Name','Qualification','Address','Locality','City','Email','Phone_NO'])
    with st.expander("Current Data present"):
        st.dataframe(df)

    list_of_customers = [i[0] for i in cu_view_only()]
    selected_customers = st.selectbox("Customer to Delete", list_of_customers)
    st.warning("Do you want to delete :: {}".format(selected_customers))
    if st.button("Delete Customer"):
        cu_delete_data(selected_customers)
        st.success("Customer has been deleted successfully")
    new_result = cu_view_all_data()
    df2 = pd.DataFrame(new_result, columns = ['C_ID', 'First_Name','Last Name','Qualification','Address','Locality','City','Email','Phone_NO','DOP','E_ID','Order_C_ID','Item_ID','Price','Quantity','O_Date','O_Amount'])
    with st.expander("Updated data"):
        st.dataframe(df2)
    
    result2 = cu_read_delete()
    df = pd.DataFrame(result2, columns = ['C_ID', 'First_Name','Last Name','Qualification','Address','Locality','City','Email','Phone_NO','DOP','E_ID','Store_ID','Item_ID','Quantity','O_Amount'])
    with st.expander("History of Deleted Customers"):
        st.dataframe(df)

#############################################################################################################

def em_delete():
    result = em_view_all_data()
    df = pd.DataFrame(result, columns = ['E_ID', 'First_Name','Last_Name','MGR_ID','GENDER','SALARY','DOB','ADDRESS','Phone_NO'])
    with st.expander("Current Data present"):
        st.dataframe(df)

    list_of_emp = [i[0] for i in em_view_only()]
    selected_emp = st.selectbox("Employee to Delete", list_of_emp)
    st.warning("Do you want to delete :: {}".format(selected_emp))
    if st.button("Delete Employee"):
        em_delete_data(selected_emp)
        st.success("Employee has been deleted successfully")
    new_result = em_view_all_data()
    df2 = pd.DataFrame(new_result, columns = ['E_ID', 'First_Name','Last_Name','MGR_ID','GENDER','SALARY','DOB','ADDRESS','Phone_NO'])
    with st.expander("Updated data"):
        st.dataframe(df2)

#############################################################################################################

def it_delete():
    result = it_view_only()
    df = pd.DataFrame(result, columns = ['Item_ID', 'Item_Name','Price','Gender','Brand','Colour','Size','Quantity','Store_ID'])
    with st.expander("Current Data present"):
        st.dataframe(df)

    list_of_items = [i[0] for i in it_view_only()]
    selected_items = st.selectbox("Item to Delete", list_of_items)
    st.warning("Do you want to delete :: {}".format(selected_items))
    if st.button("Delete Item from Store"):
        it_delete_data(selected_items)
        st.success("Item in store has been deleted successfully")
    new_result = it_view_only()
    df2 = pd.DataFrame(new_result, columns = ['Item_ID', 'Item_Name','Price','Gender','Brand','Colour','Size','Quantity','Store_ID'])
    with st.expander("Updated data"):
        st.dataframe(df2)

#############################################################################################################

def su_delete():
    result = su_view_all_data()
    df = pd.DataFrame(result, columns = ['Supp_ID','Name','Address','Ship_ID','Cost_of_shipping','Mode_of_Travelling','Date_Of_Shipment','Store_ID'])
    with st.expander("Current Data present"):
        st.dataframe(df)

    list_of_sup = [i[0] for i in su_view_only()]
    selected_sup = st.selectbox("Supplier to Delete", list_of_sup)
    st.warning("Do you want to delete :: {}".format(selected_sup))
    if st.button("Delete Supplier"):
        su_delete_data(selected_sup)
        st.success("Supplier has been deleted successfully")
    new_result = su_view_all_data()
    df2 = pd.DataFrame(new_result, columns = ['Supp_ID','Name','Address','Ship_ID','Cost_of_shipping','Mode_of_Travelling','Date_Of_Shipment','Store_ID'])
    with st.expander("Updated data"):
        st.dataframe(df2)

#############################################################################################################
