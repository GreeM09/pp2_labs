import re

txt = input()
result = re.findall(r"[a-z]+_[a-z]+", txt)
print(result)
