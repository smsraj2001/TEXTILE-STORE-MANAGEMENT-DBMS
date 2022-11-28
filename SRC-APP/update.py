import datetime
import pandas as pd
import streamlit as st
from database import *


def cu_update():
    result = cu_view_cust_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['C_ID', 'First_Name','Last Name','Qualification','Address','Locality','City','Email','Phone_NO'])
    with st.expander("Current Customers"):
        st.dataframe(df)
    list_of_customers = [i[0] for i in cu_view_only()]
    selected_cus = st.selectbox("Customer to Edit", list_of_customers)
    selected_result = cu_get(selected_cus)
    # st.write(selected_result)
    if selected_result:
        c_id = selected_result[0][0]
        c_fn = selected_result[0][1]
        c_ln = selected_result[0][2]
        c_qual = selected_result[0][3]
        c_address = selected_result[0][4]
        c_locate = selected_result[0][5]
        c_city = selected_result[0][6]
        c_email = selected_result[0][7]
        c_phone = selected_result[0][8]


        # Layout of Create

    col1, col2 = st.columns(2)
    with col1:
        new_c_id = st.number_input("Customer ID: ",max_value = 2999,value = c_id)
        new_c_fn = st.text_input("First Name: ",value = c_fn)
        new_c_ln = st.text_input("Last Name: ",value = c_ln)
        new_c_qual = st.text_input("Qualification: ",value = c_qual)
        new_c_phone = st.text_input("Phone: ",value = c_phone)

    with col2:
        new_c_address = st.text_input("Address: ",value = c_address)
        new_c_locate = st.text_input("Locality: ",value = c_locate)
        new_c_city = st.text_input("City: ",value = c_city)
        new_c_email = st.text_input("Email: ",value = c_email)
        st.markdown("\n")
        st.markdown("\n")
        
        if st.button("Update Customer Details"):
            cu_edit(new_c_id,new_c_fn,new_c_ln,new_c_qual, new_c_address, new_c_locate, new_c_city, new_c_email,new_c_phone,c_id,c_fn,c_ln, c_qual, c_address, c_locate, c_city, c_email,c_phone)
            st.success("Successfully updated:: {} to :: {} and other details".format(c_fn, new_c_fn))

    result2 = cu_view_all_data()
    df2 = pd.DataFrame(result2, columns = ['C_ID', 'First_Name','Last Name','Qualification','Address','Locality','City','Email','Phone_NO','DOP','E_ID','Order_C_ID','Item_ID','Price','Quantity','O_Date','O_Amount'])
    with st.expander("Updated Data"):
        st.dataframe(df2)

#############################################################################################################

def em_update():
    result = em_view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns = ['E_ID', 'First_Name','Last_Name','MGR_ID','GENDER','SALARY','DOB','ADDRESS','Phone_NO'])
    with st.expander("Current Employees"):
        st.dataframe(df)
    list_of_trains = [i[0] for i in em_view_only()]
    selected_train = st.selectbox("Employee name to Edit", list_of_trains)
    selected_result = em_get(selected_train)
    # st.write(selected_result)
    if selected_result:
        e_id = selected_result[0][0]
        e_fn = selected_result[0][1]
        e_ln = selected_result[0][2]
        emgr_id = selected_result[0][3]
        e_gender = selected_result[0][4]
        e_salary = selected_result[0][5]
        e_dob = selected_result[0][6]
        e_address = selected_result[0][7]
        e_phone = selected_result[0][8]

        # Layout of Create

        col1, col2 = st.columns(2)
    with col1:
        new_e_id = st.number_input("Employee ID: ",min_value = 1000, max_value = 1999,value = e_id)
        new_e_fn = st.text_input("First Name: ",value = e_fn)
        new_e_ln = st.text_input("Last Name: ",value = e_ln)
        new_e_address = st.text_input("Address: ",value = e_address)
        new_e_phone = st.text_input("Phone: ",value = e_phone)
    with col2:
        c.execute("SELECT DISTINCT MGR_ID FROM EMPLOYEE WHERE MGR_ID <> 0")
        data = c.fetchall()
        mgr_data = []
        for i in data:
            for j in i:
                mgr_data.append(int(j))
        new_emgr_id = st.selectbox("Manager", mgr_data)
        new_e_gender = st.radio("Gender",('M', 'F'))
        new_e_salary = st.number_input("Salary: ",value = e_salary)
        new_e_dob = st.date_input("Date of Birth:",value = e_dob)
        st.markdown("\n")

        if st.button("Update Employee"):
            em_edit(new_e_id,new_e_fn,new_e_ln,new_emgr_id,new_e_gender,new_e_salary,new_e_dob,new_e_address,new_e_phone,e_id,e_fn,e_ln,emgr_id,e_gender,e_salary,e_dob,e_address,e_phone)
            st.success("Successfully updated :: {} to :: {} and other details".format(e_fn, new_e_fn))

    result2 = em_view_all_data()
    df2 = pd.DataFrame(result2, columns = ['E_ID', 'First_Name','Last_Name','MGR_ID','GENDER','SALARY','DOB','ADDRESS','Phone_NO'])
    with st.expander("Updated Data"):
        st.dataframe(df2)

#############################################################################################################

def it_update():
    result = it_view_only()
    # st.write(result)
    df = pd.DataFrame(result, columns = ['Item_ID', 'Item_Name','Price','Gender','Brand','Colour','Size','Quantity','Store_ID'])
    with st.expander("Current Items in Stores"):
        st.dataframe(df)
    list_of_trains = [i[0] for i in it_view_only()]
    selected_train = st.selectbox("Items in Store to Edit", list_of_trains)
    selected_result = it_get(selected_train)
    # st.write(selected_result)
    if selected_result:
        i_id = selected_result[0][0]
        i_name = selected_result[0][1]
        i_price = selected_result[0][2]
        i_gender = selected_result[0][3]
        i_brand = selected_result[0][4]
        i_colour = selected_result[0][5]
        i_size = selected_result[0][6]
        i_quantity = selected_result[0][7]
        st_id = selected_result[0][8]


        # Layout of Create

        col1, col2, col3 = st.columns(3)
    with col1:
        new_i_id = st.number_input("ITEM ID: ",min_value = 4000,max_value = 4999,value = i_id)
        new_i_name = st.text_input("Name: ",value = i_name)
        new_i_price = st.number_input("Price: ",value = i_price)
        
    with col2:
        new_i_brand = st.text_input("Brand: ",value = i_brand)
        new_i_colour = st.text_input("Colour: ",value = i_colour)
        new_i_size = st.selectbox("Size", ["NA","28","30","32","34","36","38","40","42","44","46","48","50","52","54","56","58","60","M","L","XL","XXL","XXXL"])
    
    with col3:
        new_i_gender = st.radio("Gender",('M', 'F'))
        new_i_quantity = st.number_input("Quantity: ",min_value = 1, max_value = 50,value = i_quantity)
        new_st_id = st.selectbox("STORE-ID",[6001,6002,6003,6004])

    with col1:
        if st.button("Update Item in Store"):
            it_edit(new_i_id,new_i_name,new_i_price,new_i_brand,new_i_colour,new_i_size,new_i_gender,new_i_quantity,new_st_id,i_id,i_name,i_price,i_brand,i_colour,i_size,i_gender,i_quantity,st_id)
            st.success("Successfully updated :: {} to :: {} and other details".format(i_name, new_i_name))

    result2 = it_view_all_data()
    df2 = pd.DataFrame(result2, columns = ['Item_ID', 'Item_Name','Price','Gender','Brand','Colour','Size','Quantity','Store_ID'])
    with st.expander("Updated Data"):
        st.dataframe(df2)

#############################################################################################################

def su_update():
    result = su_view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns = ['Supp_ID','Name','Address','Ship_ID','Cost_of_shipping','Mode_of_Travelling','Date_Of_Shipment','Store_ID'])
    with st.expander("Current Suppliers and Shipping Details"):
        st.dataframe(df)
    list_of_sup = [i[0] for i in su_view_only()]
    selected_sup = st.selectbox("Supplier/Ship to Edit", list_of_sup)
    selected_result = su_get(selected_sup)
    # st.write(selected_result)
    if selected_result:
        su_id = selected_result[0][0]
        su_name = selected_result[0][1]
        su_address = selected_result[0][2]
        sh_id = selected_result[0][3]
        sh_cost = selected_result[0][4]
        sh_mode = selected_result[0][5]
        sh_date = selected_result[0][6]
        su_st_id = selected_result[0][7]

        # Layout of Create

        col1, col2 = st.columns(2)
    with col1:
        new_su_id = st.number_input("Supplier ID: ",min_value = 7000,max_value = 7999,value = su_id)
        new_su_name = st.text_input("Name: ",value = su_name)
        new_su_address = st.text_input("Address: ",value = su_address)
        c.execute("SELECT STORE_ID FROM STORE")
        data = c.fetchall()
        store_data = []
        for i in data:
            for j in i:
                #j = j.replace(",","")
                store_data.append(int(j))

        new_su_st_id = st.selectbox("STORE-ID",store_data)

    with col2:
        new_sh_id = st.number_input("Ship ID: ",min_value = 8000,max_value = 8999,value = sh_id)
        new_sh_cost = st.number_input("Shipping Cost: ",value = sh_cost)
        new_sh_date = st.date_input("Date of Shipment: ",value = sh_date)
        new_sh_mode = st.selectbox("Mode of Travel", ["Roadways","Railways","Airways","Waterways"])

    with col1:
        if st.button("Update SUPPLIER - SHIP"):
            su_edit(new_su_id,new_su_name,new_su_address,new_sh_id,new_sh_cost,new_sh_mode,new_sh_date,new_su_st_id,su_id,su_name,su_address,sh_id,sh_cost,sh_mode,sh_date,su_st_id)
            st.success("Successfully updated :: {} to :: {} and other details".format(su_name, new_su_name))

    result2 = su_view_all_data()
    df2 = pd.DataFrame(result2, columns = ['Supp_ID','Name','Address','Ship_ID','Cost_of_shipping','Mode_of_Travelling','Date_Of_Shipment','Store_ID'])
    with st.expander("Updated Data"):
        st.dataframe(df2)

#############################################################################################################
