import streamlit as st
from database import *


def cu_create():
    col1, col2, col3 = st.columns(3)
    with col1:
        c_id = st.number_input("Customer ID: ",min_value = 2000, max_value = 2999)
        cf_name = st.text_input("First Name: ")
        cl_name = st.text_input("Last Name: ")
        c_qual = st.text_input("Qualification: ")
        c_phone = st.text_input("Phone: ")
        b_bank = st.text_input("Bank: ")

    with col2:
        c_address = st.text_input("Address: ")
        c_locate = st.text_input("Locality: ")
        c_city = st.text_input("City: ")
        c_email = st.text_input("Email: ")
        c.execute("SELECT E_ID FROM Employee")
        emp_data = c.fetchall()
        e_data = []
        for i in emp_data:
            for j in i:
                e_data.append(int(j))
        c_emp = st.selectbox("Serving Employee", e_data)
        b_tid = st.text_input("Transaction ID: ")
        b_id = c_id + 7000
    
    with col3:
        c.execute("SELECT Item_ID FROM Items")
        data = c.fetchall()
        item_data = []
        for i in data:
            for j in i:
                item_data.append(int(j))
        c_item_id = st.selectbox("Item", item_data)
        c.execute("SELECT Item_Name,Brand,Size FROM Item_Category WHERE Item_ID ={}".format(c_item_id))
        it_n = c.fetchall()
        in_data = []
        for i in it_n:
            for j in i:
                in_data.append((j))
        in_data = in_data[0] + " :: "+in_data[1] + " :: " + in_data[2]
        st.write("Item Name :: Item Brand :: Item Size")
        st.markdown('`{}`'.format(in_data))

        c_qty = st.number_input("Quantity: ",min_value=1, max_value=50)
        c.execute("SELECT Price FROM Items WHERE Item_ID = {}".format(c_item_id))
        it_da = c.fetchall()
        price_data = []
        for i in it_da:
            for j in i:
                price_data.append(float(j))
        c_price = price_data[0]
        st.markdown("Price: ")
        st.write(c_price)
        c_dop = st.date_input("Purchase Date:")
        st.write("Total item order value")
        c_total = st.write(c_price * c_qty)
        c_total = c_price * c_qty
    
    c.execute("SELECT sum(O.O_Amount) AS Total_Bill FROM ORDERS AS O WHERE O.C_ID = {} ORDER BY sum(O.O_Amount) DESC".format(c_id))
    b_amt = c.fetchall()
    price_data = []
    for i in b_amt:
            for j in i:
                price_data.append((j))
    b_amount = price_data[0]
    with col3:
        st.markdown("Total Bill Amount: ")
        st.write(b_amount)

    with col1:
        if st.button("Add CUSTOMER"):
                cu_add_data(c_id,cf_name,cl_name,c_qual,c_address,c_locate,c_city,c_email,c_phone,c_dop,c_emp)
                st.success("Successfully added CUSTOMER: {}".format(cf_name))
    with col2:
        if st.button("Add ORDERS"):
                cu_orders_add_data(c_id,c_item_id,c_price,c_qty,c_dop,c_total)
                st.success("Successfully added ORDERS: {}".format(c_item_id))
    
    if st.button("GENERATE BILL"):
        cu_bill(b_id,b_bank,c_dop,b_tid,b_amount,c_id)
        st.success("Successfully generated BILL :: {}".format(b_id))
        view_bill(c_id)
        st.success("Successfully printed BILL :: {}".format(b_id))

#############################################################################################################

def em_create():
    col1, col2 = st.columns(2)
    with col1:
        e_id = st.number_input("Employee ID: ",min_value = 1000,max_value = 1999)
        e_fn = st.text_input("First Name: ")
        e_ln = st.text_input("Last Name: ")
        e_address = st.text_input("Address: ")
        e_phone = st.text_input("Phone: ")
    with col2:
        c.execute("SELECT DISTINCT MGR_ID FROM EMPLOYEE WHERE MGR_ID <> 0")
        data = c.fetchall()
        mgr_data = []
        for i in data:
            for j in i:
                mgr_data.append(int(j))
        emgr_id = st.selectbox("Manager", mgr_data)
        e_gender = st.radio("Gender",('M', 'F'))
        e_salary = st.number_input("Salary: ")
        e_dob = st.date_input("Date of Birth:")
    
    if st.button("Add Employee"):
        em_add_data(e_id,e_fn,e_ln,emgr_id,e_gender,e_salary,e_dob,e_address,e_phone)
        st.success("Successfully added EMPLOYEE: {}".format(e_fn))

#############################################################################################################

def it_create():
    col1, col2, col3 = st.columns(3)
    with col1:
        i_id = st.number_input("ITEM ID: ",min_value = 4000,max_value = 4999)
        i_name = st.text_input("Name: ")
        i_price = st.number_input("Price: ")
        
    with col2:
        i_brand = st.text_input("Brand: ")
        i_colour = st.text_input("Colour: ")
        i_size = st.selectbox("Size", ["NA","28","30","32","34","36","38","40","42","44","46","48","50","52","54","56","58","60","M","L","XL","XXL","XXXL"])
    with col3:
        i_gender = st.radio("Gender",('M', 'F'))
        i_quantity = st.number_input("Quantity: ",min_value = 1, max_value = 50)
        c.execute("SELECT STORE_ID FROM STORE")
        data = c.fetchall()
        store_data = []
        for i in data:
            for j in i:
                store_data.append(int(j))
        st_id = st.selectbox("STORE-ID",store_data)

    
    if st.button("Add ITEM-STOCK"):
        it_add_data(i_id,i_name,i_price,i_gender,i_brand,i_colour,i_size,i_quantity,st_id)
        st.success("Successfully added ITEM TO STORE: {}".format(i_id))

    
#############################################################################################################

def su_create():
    col1, col2 = st.columns(2)
    with col1:
        su_id = st.number_input("Supplier ID: ",min_value = 7000,max_value = 7999)
        su_name = st.text_input("Name: ")
        su_address = st.text_input("Address: ")
        c.execute("SELECT STORE_ID FROM STORE")
        data = c.fetchall()
        store_data = []
        for i in data:
            for j in i:
                store_data.append(int(j))

        su_st_id = st.selectbox("STORE-ID",store_data)
    with col2:
        sh_id = st.number_input("Ship ID: ",min_value = 8000,max_value = 8999)
        sh_cost = st.number_input("Shipping Cost: ")
        sh_date = st.date_input("Date of Shipment: ")
        sh_mode = st.selectbox("Mode of Travel", ["Roadways","Railways","Airways","Waterways"])

        
    
    if st.button("Add SUPPLIER - SHIP"):
        su_add_data(su_id,su_name,su_address,sh_id,sh_cost,sh_mode,sh_date,su_st_id)
        st.success("Successfully added SUPPLIER-SHIP: {}".format(su_name))

#############################################################################################################


    