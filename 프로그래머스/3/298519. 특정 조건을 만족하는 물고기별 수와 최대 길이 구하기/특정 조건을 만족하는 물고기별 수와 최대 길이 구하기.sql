-- 코드를 작성해주세요
select count(*) as FISH_COUNT, max(LENGTH) as MAX_LENGTH, FISH_TYPE
from FISH_INFO
group by FISH_TYPE
having avg(ifnull(LENGTH, 10)) >= 33
ORDER BY FISH_TYPE;