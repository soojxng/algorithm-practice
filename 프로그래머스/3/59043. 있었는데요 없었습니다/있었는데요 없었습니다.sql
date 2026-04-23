-- 코드를 입력하세요
SELECT i.animal_id, i.name
FROM animal_ins as i, animal_outs as o
WHERE i.animal_id = o.animal_id and i.datetime > o.datetime
ORDER BY i.datetime;