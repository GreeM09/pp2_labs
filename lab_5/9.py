import re

txt = input()
result = re.findall("[A-Z][a-z]*", txt)
print(' '.join(result))
