from crawler import Crawler
from sys import version_info as v
from sys import exit

if v.major != 3 or v.minor != 9 or v.micro != 1:
    print("Python 3.9.1 is required.")
    exit(1)
else:
    print('success')

c = Crawler(code=66080)
c.go()
