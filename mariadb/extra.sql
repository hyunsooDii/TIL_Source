USE employees;

/*
SELECT * FROM employees WHERE emp_no = 10838;

SELECT * FROM employees WHERE first_name = 'Deniz';


CREATE INDEX idx_employees_fst_name
	ON employees (first_name);
	
SHOW INDEX FROM usertbl;
*/

CREATE USER 'iot_user'@'%' IDENTIFIED BY '1234';

grant DROP 'iot_user'

SELECT * FROM employees.employees;