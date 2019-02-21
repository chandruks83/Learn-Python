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
