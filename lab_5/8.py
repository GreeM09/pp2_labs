import re

txt = input()
result = re.findall("[A-Z][^A-Z]*", txt)
print(result)
