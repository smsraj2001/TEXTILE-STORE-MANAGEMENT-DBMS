SELECT O.C_ID,C.First_Name, sum(O.O_Amount) AS MAXIMUM 
FROM ORDERS AS O,CUSTOMERS AS C 
WHERE O.C_ID = C.C_ID 
GROUP BY O.C_ID 
ORDER BY sum(O.O_Amount) DESC 

------------------------------------------------------------------------------------------------------

SELECT O.C_ID, sum(O.O_Amount) AS MAXIMUM
FROM ORDERS AS O
WHERE O.C_ID = 2001
ORDER BY sum(O.O_Amount) DESC

------------------------------------------------------------------------------------------------------

DELIMITER $$
CREATE TRIGGER Discount 
AFTER INSERT ON Bill FOR EACH ROW
BEGIN
    DECLARE error_msg VARCHAR(255);
    SET error_msg = ('The new quantity cannot be greater than 50');
    IF new.Amount > 20000 THEN
        SET Bill.Amount = New.Amount - (New.Amount * 0.2) ;
        SET @msg = CONCAT('The discount given is ', New.Amount * 0.2);
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = @msg;

    ELSE IF new.Amount > 10000 THEN
        SET Amount = New.Amount - (New.Amount * 0.1);
        SET @msg = CONCAT('The discount given is ', New.Amount * 0.1);
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = @msg;

    END IF;
    ELSE
        UPDATE Bill SET Amount = New.Amount - (New.Amount * 0.05) WHERE c_id = NEW.c_id;
        SET @msg = CONCAT('The discount given is ', New.Amount * 0.05);
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = @msg;

    END IF;
END $$
DELIMITER;

------------------------------------------------------------------------------------------------------

UPDATE Bill
SET Final_Amount = Amount - Discount(C_ID);
