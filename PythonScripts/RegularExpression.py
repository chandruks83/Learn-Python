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

Character classes

Shorthand character class Represents

\d = Any numeric digit from 0 to 9.

\D = Any character that is not a numeric digit from 0 to 9.

\w = Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)

\W = Any character that is not a letter, numeric digit, or the underscore character.

\s = Any space, tab, or newline character. (Think of this as matching “space” characters.)

\S = Any character that is not a space, tab, or newline.

The findall() method returns all matching strings of the regex pattern in a list

rx = re.compile(r'\d+\s\w+')
rx.findall('12 drummers, 11 pipers, 2 piannos')
['12 drummers', '11 pipers', '2 piannos']

Making Your Own Character Classes

There are times when you want to match a set of characters but the shorthand character classes (\d, \w, \s, and so on) are too broad. You can define your own character class using square brackets. For example, the character class [aeiouAEIOU] will match any vowel, both lowercase and uppercase

By placing a caret character (^) just after the character class’s opening bracket, you can make a negative character class

rx = re.compile(r'[aeiouAEIOU]')
rx.findall('Robocop eats baby food. BABY FOOD')
['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']

#ignore case
rx = re.compile(r'[aeiou]',re.I)
rx.findall('Robocop eats baby food. BABY FOOD')
['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']

rx = re.compile(r'[^aeiouAEIOU]')
rx.findall('Robocop eats baby food. BABY FOOD')
['R', 'b', 'c', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', ' ', 'B', 'B', 'Y', ' ', 'F', 'D']

You can also include ranges of letters or numbers by using a hyphen. For example, the character class [a-zA-Z0-9] will match all lowercase letters, uppercase letters, and numbers

The Caret and Dollar Sign Characters

You can also use the caret symbol (^) at the start of a regex to indicate that a match must occur at the beginning of the searched text. Likewise, you can put a dollar sign ($) at the end of the regex to indicate the string must end with this regex pattern.

rx = re.compile(r'^hello')
rx.search('hello world')
<re.Match object; span=(0, 5), match='hello'>

rx = re.compile('world$')
rx.search('hello world')
<re.Match object; span=(6, 11), match='world'>

rx = re.compile('^Hello world$')
rx.search('Hello this is the real world')

rx = re.compile(r'^\d+$')
rx.search('123456')
<re.Match object; span=(0, 6), match='123456'>

rx = re.compile(r'.at')
rx.findall('The cat in the hat sat on the flat mat')
['cat', 'hat', 'sat', 'lat', 'mat']

The Wildcard Character

The . (or dot) character in a regular expression is called a wildcard and will match any character except for a newline

rx = re.compile(r'.{1,2}at')
rx.findall('The cat in the hat sat on the flat mat')
[' cat', ' hat', ' sat', 'flat', ' mat']

rx = re.compile(r'First name : (.*) Last name : (.*)')
rx.findall('First name : chandra Last name : kanth')
[('chandra', 'kanth')]