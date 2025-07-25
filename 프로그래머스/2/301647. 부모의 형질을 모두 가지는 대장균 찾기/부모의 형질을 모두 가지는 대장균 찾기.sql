SELECT a.id, a.genotype, b.genotype as parent_genotype
FROM ecoli_data as a, ecoli_data as b
WHERE a.parent_id = b.id AND a.genotype & b.genotype = b.genotype
order by id