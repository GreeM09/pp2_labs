import re

txt = input()
result = re.findall(r"a.+b$", txt)
print(result)
