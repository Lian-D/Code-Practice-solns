select distinct s.city
from station s
where SUBSTR(s.city,length(s.city),length(s.city)) IN('A','E','I','O','U') and SUBSTR(s.city,1,1) IN('A','E','I','O','U')
