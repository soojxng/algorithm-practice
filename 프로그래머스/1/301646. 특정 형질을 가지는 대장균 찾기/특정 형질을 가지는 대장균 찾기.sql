-- 코드를 작성해주세요
select
    count(*) as count
from
    ecoli_data
where
    (genotype & 1 > 0 or genotype & 4 > 0) and genotype & 2 = 0;