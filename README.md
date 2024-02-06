# TEXTILE-STORE-MANAGEMENT-DBMS
A DBMS project on Textile Store Management using StreamLit-Python for the frontend app and a ```mysql``` database

## SYNOPSIS

A DBMS mini project on Textile Store Management System where we use streamlit python for front-end and ```mysql database``` as the backend. Apart from that we have multiple mysql queries based on :
- Joins, comprising natural, inner, outer, etc...
- Aggregation & Set operations
- Views
- Triggers & Cursors
- Procedures & Functions

## INSTRUCTIONS
- Install the latest version of ```XAMPP``` or any other mysql equivalent workspace
- Download the project, or enter the following in terminal ```if you have git installed``` :-
```bash 
git clone github.com/smsraj2001/TEXTILE-STORE-MANAGEMENT-DBMS.git
```
### DATABASE
- Next switch on your xampp server and click on `phpMyAdmin` and click on `New` database and create it with any name.
  - Now click on your new database and on your right panel select `Import` option and upload the .sql file from the database folder available in `TEXTILE-STORE-MANAGEMENT-DBMS` folder.
  - Your database will be loaded with all the pre-existing values, functions, procedures, triggers, views, cursors, etc...
  - Enter your my-sql database connection details in the ```secrets.toml``` file available in the ```/.streamlit``` directory in ```SRC-APP (Root-Directory)```. 
  - For complete understanding of the database please refer to the `ER-Diagrams` uploaded which has both E-R diagram and Relational Schema
  - Now let's dive to the front end

### FRONTEND
- Before entering the front-end, *(Python should be already installed)* , install `streamlit` and `plotly` by the following command :
  ```bash 
  pip install streamlit
  ```
  ```bash 
  pip install plotly
  ```
- After this enter into the folder:
  ```bash 
  cd TEXTILE-STORE-MANAGEMENT-DBMS\SRC-APP
  ```
- Open a terminal here and run 
  ```bash 
  steamlit run app.py
  ```
- Remember : In the ```database.py``` file , rename the database name to the name you had given initially in the ```DATABASE``` instructions.
- Hence, you have the entire project running successfully.
- For deeper understanding of the DBMS project, look into the ```REPORT PDF``` uploaded for visualizing the outputs for database and front-end.

#### ENJOY !!!

#### ```UPDATE``` : [Click Here](https://textile-store-management-app.onrender.com/) Deployed in ```RENDER```!!!
#### ```NOTE``` : For any queries/corrections, please feel free to mail : sutharsanraj2001@gmail.com

  
