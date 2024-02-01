# Importing pakages
import streamlit as st
import mysql.connector

from create import *
from database import *
from delete import *
from read import *
from update import *

def main():
    st.set_page_config(
    page_title = "Textile 362",
    # page_icon = "🧊",
    layout = "wide",
    initial_sidebar_state = "expanded",
    )
    # st.snow()
    # st.balloons()
    st.image('./Header.png')
    st.sidebar.image("Fashion.png")
    st.title("SMS TEXTILE STORES - 362")
    #st.write("------------------------------------------------------")
    menu = ["ADD", "VIEW", "EDIT", "REMOVE"]
    st.sidebar.header("MENU")
    
    ch = st.sidebar.selectbox("OPTIONS",["CUSTOMER","EMPLOYEE","ITEMS-STOCK","SUPPLIER"])
    option = st.sidebar.selectbox("ACTION", menu)
    ch2 = st.sidebar.selectbox("RUN ANY QUERY",["Click here/Scroll Down \u2193"])
    if ch == "CUSTOMER":
        cu_create_table()
        if option == "ADD":
            st.subheader("Enter CUSTOMER Details :")
            cu_create()

        elif option == "VIEW":
            st.subheader("View added CUSTOMER :")
            cu_read()

        elif option == "EDIT":
            st.subheader("Update CUSTOMER Details :")
            cu_update()

        elif option == "REMOVE":
            st.subheader("Delete CUSTOMER Details :")
            cu_delete()

        else:
            st.subheader("About tasks")
            
#############################################################################################################

    if ch == "EMPLOYEE":
        em_create_table()
        if option == "ADD":
            st.subheader("Enter EMPLOYEE Details :")
            em_create()

        elif option == "VIEW":
            st.subheader("View added EMPLOYEE :")
            em_read()

        elif option == "EDIT":
            st.subheader("Update EMPLOYEE Details :")
            em_update()

        elif option == "REMOVE":
            st.subheader("Delete EMPLOYEE Details :")
            em_delete()

        else:
            st.subheader("About tasks")
            
#############################################################################################################

    if ch == "ITEMS-STOCK":
        it_create_table()
        if option == "ADD":
            st.subheader("Enter ITEM Details :")
            it_create()

        elif option == "VIEW":
            st.subheader("View added ITEMS :")
            it_read()

        elif option == "EDIT":
            st.subheader("Update ITEM Details :")
            it_update()

        elif option == "REMOVE":
            st.subheader("Delete ITEM Details :")
            it_delete()

        else:
            st.subheader("About tasks")
            
#############################################################################################################

    if ch == "SUPPLIER":
        su_create_table()
        if option == "ADD":
            st.subheader("Enter SUPPLIER AND SHIPPING Details :")
            su_create()

        elif option == "VIEW":
            st.subheader("View added SUPPLIER :")
            su_read()

        elif option == "EDIT":
            st.subheader("Update SUPPLIER AND SHIPPING Details :")
            su_update()

        elif option == "REMOVE":
            st.subheader("Delete SUPPLIER Details :")
            su_delete()

        else:
            st.subheader("About tasks")
       
#############################################################################################################
    def any_query_data(query):
        conn = mysql.connector.connect(**st.secrets["mysql"])
        cur = conn.cursor(buffered = True)
        cur.execute(query)
        result = cur.fetchall()
        conn.commit()
        conn.close()
        return result
    def any_query():
        st.subheader("RUN ANY QUERY")
        query = st.text_area("Enter your query here",value = "SELECT * FROM store")
        if st.button("Run Query"):
            result = any_query_data(query)
            df = pd.DataFrame(result)
            st.dataframe(df)
    st.write("------------------------------------------------------")
    if ch2 == "Click here/Scroll Down \u2193":
        any_query()


if __name__ == '__main__':
    main()
