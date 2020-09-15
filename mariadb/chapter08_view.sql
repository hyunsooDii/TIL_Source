USE tabledb;

/*
CREATE VIEW v_userTBL
AS
SELECT userid, name, addr FROM usertbl;

SELECT * FROM v_userTBL;
*/

 ALTER TABLE userTBL
 ADD homepage VARCHAR(30)
 DEFAULT 'http://www.hanbit.co.kr'
 NULL;

ALTER TABLE usertbl
ADD mobile1, CHAR(8), null;

SELECT U.userid, U.name, B.prodName, U.addr,
CONCAT(U.mobile1, U.mobile2) AS '연락처'
FROM userTBL U
INNER JOIN buyTBL B
ON U.userid = B.userid ;
