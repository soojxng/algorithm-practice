-- 코드를 입력하세요
SELECT a.category, a.price AS max_price, a.product_name
FROM food_product AS a,
    (SELECT category, MAX(price) AS max_price
    FROM food_product
    WHERE category IN ('과자', '국', '김치', '식용유')
    GROUP BY category) AS b
WHERE a.category = b.category AND a.price = b.max_price
ORDER BY a.price DESC;