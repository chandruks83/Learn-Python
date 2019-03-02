from filecmp import dircmp
def print_diff_files(dcmp):
    for name in dcmp.diff_files:
        print('diff_file '+ name + ' found in ' + dcmp.left + ' and ' + dcmp.right)
    for sub_dcmp in dcmp.subdirs.values():
        print_diff_files(sub_dcmp)

dcmp = dircmp(r'F:\Uttara\Python\NewFolder1', r'F:\Uttara\Python\NewFolder2')
print_diff_files(dcmp)
