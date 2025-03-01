import re

txt = input()
result = re.findall(r"ab{2,3}", txt)
print(result)
