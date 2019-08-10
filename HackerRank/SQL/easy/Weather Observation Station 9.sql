select distinct s.city
from station s
where SUBSTR(s.city,1,1) NOT IN('A','E','I','O','U')
