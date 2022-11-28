
-------------------------------------------------------------------------------------------------------------
--a.   VIEW of BILL with dynamic update with each item and quantity mapped to each customer with total amount

CREATE VIEW `Bills` AS
SELECT C.C_ID, C.First_Name, C.Last_Name, I.Item_ID, I.Item_Name,IC.Brand,IC.Size, O.Quantity, sum(O.O_Amount) AS TOTAL,C.DOP
FROM Customers AS C JOIN ORDERS AS O ON C.C_ID = O.C_ID JOIN Items as I ON I.Item_ID = O.Item_ID 
JOIN Item_Category AS IC ON I.Item_ID = IC.Item_ID
GROUP BY O.C_ID,Item_ID
ORDER BY C.DOP ASC;

-------------------------------------------------------------------------------------------------------------
-- b.   VIEW of BILL with dynamic update with each item and quantity mapped to each

CREATE VIEW `Total_Orders` AS
SELECT O.Item_ID,O.C_ID,I.Price,O.Quantity,(O.quantity * I.price) AS O_Amount
FROM Orders AS O JOIN Items AS I
on O.Item_ID = I.Item_ID;

-------------------------------------------------------------------------------------------------------------
