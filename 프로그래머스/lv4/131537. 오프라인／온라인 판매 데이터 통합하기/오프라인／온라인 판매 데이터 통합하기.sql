# -- 코드를 입력하세요
# SELECT SALES_DATE, PRODUCT_ID, NULL AS USER_ID, SALES_AMOUNT
# FROM OFFLINE_SALE 
# WHERE SALES_DATE BETWEEN '2022-03-01' AND '2022-04-01'

# UNION ALL

# SELECT SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
# FROM ONLINE_SALE 
# WHERE SALES_DATE BETWEEN '2022-03-01' AND '2022-04-01'
# ORDER BY SALES_DATE, PRODUCT_ID ASC, USER_ID ASC;

select date_format(sales_date, '%Y-%m-%d') as sales_date, product_id, user_id, sales_amount
from online_sale
where sales_date >= '2022-03-01' and sales_date < '2022-04-01'

union all

select date_format(sales_date, '%Y-%m-%d') as sales_date, product_id, NULL as user_id, sales_amount
from offline_sale
where sales_date >= '2022-03-01' and sales_date < '2022-04-01'

order by sales_date, product_id, user_id