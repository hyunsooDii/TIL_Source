DROP DATABASE IF EXISTS tableDB;
CREATE DATABASE tableDB;

USE tableDB;

DROP TABLE IF EXISTS buyTBL, userTBL;
CREATE TABLE userTBL
(userID char(8) not null PRIMARY KEY,
 name varchar(10) NOT NULL,
 birthYear int NOT NULL,
 addr char(2) NOT NULL,
 mobile1 char(3) NULL,
 mobile2 char(8) NULL,
 height smallint NULL,
 mDate date NULL
);
 
DROP TABLE IF EXISTS buyTBL; 
CREATE TABLE buyTBL
(num int AUTO_INCREMENT NOT NULL PRIMARY KEY ,
 userid char(8) NOT NULL ,
 prodName char(6) NOT NULL,
 groupName char(4) NULL ,
 price int NOT NULL,
 amount smallint NOT NULL,
 CONSTRAINT FK_userTBL_buyTBL FOREIGN KEY(userID) REFERENCES userTBL(userID)
);
/*
INSERT INTO userTBL VALUES
('LSG', '이승기', 1987, '서울', '011', '1111111', 182, '2008-8-8');
INSERT INTO userTBL VALUES
('KBS', '김범수', 1979, '경남', '011', '2222222', 173, '2012-4-4');
INSERT INTO userTBL VALUES
('KKH', '김경호', 1971, '젂남', '019', '3333333', 177, '2007-7-7');

INSERT INTO buyTBL VALUES(NULL, 'KBS', '운동화', NULL , 30, 2);
INSERT INTO buyTBL VALUES(NULL, 'KBS', '노트북', '젂자', 1000, 1);
*/

CREATE TABLE usertbl2
(
 userID CHAR(8) NOT NULL,
 name VARCHAR(10) NOT NULL,
 birthYear INT NOT NULL,
 CONSTRAINT PRIMARY KEY PK_userTBL_userID (userID)
);

DROP TABLE IF EXISTS prodTbl;
CREATE TABLE prodTbl
( prodCode CHAR(3) NOT NULL,
 prodID CHAR(4) NOT NULL,
 prodDate DATETIME NOT NULL,
 prodCur CHAR(10) NULL
);
ALTER TABLE prodTbl
ADD CONSTRAINT PRIMARY KEY (prodCode, prodID); 

ALTER TABLE buyTBL
 DROP FOREIGN KEY FK_userTBL_buyTBL;
 
ALTER TABLE buyTBL
 ADD CONSTRAINT FK_userTBL_buyTBL
 FOREIGN KEY (userID) REFERENCES userTBL (userID) ON UPDATE CASCADE;
 
 ALTER TABLE userTBL
 ADD homepage VARCHAR(30)
 DEFAULT 'http://www.hanbit.co.kr'
 NULL;
 
 ALTER TABLE userTBL
 DROP COLUMN mobile1;
 
 ALTER TABLE userTBL
 CHANGE COLUMN name uName VARCHAR(20) NULL ;
