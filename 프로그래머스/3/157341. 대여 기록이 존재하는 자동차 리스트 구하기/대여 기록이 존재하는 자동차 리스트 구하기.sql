-- 코드를 입력하세요
SELECT DISTINCT c.car_id
FROM car_rental_company_car AS c, car_rental_company_rental_history AS h
WHERE c.car_id = h.car_id AND c.car_type = '세단' AND MONTH(h.start_date) = 10
ORDER BY car_id DESC;