import re
s=raw_input()
n=re.sub('[\w]+','', s)
print(len(n))
