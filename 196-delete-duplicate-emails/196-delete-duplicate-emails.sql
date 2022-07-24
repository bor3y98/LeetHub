# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below
# select email from Person group by email having count(email) > 1 
# DELETE from Person where id=1
delete from Person where id not in (select * from (select  Min(id) from Person group by email having count(email)>=1)as e)
