-- 코드를 입력하세요
SELECT a.*
FROM places AS a,
    (SELECT host_id
    FROM places
    GROUP BY host_id
    HAVING COUNT(*) >= 2) AS b
WHERE a.host_id = b.host_id
ORDER BY a.id;