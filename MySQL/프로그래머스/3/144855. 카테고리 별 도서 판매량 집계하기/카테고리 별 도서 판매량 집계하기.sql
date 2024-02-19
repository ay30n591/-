-- 코드를 입력하세요
SELECT a.CATEGORY ,sum(b.SALES) as'TOTAL_SALES' 
# , sum(a.PRICE) as 'TOTAL_SALES'
from BOOK a join BOOK_SALES b
on a.BOOK_ID=b.BOOK_ID
where SALES_DATE like '2022-01%'
group by a.CATEGORY
order by a.CATEGORY;