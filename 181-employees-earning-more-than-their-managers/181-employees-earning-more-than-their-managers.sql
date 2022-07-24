
# select name as Employee from Employee as e1 where e1.salary> (select salary from Employee as e2 where e2.id =e1.managerId )

select e1.name as Employee from Employee as e1 
INNER JOIN Employee as e2
ON e1.managerId = e2.id AND e1.salary > e2.salary