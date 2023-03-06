-- 코드를 입력하세요
SELECT  INGREDIENT_TYPE, SUM(TOTAL_ORDER) AS TOTAL_ORDER
FROM    (
    SELECT  *
    FROM    FIRST_HALF
    INNER JOIN  ICECREAM_INFO
    USING   (FLAVOR)
) AS JOIN_TABLE
GROUP BY    INGREDIENT_TYPE
ORDER BY    TOTAL_ORDER ASC