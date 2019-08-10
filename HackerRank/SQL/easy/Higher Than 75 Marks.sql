select s.name
from students s
where s.marks > 75
order by RIGHT(NAME, 3), s.id asc
