fso = open(r'F:\Uttara\Python\NewFolder\Hello.txt', 'w')
fso.write('Hey there, new content\n')
fso.close()
fso = open(r'F:\Uttara\Python\NewFolder\Hello.txt', 'a')
fso.write('Hey there again, new content')
fso.close()