import re

txt = input()
result = re.findall(r"ab{0,}", txt)
print(result)
