-- 코드를 입력하세요
SELECT  SUM(COUNT) AS count
FROM    (
    SELECT  COUNT(*) AS COUNT
    FROM    ANIMAL_INS
    GROUP BY ANIMAL_ID
    ) AS GROUP_TABLE