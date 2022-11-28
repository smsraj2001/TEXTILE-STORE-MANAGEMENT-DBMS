-- TRIGGERS

-------------------------------------------------------------------------------------------------------------

-- a. Set a Trigger to check if the quantity of an item exceeds the size 50 in a store. If so, return an error
-- message.

SELECT Item_ID, quantity
FROM Contains
GROUP BY Item_ID;

DELIMITER $$
CREATE TRIGGER Item_Add
BEFORE INSERT 
ON Contains FOR EACH ROW
BEGIN
    DECLARE error_msg VARCHAR(255);
    SET error_msg = ('The new quantity cannot be greater than 50');
    IF new.Quantity > 50 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = error_msg;
    END IF;
END $$
DELIMITER ;
INSERT INTO `Contains`(`Store_ID`,`Item_ID`,`Quantity`)
VALUES (6004,4300,60);

-------------------------------------------------------------------------------------------------------------


-- b. Triggers and Cursors
-- Set a TRIGGER AND CURSOR by calling a stored procedure to create a backup of customer and his associated 
-- details after removing a customer from the database.

-- CREATE A BACKUP TABLE
CREATE TABLE `Customer_Backuplog` (
  `C_ID` int(11) NOT NULL,
  `First_Name` varchar(50) DEFAULT NULL,
  `Last_Name` varchar(50) NOT NULL,
  `Qualification` varchar(20) DEFAULT NULL,
  `ADDRESS` varchar(50) DEFAULT NULL,
  `Locality` varchar(20) DEFAULT NULL,
  `CITY` varchar(20) DEFAULT NULL,
  `Email` varchar(50) DEFAULT NULL,
  `Phone_NO` varchar(10) DEFAULT NULL,
  `DOP` date DEFAULT NULL,
  `E_ID` int(11) DEFAULT NULL,
  `Store_ID` int DEFAULT NULL,
  `Item_ID` int DEFAULT NULL,
  `Quantity` int DEFAULT NULL,
  `O_Amount` float DEFAULT NULL);

-- STORED PROCEDURE TO FORM A CURSOR AND DELETE THE CUSTOMER

BEGIN
DECLARE done INT DEFAULT 0;
DECLARE val int;
DECLARE `C_ID` int;
DECLARE `First_Name` varchar(50);
DECLARE `Last_Name` varchar(50);
DECLARE `Qualification` varchar(20);
DECLARE `ADDRESS` varchar(50);
DECLARE `Locality` varchar(20);
DECLARE `CITY` varchar(20);
DECLARE `Email` varchar(50);
DECLARE `Phone_NO` varchar(10);
DECLARE `DOP` date;
DECLARE `E_ID` int(11);
DECLARE `Item_ID` int;
DECLARE `Price` float;
DECLARE `Quantity` int;
DECLARE `O_Amount` float;

DELIMETER $$
DECLARE cur CURSOR FOR SELECT
C.C_ID, C.First_Name, C.Last_Name, C.Qualification,
C.Address, C.Locality, C.City, C.Email, C.Phone_NO, C.DOP, C.E_ID,
O.Item_ID,O.Price, O.Quantity, O.O_Amount
FROM Customers AS C, Orders as O
WHERE O.C_ID = C_ID_val AND C.C_ID = C_ID_val;
DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;


OPEN cur;
LABEL:loop

FETCH cur INTO  C_ID, First_Name, Last_Name, Qualification, Address,
Locality, City, Email, Phone_NO, DOP, E_ID,
Item_ID, Price, Quantity, O_Amount;

INSERT INTO Customer_Backuplog VALUES(C_ID, First_Name, Last_Name, Qualification, Address,
Locality, City, Email, Phone_NO, DOP, E_ID,
Item_ID, Price, Quantity, O_Amount);

IF done = 1 THEN LEAVE LABEL;
END IF;
END loop;
CLOSE cur;
SET val = (select count(*) from Customer_Backuplog where Customer_Backuplog.C_ID = C_ID_val);
IF val > 0 THEN
    DELETE FROM Orders
    WHERE Orders.C_ID = C_ID_val;
END IF;
END$$
DELIMITER ;

-- TRIGGER TO DELETE THE CUSTOMER

DELIMITER $$
CREATE TRIGGER Before_Delete_CustomerInfo
BEFORE DELETE
ON Customers FOR EACH ROW
BEGIN
CALL Delete_Customer(OLD.C_ID);
END$$
DELIMITER ;


-- COMMANDS

ALTER TABLE Orders  ADD CONSTRAINT `c_fid2`  FOREIGN KEY (`C_ID`) REFERENCES `Customers` (`C_ID`) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE Orders  ADD CONSTRAINT `item_fid2`  FOREIGN KEY (`Item_ID`) REFERENCES `Items` (`Item_ID`) ON DELETE CASCADE ON UPDATE CASCADE;

INSERT INTO `customers` (`C_ID`, `First_Name`, `Last_Name`, `Qualification`, `ADDRESS`, `Locality`, `CITY`, `Email`, `Phone_NO`, `DOP`, `E_ID`) VALUES
(2021, 'ABC', 'XYZ', 'Activist', 'Banashankari', 'Bannerghatta', 'Bangalore', 'abc@gmail.com', '9876543219', '2022-11-02', 1005);
INSERT INTO `orders` (`C_ID`, `ITEM_ID`,`PRICE`, `QUANTITY`, `O_Date`, `O_Amount`) VALUES ('2021', '4041','7999', '2', '2022-11-02', '15998');


DELETE FROM Customers WHERE C_ID = 2021;

TRUNCATE TABLE customer_backuplog;

--------------------------------------------------------------------------------------------------------

-------------------------------------------------------------------------------------------------------------


