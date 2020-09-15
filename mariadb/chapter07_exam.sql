USE employees;

SELECT U.first_name, DP.dept_name, D.from_date, D.to_date FROM employees U
	INNER JOIN dept_emp D
		ON U.emp_no = D.emp_no
	INNER JOIN departments DP
		ON DP.dept_no = D.dept_no
		WHERE D.to_date = '9999-01-01'
ORDER BY U.first_name
