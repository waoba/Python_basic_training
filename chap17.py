import re

text="The Ghost that says boo haunts the loo. then he says o"

m=re.findall(".oo",text)
print(m)
