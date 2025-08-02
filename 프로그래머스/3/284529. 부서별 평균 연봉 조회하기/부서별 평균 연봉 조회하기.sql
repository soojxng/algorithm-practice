SELECT d.dept_id, d.dept_name_en, ROUND(AVG(e.sal), 0) AS avg_sal
FROM hr_department AS d, hr_employees AS e
WHERE d.dept_id = e.dept_id
GROUP BY e.dept_id
ORDER BY avg_sal DESC;