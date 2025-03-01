import re

txt = input()
result = re.findall(r"[A-Z][a-z]", txt)
print(result)
