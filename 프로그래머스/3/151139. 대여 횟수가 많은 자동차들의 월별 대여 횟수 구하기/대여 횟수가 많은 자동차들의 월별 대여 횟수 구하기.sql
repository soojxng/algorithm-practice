-- 코드를 입력하세요
SELECT MONTH(a.start_date) AS month, a.car_id, COUNT(*) AS records
FROM car_rental_company_rental_history AS a, (SELECT car_id
      FROM car_rental_company_rental_history
      WHERE start_date >= '2022-08-01' AND start_date <= '2022-10-31'
      GROUP BY car_id
      HAVING COUNT(*) >= 5) AS b
WHERE a.car_id = b.car_id AND start_date >= '2022-08-01' AND start_date <= '2022-10-31'
GROUP BY a.car_id, month
ORDER BY month, a.car_id DESC;