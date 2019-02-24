#Regular expression
str1 = "My Phone number is +91-9889889889 \
           Shilpa's number +91-9986998699"
import re
getphone = re.compile(r'\+\d\d\-\d\d\d\d\d\d\d\d\d\d')
phone = getphone.search(str1)
#Search for one element
print(phone.group())

#Search for all the elements
print(getphone.findall(str1))

#Grouping of strings using brackets
getphone = re.compile(r'\+(\d\d)\-(\d\d\d\d\d\d\d\d\d\d)')
phone = getphone.search(str1)
print(phone.group(1))
print(phone.group(2))

#using pipe character, match any one of the strings
regexWithpipe = re.compile(r'Bat(man|mobile|woman)')
mo = regexWithpipe.search('Batwoman came to rescue and Batman followed')
print(mo.group())

#match 0 or one time using ?
regexp = re.compile(r'Bat(wo)?man')
mo = regexp.search('I am a Batman with a Batwoman')
print(mo.group())

rx = re.compile(r'(\d\d-)?\d\d\d\d\d\d\d\d\d\d')
mo = rx.search('91-9886688660')
print(mo.group())
mo = rx.search('9886688660')
print(mo.group())