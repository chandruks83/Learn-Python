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

#Grouping of strings
getphone = re.compile(r'\+(\d\d)\-(\d\d\d\d\d\d\d\d\d\d)')
phone = getphone.search(str1)
print(phone.group(1))
print(phone.group(2))

#using pipe character
regexWithpipe = re.compile(r'Bat(man|mobile|woman)')
mo = regexWithpipe.search('Batwoman came to rescue and Batman followed')
print(mo.group())