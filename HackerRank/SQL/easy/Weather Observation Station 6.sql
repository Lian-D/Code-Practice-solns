select distinct s.city
from station s
where SUBSTR(s.city,1,1) IN('A','E','I','O','U')
