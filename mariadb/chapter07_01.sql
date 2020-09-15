/* SQL 고급 - 조인 (제일 중요한 part)
*/

/*
[형식]
SELECT <열 목록>
FROM <첫 번째 테이블>
INNER JOIN <두 번째 테이블>
ON <조인될 조건 = 공통 컬럼>
[WHERE 검색 조건]
*/

USE sqlDB;

/*
SELECT *
FROM buyTBL
	INNER JOIN userTBL
	ON buyTBL.userID = Usertbl.userID
WHERE buytbl.userID = 'BBK' -- 이름이 중복될 경우 table 명까지 작성
ORDER BY usertbl.userID
*/

/*
SELECT buytbl.userID, NAME, prodName, addr, CONCAT(mobile1, mobile2) AS '연락처'
FROM buytbl
	INNER JOIN userTBL
	ON buytbl.userID = usertbl.userID
*/

/*
SELECT B.userID, U.name, B.prodName, U.addr,
	CONCAT(mobile1, mobile2) AS '연락처'
FROM buytbl B
	INNER JOIN usertbl U
	ON B.userID = U.userID
WHERE B.userID = 'JYP'
ORDER BY U.userID;
*/

/*
SELECT DISTINCT U.userID, U.name, U.addr
FROM usertbl U
	INNER JOIN buytbl B
	ON U.userID = B.userID
ORDER BY U.userID;
*/

/*
SELECT U.addr, sum(B.amount) AS '지역별배송건', SUM(B.amount*B.price) AS '매출 현황' FROM usertbl U
	INNER JOIN buytbl B
	ON B.userID = U.userID
GROUP BY U.addr;
*/


/*
CREATE TABLE stdTBL(
stdName VARCHAR(10) NOT NULL PRIMARY KEY,
addr CHAR(4) NOT NULL
);

CREATE TABLE clubTBL(
clubName VARCHAR(10) NOT NULL PRIMARY KEY,
roomNo CHAR(4) NOT NULL
);

CREATE TABLE stdclubTBL(
num int AUTO_INCREMENT NOT NULL PRIMARY KEY,
stdName VARCHAR(10) NOT NULL,
clubName VARCHAR(10) NOT NULL,
FOREIGN KEY(stdName) REFERENCES stdTBL(stdName),
FOREIGN KEY(clubName) REFERENCES clubTBL(clubName)
);
*/

/*
INSERT INTO stdTBL VALUES
(N'김범수', N'경남'), (N'성시경', N'서울'), (N'조용필', N'경기'),
(N'은지원', N'경북'), (N'바비킴', N'서울');
INSERT INTO clubTBL VALUES
(N'수영', N'101호'), (N'바둑', N'102호'), (N'축구', N'103호'),
(N'봉사', N'104호');
INSERT INTO stdclubTBL VALUES
(NULL, N'김범수', N'바둑'), (NULL, N'김범수', N'축구'),
(NULL, N'조용필', N'축구'), (NULL, N'은지원', N'축구'),
(NULL, N'은지원', N'봉사'), (NULL, N'바비킴', N'봉사');
*/

/*
SELECT S.stdName, S.addr, C.clubName, C.roomNo
FROM stdtbl S
	INNER JOIN stdclubtbl SC
		ON S.stdName = SC.stdName
	INNER JOIN clubtbl C
		ON SC.clubName = C.clubName
ORDER BY S.stdName;
*/


/*
SELECT U.userId, U.name, B.prodName, U.addr, CONCAT(U.mobile1, U.mobile2) AS '연락처'
FROM usertbl U
	left OUTER JOIN buytbl B
	ON U.userID = B.userID
	WHERE B.prodName is NULL
ORDER BY U.userID;

SELECT U.userId, U.name, B.prodName, U.addr, CONCAT(U.mobile1, U.mobile2) AS '연락처'
FROM usertbl U
	right OUTER JOIN buytbl B
	ON U.userID = B.userID
ORDER BY U.userID;
*/

/*
SELECT U.userId, U.name, IFNULL(sum(B.price*B.amount),0) AS '총 구매액'
FROM usertbl U
	left OUTER JOIN buytbl B
	ON U.userID = B.userID
GROUP BY U.userID	;
*/

/*
CREATE TABLE empTbl (emp CHAR(3), manager CHAR(3), emptel VARCHAR(8));

INSERT INTO empTbl VALUES
(N'나사장',NULL,'0000'),
(N'김재무',N'나사장','2222'),
(N'김부장',N'김재무','2222-1'),
(N'이부장',N'김재무','2222-2'),
(N'우대리',N'이부장','2222-2-1'),
(N'지사원',N'이부장','2222-2-2'),
(N'이영업',N'나사장','1111'),
(N'한과장',N'이영업','1111-1'),
(N'최정보',N'나사장','3333'),
(N'윤차장',N'최정보','3333-1'),
(N'이주임',N'윤차장','3333-1-1');
*/

/*
SELECT A.emp AS '부하직원', B.emp AS '직속상관', B.empTel AS '직속상관연락처'
FROM emptbl A
	INNER JOIN emptbl B
		ON A.manager = B.emp
WHERE A.emp = '우대리';
*/


SELECT stdName, addr FROM stdtbl
UNION ALL
SELECT clubName, roomNo FROM clubtbl;

SELECT NAME, CONCAT(mobile1, mobile2) AS '전화번호' FROM usertbl
WHERE NAME NOT IN (SELECT NAME FROM usertbl WHERE mobile1 IS NULL);

SELECT NAME, CONCAT(mobile1, mobile2) AS '전화번호' FROM usertbl
WHERE NAME IN(SELECT NAME FROM usertbl WHERE mobile1 IS NULL);