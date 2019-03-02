import filecmp
x = filecmp.dircmp(r'F:\Uttara\Python\NewFolder1', r'F:\Uttara\Python\NewFolder2')
x.report()
print('*******')
x.report_partial_closure()
print('*******')
x.report_full_closure()
print('*******')
