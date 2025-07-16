-- 코드를 작성해주세요
select count(*) as FISH_COUNT, N.FISH_NAME
from FISH_NAME_INFO AS N
join FISH_INFO AS I
on N.FISH_TYPE = I.FISH_TYPE
group by N.FISH_NAME
order by FISH_COUNT DESC;