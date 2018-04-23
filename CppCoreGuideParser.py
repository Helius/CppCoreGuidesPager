#!/usr/bin/python3
import re

#https://raw.githubusercontent.com/isocpp/CppCoreGuidelines/master/CppCoreGuidelines.md

# use github api to render .md file
# curl https://api.github.com/markdown/raw -X "POST" -H "Content-Type: text/plain" --data-binary "@rule.md" > tmp.html

f = open('CppCoreGuidelines.md', 'r')
text = f.read()

items = re.split('###\s<a', text)
print(len(items))
print(items[31])
