import re

pat = r"(?<=\w)([^\w]+)(?=\w)"

text="This$#is% Matrix#  %!"

c = re.compile(pat)
result = c.sub(" ",text)

print(result)


