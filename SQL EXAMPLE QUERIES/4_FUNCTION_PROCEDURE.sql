-- PROCEDURE :

-------------------------------------------------------------------------------------------------------------

-- a. Procedure to display the age of a particular employee : 
-- Procedure to display the age of an employee provided the Employee ID and this procedure returns age as the output

DELIMITER &&  
CREATE PROCEDURE Display_Age(IN UID int, OUT Age INT)
BEGIN  
    DECLARE Date_OF_Birth date; 
    SELECT * FROM Employee WHERE E_ID = UID;
    SELECT E.DOB INTO Date_OF_Birth
    FROM Employee AS E
    WHERE E.E_ID = UID;
    SET Age = FLOOR(DATEDIFF(CURRENT_DATE, Date_OF_Birth)/365);
END &&  
DELIMITER ;  
CALL Display_Age(1001,@AGE);
SELECT @AGE;

-------------------------------------------------------------------------------------------------------------

-- FUNCTION :
-- b. Create a function to display the customer level based on their order amount of purchase. 
-- FUNCTION to display the level of a customer as PLATINUM, GOLD, SILVER, BRONZE based on his/her total purchase


DELIMITER $$

CREATE FUNCTION CustomerLevel(C_ID int) 
RETURNS VARCHAR(20)
DETERMINISTIC
BEGIN
    DECLARE customerLevel VARCHAR(20);
    DECLARE credit float;
    SELECT sum(O.O_Amount) INTO credit
    FROM ORDERS AS O
    WHERE O.C_ID = C_ID
    GROUP BY O.C_ID;
    

    IF credit > 25000 THEN
		SET customerLevel = 'PLATINUM';
    ELSEIF (credit >= 21000 AND 
			credit <= 25000) THEN
        SET customerLevel = 'GOLD';
    ELSEIF credit < 20000 THEN
        SET customerLevel = 'SILVER';
    ELSE
        SET customerLevel = 'BRONZE';
    END IF;
	-- Return the customer level
	RETURN (customerLevel);
END$$
DELIMITER ;

SELECT `C_ID`,`First_Name`,`Last_Name`, CustomerLevel(`C_ID`) FROM `Customers`;

-------------------------------------------------------------------------------------------------------------

-- c. Function to calculate Discount

DELIMITER $$
CREATE FUNCTION Discount(C_ID int) 
RETURNS float
DETERMINISTIC
BEGIN
    DECLARE credit float;
    DECLARE discount float;
    DECLARE final_amount float;
    SELECT Amount INTO credit
    FROM Bill AS B
    WHERE B.C_ID = C_ID;
    

    IF credit > 25000 THEN
		SET final_amount = credit - (credit * 0.2);
        SET discount = credit * 0.2;
    ELSEIF (credit > 10000 AND credit <= 25000) THEN
        SET final_amount = credit - (credit * 0.1);
        SET discount = credit * 0.1;
    ELSEIF (credit > 5000 AND credit <= 10000) THEN
        SET final_amount = credit - (credit * 0.08);
        SET discount = credit * 0.08;
    ELSE
        SET final_amount = credit - (credit * 0.05);
        SET discount = credit * 0.05;
    END IF;
	RETURN (discount);
END$$
DELIMITER ;
SELECT B_ID,Amount,C_ID, Discount(C_ID) FROM Bill;
SET @p0='2002'; SELECT `Discount`(@p0) AS `Discount`;

-------------------------------------------------------------------------------------------------------------
