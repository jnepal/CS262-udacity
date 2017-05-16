import re

print(re.findall('[0-9]', "11-7"))


print(re.findall(r'[a|b]|[0-9]+', "abc 123"))

#Regex for expression a, a-b, abc but not others a-b-c
print(re.findall('[a-z]-[a-z]', 'a-b'))

#Regex for function like sqrt(2) or sqrt( 2 )

print(re.findall('[a-z]+[\(][ ]*[0-9]+[ ]*[\)]', "sqrt( 2 )"))


# print(re.findall('[mi|re|do]+', "mimi rere midore doo-woop "))
print(re.findall('(mi|re|do)+', "mimi rere midore doo-woop ")) #doesn't work
print(re.findall('(?: do|re|mi)+', "mimi rere midore doo-woop"))

#Regex for
string1 = '"I say, \\"hello\\""' #(accept)
string2 = '\\' #reject

#["][a-z]*[][a-z]*[,][\]["][a-z]*[\]["]

#backslash should be escaped
regex = r'"(?:[^\\]|(?:\\.))*"'
print(re.findall(regex, string1))

# regex = r'<!--[a-zA-z0-9 ]*(?:-->'
# print(re.findall(regex, '<!--This is a comment--> hello'))
