-- 코드를 입력하세요
SELECT DISTINCT car_id, IF(car_id in (SELECT car_id
                            FROM car_rental_company_rental_history
                            WHERE start_date <= '2022-10-16' AND end_date >= '2022-10-16'),
                 '대여중', '대여 가능') AS availability
FROM car_rental_company_rental_history
ORDER BY car_id DESC;