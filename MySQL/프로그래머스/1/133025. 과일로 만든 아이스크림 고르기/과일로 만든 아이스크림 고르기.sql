-- 코드를 입력하세요
SELECT i.FLAVOR
from FIRST_HALF h join ICECREAM_INFO i
on h.FLAVOR = i.FLAVOR
and h.TOTAL_ORDER > 3000
where i.INGREDIENT_TYPE="fruit_based"
order by TOTAL_ORDER desc