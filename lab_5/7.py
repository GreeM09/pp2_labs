import re

txt = input()
print(''.join(x.capitalize() or '_' for x in txt.split('_')))
