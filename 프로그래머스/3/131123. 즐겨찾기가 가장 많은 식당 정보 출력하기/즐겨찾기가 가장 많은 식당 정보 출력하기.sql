-- 코드를 입력하세요
SELECT i.food_type, i.rest_id, i.rest_name, i.favorites
FROM rest_info AS i,
    (SELECT food_type, MAX(favorites) AS fav
     FROM rest_info
     GROUP BY food_type
     ) AS m
WHERE i.food_type = m.food_type AND i.favorites = m.fav
ORDER BY food_type DESC;