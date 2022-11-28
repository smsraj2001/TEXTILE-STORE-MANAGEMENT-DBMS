-- AGGREGATE FUNCTIONS :

-------------------------------------------------------------------------------------------------------------

-- a. Average salary of all the employees in their respective stores

SELECT S.Store_ID, S.Name, S.MGR_ID, AVG(E.Salary) AS Average_Salary
FROM Store AS S JOIN Employee AS E ON S.MGR_ID = E.MGR_ID
GROUP BY E.MGR_ID
ORDER BY AVG(E.Salary) ASC;

-------------------------------------------------------------------------------------------------------------

-- b. Find out total sales across all the stores during July to December

SELECT  S.Store_ID, S.Name, S.MGR_ID, SUM(O.O_Amount) AS Total_Sales
FROM Orders AS O JOIN Customers AS C ON O.C_ID = C.C_ID JOIN Employee AS E ON C.E_ID = E.E_ID
JOIN Store AS S ON S.MGR_ID = E.MGR_ID
GROUP BY E.MGR_ID
ORDER BY SUM(O.O_Amount) DESC;

-------------------------------------------------------------------------------------------------------------

-- c. Count the total number of customers according to their qualifications

SELECT Qualification, COUNT(qualification)
FROM CUSTOMERS
GROUP BY Qualification;

-------------------------------------------------------------------------------------------------------------

-- d. Find the customers with highest and lowest number of order amount

SELECT O.C_ID, sum(O.O_Amount) AS MAXIMUM
FROM ORDERS AS O
GROUP BY O.C_ID
ORDER BY sum(O.O_Amount) DESC
LIMIT 1;

SELECT O.C_ID, sum(O.O_Amount) AS MINIMUM
FROM ORDERS AS O
GROUP BY O.C_ID
ORDER BY sum(O.O_Amount) ASC
LIMIT 1;

-------------------------------------------------------------------------------------------------------------

-- e. Retrieve the maximum and minimum orders by each and every customer.

SELECT O.C_ID, MAX(O.O_Amount) AS MAXIMUM,  MIN(O.O_Amount)
FROM ORDERS AS O
GROUP BY O.C_ID
ORDER BY (O.O_Amount) ASC

-------------------------------------------------------------------------------------------------------------
