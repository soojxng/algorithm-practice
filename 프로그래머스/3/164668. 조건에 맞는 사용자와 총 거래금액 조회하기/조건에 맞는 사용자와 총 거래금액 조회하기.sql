-- 코드를 입력하세요
SELECT u.user_id, u.nickname, b.total_sales
FROM used_goods_user AS u, 
    (SELECT writer_id, SUM(price) AS total_sales
     FROM used_goods_board as ugb
     WHERE ugb.status = 'done'
     GROUP BY writer_id
    ) AS b
WHERE u.user_id = b.writer_id AND b.total_sales >= 700000
ORDER BY b.total_sales ASC;
