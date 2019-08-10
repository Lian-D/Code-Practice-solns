select distinct s.city
from station s
where SUBSTR(s.city,length(s.city),length(s.city)) NOT IN('A','E','I','O','U') or SUBSTR(s.city,1,1) NOT IN('A','E','I','O','U')
