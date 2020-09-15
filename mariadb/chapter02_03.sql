-- USE sqldb;

/* SELECT * FROM usertbl;

SELECT * FROM usertbl WHERE NAME = '김경';
*/

/*
SELECT userID FROM usertbl;
WHERE birthYear >= 1970 AND height >= 182;
*/

/*
SELECT NAME, addr FROM usertbl;
WHERE addr IN('경남', '전남', '경북');
*/

/*
SELECT NAME, height;
FROM usertbl;
WHERE NAME LIKE "김%";
*/

-- USE employees;

-- SELECT first_name FROM employees;
-- SELECT first_name, last_name, gender FROM employees;

-- SELECT first_name AS 이름, gender AS 성별 FROM employees;

/*
SELECT *
FROM employees
WHERE birth_date >= '1960-01-01';

SELECT * FROM employees
WHERE birth_date BETWEEN '1960-01-01' AND "1960-12-31"*/

/*
SELECT *
FROM employees
WHERE last_name IN('Lenart', 'Baaz', 'Pillow');
*/
-- USE sqldb;

-- SELECT height FROM usertbl WHERE addr = '경남';

/*
SELECT NAME, height FROM usertbl
WHERE height = ANY (SELECT height FROM usertbl WHERE addr = '경남');\
*/

/*
SELECT NAME, mdate FROM usertbl ORDER BY mdate;
-- mDate의 오름 차순으로 정렬
*/

/*
SELECT NAME, height FROM usertbl ORDER BY height DESC, NAME ASC;
-- height로 내림차순 정렬하고,
-- height가 동률일 때는 name으로 오름차순 정렬
*/

/*
SELECT DISTINCT addr FROM usertbl;
-- 중복된 것은 하나만 남기는 DISTINCT
*/

-- USE employees;

/*
SELECT emp_no, hire_date FROM employees 
ORDER BY hire_date ASC
LIMIT 0, 5; -- Limit 5, offset 0
-- 출력하는 개수를 제한하는 LIMIT , 게시판이용할 때 사용
*/

-- USE sqldb;

/*
CREATE TABLE buyTbl2 (SELECT * FROM buyTbl);
SELECT * FROM buyTbl2;

CREATE TABLE buytbl3 (SELECT userID, prodname FROM buytbl);
SELECT * FROM buytbl3;

CREATE TABLE buytbl4 (SELECT userID AS user, prodname AS product FROM buytbl);
SELECT * FROM buytbl4;
-- 테이블을 복사하는 CREATE TABLE … SELECT
*/

/*
SELECT userID, price*amount, price, amount
FROM buytbl
order BY userID;

SELECT USERID AS '사용자아이디', SUM(price*amount) AS '총 구매액'
FROM buytbl
GROUP BY userID;
-- GROUP BY 및 HAVING 그리고 집계 함수

SELECT COUNT(userid)AS '개수' FROM buytbl;

SELECT COUNT(mobile1) FROM usertbl;

SELECT COUNT(*), COUNT(userID), COUNT(mobile1) FROM usertbl;
*/

/*
SELECT AVG(amount) AS "평균 구매 개수" FROM buytbl;

SELECT AVG(amount) AS "평균 구매 개수" FROM buytbl
GROUP BY userID;

SELECT NAME, MAX(height), MIN(height) FROM usertbl;

SELECT NAME, MAX(height), MIN(height) FROM usertbl
GROUP BY NAME;
*/

/*
SELECT NAME, height
FROM usertbl
WHERE height = (SELECT MAX(height) FROM usertbl)
OR height = (SELECT MIN(height)FROM usertbl);
*/

/*
HAVING 절
GROUP BY 결과에서 필터링
*/

/*
SELECT userid AS '사용자', SUM(price*amount) AS '총구매액'
FROM buytbl
GROUP BY userid
HAVING SUM(price*amount)>1000 -- sum(price*amount) 대신 '총구매액' 으로 써도 됨
ORDER BY '총구매액'buytbl2buytbl DESC;
*/

/*
SELECT num, groupname, SUM(price * amount) AS '비용'
FROM buytbl
GROUP BY groupname, num
WITH ROLLUP;

SELECT num, groupname, SUM(price * amount) AS '비용'
FROM buytbl
GROUP BY groupname
WITH ROLLUP;
*/

/*
CREATE TABLE testtbl1 (id INT, username CHAR(3), age INT);

INSERT INTO testtbl1 VALUES (1, '홍길동', 25);
INSERT INTO testtbl1(id, username) VALUES (2, '설현');
INSERT INTO testtbl1(username, age, id) VALUES ('초아', 25, 3);

SELECT * FROM testtbl1
*/

/*
CREATE TABLE testtbl2
	(id INT AUTO_INCREMENT PRIMARY KEY,
	username CHAR(3),
	age INT );*/

/*	
INSERT INTO testtbl2 VALUES (NULL, '지민', 25);
INSERT INTO testtbl2 VALUES (NULL, '유나', 22);
INSERT INTO testtbl2 VALUES (NULL, '유경', 21);
INSERT INTO testtbl2 (username, age) VALUES ('둘리',12);

SELECT * FROM testtbl2 ORDER BY id DESC -- 최신 순으로 정렬
*/

/*
CREATE TABLE testTBL3
(id int AUTO_INCREMENT PRIMARY KEY,
userName char(3),
age INT );
ALTER TABLE testTBL3 AUTO_INCREMENT=1000;

INSERT INTO testtbl3 VALUES (NULL, '나연', 20);
INSERT INTO testtbl3 VALUES (NULL, '정연', 18);
INSERT INTO testtbl3 VALUES (NULL, '모모', 19);

INSERT INTO testtbl3 VALUES -- 데이터를 한번에 많이 줄때
(NULL, '나연', 20),
(NULL, '정연', 18),
(NULL, '모모', 19);

SELECT * FROM testtbl3;
*/

/*
CREATE TABLE testTBL4 (id int, Fname varchar(50), Lname varchar(50));

INSERT INTO testTBL4
SELECT emp_no, first_name, last_name
FROM employees.employees ;



SELECT * FROM testtbl4 WHERE fname = 'Maryemployeesemployees';

DELETE FROM testtbl4 WHERE fname = 'Aamer';
DELETE FROM testtbl4 WHERE fname = 'Mary' LIMIT 5;
*/

/*
SELECT AVG(amount) AS '평균 구매 개수' FROM buytbl;
SELECT CAST(AVG(amount) AS SIGNED INTEGER) AS '평균 구매 개수' FROM buytbl;

SELECT CONVERT(AVG(amount), SIGNED INTEGER) AS '평균 구매 개수' FROM buytbl;
SELECT CAST('2022$12$12' AS DATE)
*/

/*
SELECT
	num,
	CONCAT(CAST(price AS CHAR(10)), 'X', CAST(amount AS CHAR(4)), '=')
	AS '단가X수량',
	price*amount AS '구매액'
FROM buytbl;
*/

/*
SELECT '100' + '200' ; -- 문자와 문자를 더함 (정수로 변환되서 연산됨)
SELECT CONCAT('100', '200'); -- 문자와 문자를 연결 (문자로 처리)
SELECT CONCAT(100, '200'); -- 정수와 문자를 연결 (정수가 문자로 변환되서 처리)
SELECT 1 > '2mega'; -- 정수 2로 변환되어서 비교
SELECT 3 > '2MEGA'; -- 정수 2로 변환되어서 비교
SELECT 0 = 'mega2'; -- 문자는 0으로 변환됨
*/

/*
SELECT if (100 > 200, '참이다', '거짓이다'); -- From 안써도됨
SELECT IFNULL(NULL, '널이군요'), IFNULL(100,'널이군요'); -- 수식1이 Null이 아니면 수식1리턴, Null이면 수식2 리턴
SELECT NULLIF(100,100), NULLIF(200,100); -- 수식1과 수식2가 같으면 Null반환, 다르면 수식1 반환
*/

/*
SELECT
	case 10
		when 1 then '일'
		when 5 then '오'
		when 10 then '십'
		ELSE '모름'
	END;
*/

/*
SELECT BIT_LENGTH('가나다'), CHAR_LENGTH('가나다'), LENGTH('가나다'); -- CHAR_LENGTH : 글자 개수 LENGTH : Byte 수
SELECT CONCAT_WS('/', '2022', '01', '01'); -- Join함수랑 비슷
*/

/*
SELECT
ELT(2, '하나', '둘', '셋'), -- 매개변수의 숫자에 따른 문자 위치
FIELD('둘', '하나', '둘', '셋'), -- 매개변수의 문자가 몇번째에 있느냐
FIND_IN_SET('둘', '하나,둘,셋'), -- 콤마로 구분됐을때 몇번째에 위치 하는가
INSTR('하나둘셋', '둘'), -- find와 같음, 첫번째 문자열에서 두번째 매개변수가 몇번째에 있는지 
LOCATE('둘', '하나둘셋'); -- INSTR의 매개변수위치가 다름
*/

/*
-- SELECT FORMAT(123456.123456,4) -- FORMAT(숫자, 소수점 자리수)
SELECT INSERT('abcdefghi', 3, 4, '@@@@'), INSERT('abcdefghi', 3, 2, '@@@@'); -- INSERT(기준 문자열, 위치, 길이, 삽입할 문자열)
SELECT LEFT('abcdefghi', 3), RIGHT('abcdefghi', 3); -- 문자열 왼쪽에서 몇번째, 오른쪽에서 몇번째 출력
SELECT LOWER('abcdEFGH'), UPPER('abcdEFGH'); -- 대문자, 소문자 변환
*/

/*
SELECT LPAD('이것이', 5, '##'), RPAD('이것이', 5, '##'); -- LPAD(문자열, 길이), RIGHT(문자열, 길이)
SELECT LTRIM(' 이것이'), RTRIM('이것이 '); -- LTRIM(문자열), RTRIM(문자열)
SELECT TRIM(' 이것이 '), TRIM(BOTH 'ㅋ' FROM 'ㅋㅋㅋ재밌어요.ㅋㅋㅋ'); --TRIM(문자열), TRIM(방향 자를_문자열 FROM 문자열)
*/

/*
SELECT REPEAT('이것이', 3); -- REPEAT(문자열, 횟수)
SELECT REPLACE ('이것이 MariaDB다', '이것이' , 'This is'); -- REPLACE(문자열, 원래문자열, 바꿀문자열)
SELECT REVERSE ('MariaDB'); -- Reverse(문자열)
*/

/*
SELECT CONCAT('이것이', SPACE(10), 'MariaDB다'); -- SPACE(길이)
SELECT SUBSTRING('대한민국만세', 3, 2); --SUBSTRING(문자열, 시작위치, 길이),
                                        --SUBSTRING(문자열 FROM 시작위치 FOR 길이)
*/

/*
SELECT
SUBSTRING_INDEX('cafe.naver.com', '.', 2), 
SUBSTRING_INDEX('cafe.naver.com', '.', -2); --SUBSTRING_INDEX(문자열, 구분자, 횟수)
*/

/*
SELECT -- ADDDATE(날짜, 차이), SUBDATE(날짜, 차이)
ADDDATE('2022-01-01', INTERVAL 31 DAY),
ADDDATE('2022-01-01', INTERVAL 1 MONTH);
SELECT
SUBDATE('2022-01-01', INTERVAL 31 DAY),
SUBDATE('2022-01-01', INTERVAL 1 MONTH);
*/

/*
SELECT YEAR(CURDATE()), MONTH(CURRENT_DATE()), DAYOFMONTH(CURRENT_DATE); -- NOW(), SYSDATE()는 INSERT문에 많이 쓰임
SELECT HOUR(CURTIME()), MINUTE(CURRENT_TIME()), SECOND(CURRENT_TIME),
MICROSECOND(CURRENT_TIME);
*/

/*
USE employees;

SELECT * FROM employees
WHERE month(birth_date) = month(NOW()) AND DAY(birth_date) = DAY(NOW());
*/

/*
SELECT CURRENT_USER(), DATABASE();
*/

USE sqlDB;
/*
SELECT * FROM userTBL;
SELECT FOUND_ROWS(); -- ▪ FOUND_ROWS():바로 앞의 SELECT 호출 결과 행의 수 리턴
*/

/*
UPDATE buyTBL SET price=price*2;
SELECT ROW_COUNT(); -- ROW_COUNT(): INSERT, UPDATE, DELETE 호출 결과 영향 받은 행의 수 리턴
*/

/*
SELECT * INTO OUTFILE 'C:/temp/userTBL.txt' FROM userTBL; -- 테이블 -> 파일
*/

CREATE TABLE memberTBL LIKE userTBL; -- 테이블 구조만 복사
LOAD DATA LOCAL INFILE 'C:/temp/userTBL.txt' INTO TABLE memberTBL;
SELECT * FROM memberTBL;





