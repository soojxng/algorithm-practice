SELECT sum(g.score) AS score, e.emp_no, e.emp_name, e.position, e.email
FROM hr_employees AS e, hr_grade AS g
WHERE e.emp_no = g.emp_no
GROUP BY g.emp_no, g.year
HAVING g.year = '2022'
ORDER BY score DESC
LIMIT 1;