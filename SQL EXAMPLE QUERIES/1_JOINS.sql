-- JOIN :

-------------------------------------------------------------------------------------------------------------

-- a. Retrieve the first name , last name and item names sold by employees to the customers where item price > 1000

SELECT I.ITEM_ID, I.Item_Name, I.Price, C.C_ID, C.First_Name AS CUSTOME_NAME, E.E_ID, E.First_Name AS EMPLOYEE_NAME
FROM ITEMS as I JOIN ORDERS AS O ON O.Item_ID = I.Item_ID JOIN CUSTOMERS AS C ON O.C_ID = C.C_ID 
RIGHT OUTER JOIN Employee AS E
ON C.E_ID = E.E_ID
WHERE I.Price >= 999;

-------------------------------------------------------------------------------------------------------------

-- b. List all the brands of the T-Shirt available in STORE : 6001 along with their quantities.

SELECT I.ITEM_ID, I.Item_Name, IC.Brand, C.quantity
FROM CONTAINS AS C JOIN ITEMS AS I ON C.Item_ID = I.Item_ID 
JOIN Item_Category AS IC ON I.Item_ID = IC.Item_ID
WHERE I.Item_ID in (4160,4161,4162,4163) AND C.Store_ID = 6001;

-------------------------------------------------------------------------------------------------------------

-- c. Retrieve the mode of travelling and names of suppliers, whose products were shipped during June.

SELECT SU.SUPP_ID, SH.Mode_of_travelling, SH.SHIP_ID, SHM.Date_of_Shipment
FROM Suppliers AS SU NATURAL JOIN Ships AS SH NATURAL JOIN SHIPMENT AS SHM
WHERE month(SHM.Date_of_Shipment) = 6;

-------------------------------------------------------------------------------------------------------------

-- d. List the details of items bought by customers who are engineers

SELECT I.Item_ID, I.Item_Name, IC.Gender, IC.Brand, IC.Colour, IC.Size, C.C_ID, C.First_Name AS NAME
FROM Customers AS C JOIN Orders AS O ON C.C_ID = O.C_ID JOIN Items AS I ON O.Item_ID = I.Item_ID
LEFT OUTER JOIN 
Item_Category as IC ON I.Item_ID = IC.Item_ID
WHERE C.Qualification LIKE '%engineer%';

-------------------------------------------------------------------------------------------------------------

-- e. Show the item name and brand in STORE = 6002 which has dress with size XXL or 42

SELECT S.Store_ID, I.Item_ID, I.Item_Name, IC.Brand
FROM Store AS S JOIN Contains AS C ON S.Store_ID = C.Store_ID JOIN Items AS I ON I.Item_ID = C.Item_ID 
JOIN Item_Category
AS IC ON I.Item_ID = IC.Item_ID
WHERE S.Store_ID = 6002 AND (IC.Size = 'XXL' OR IC.Size = 42);

-------------------------------------------------------------------------------------------------------------

-- f. List the customers visiting Store : 6003

SELECT C.C_ID, C.First_Name AS Customer_Name, C.Phone_NO
FROM Customers AS C JOIN Employee AS E ON C.E_ID = E.E_ID JOIN Store AS S ON E.MGR_ID = S.MGR_ID
WHERE S.Store_ID = 6003;

-------------------------------------------------------------------------------------------------------------
