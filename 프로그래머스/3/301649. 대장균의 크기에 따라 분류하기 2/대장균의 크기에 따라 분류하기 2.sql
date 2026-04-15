SELECT E.id,
    CASE
        WHEN E.p <= 0.25 THEN 'CRITICAL'
        WHEN E.p <= 0.5 THEN 'HIGH'
        WHEN E.p <= 0.75 THEN 'MEDIUM'
        ELSE 'LOW'
    END AS colony_name
FROM(
    SELECT id, percent_rank() OVER (ORDER BY size_of_colony DESC) AS p
    FROM ecoli_data
) AS E
ORDER BY E.id;