-- SET OPERATIONS :

-------------------------------------------------------------------------------------------------------------

-- a. List the mode of travelling to store 6003 between April and June.

SELECT DISTINCT SHM1.Store_ID,SH1.Mode_of_Travelling, SHM1.Date_of_Shipment
FROM Ships AS SH1, Shipment AS SHM1
WHERE month(SHM1.Date_of_Shipment) >= 4 AND SHM1.Store_ID = 6003
UNION
SELECT DISTINCT SHM2.Store_ID, SH2.Mode_of_Travelling, SHM2.Date_of_Shipment
FROM Ships AS SH2, Shipment AS SHM2
WHERE month(SHM2.Date_of_Shipment) <= 6 AND SHM2.Store_ID = 6003;

-------------------------------------------------------------------------------------------------------------

-- b. List the customers who bought both Tops/Shirt and Leggings/Jeggings

SELECT C1.C_ID,C1.First_Name as Name
FROM Customers AS C1 JOIN Orders as O1 ON O1.C_ID = C1.C_ID JOIN Items AS I1 ON O1.Item_ID = I1.Item_ID
WHERE I1.Item_Name = 'Tops' OR I1.Item_Name = 'Shirt'
INTERSECT
SELECT C2.C_ID,C2.First_Name as Name
FROM Customers AS C2 JOIN Orders as O2 ON O2.C_ID = C2.C_ID JOIN Items AS I2 ON O2.Item_ID = I2.Item_ID
WHERE I2.Item_Name = 'Legging' OR I2.Item_Name = 'Jeggings';

-------------------------------------------------------------------------------------------------------------

-- c. Details of dresses of all colours except 'red' and 'blue' 

SELECT IC1.Item_ID, IC1.Item_Name, IC1.Colour
FROM Item_Category AS IC1
EXCEPT
SELECT IC2.Item_ID, IC2.Item_Name, IC2.Colour
FROM Item_Category AS IC2
WHERE IC2.Colour LIKE '%red%' OR IC2.Colour LIKE '%blue%'

-------------------------------------------------------------------------------------------------------------

-- d. Find all items which are bought in September or October-2022

SELECT I1.Item_ID, I1.Item_Name, O1.O_Date
FROM Orders AS O1 JOIN Items as I1 ON O1.Item_ID = I1.Item_ID 
WHERE month(O1.O_Date) = 9
UNION ALL
SELECT I2.Item_ID, I2.Item_Name, O2.O_Date
FROM Orders AS O2 JOIN Items as I2 ON O2.Item_ID = I2.Item_ID 
WHERE month(O2.O_Date) = 10;

-------------------------------------------------------------------------------------------------------------
