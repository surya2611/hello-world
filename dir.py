import os, time, shutil

file = [os.getcwd(), os.path.abspath(os.pardir)]
output = []
total_size_of_files = no_of_directories = 0
name = ''

for i in os.listdir('.'):
    if i.startswith('.'):
        continue
    file.append(os.path.realpath(i))

for j in file:

    last_mtim = time.localtime(os.path.getmtime(j))
    f_time = time.strftime('%d-%m-%Y  %H:%M', last_mtim)

    if os.path.isdir(j):
        no_of_directories += 1
        if j == os.getcwd():
            name = '.'
            cwd_last_mtime = f_time
        elif j == os.path.abspath(os.pardir):
            name = '..'
            f_time = cwd_last_mtime
        else:
            name = os.path.basename(j)
        output.append('{:<20} {:<15}{}'.format(f_time, '(DIR)', name))
    else:
        total_size_of_files += os.path.getsize(j)
        output.append('{:<20} {:>14,} {}'.format(f_time, os.path.getsize(j), os.path.basename(j)))

no_of_files = len(file) - no_of_directories
print(' Volume in drive is')
print(' Volume Serial Number is')
print('\n Directory of ' + file[0] + '\n')
for i in output:
    print(i)
print('{:>16,} File(s){:>15,} bytes'.format(no_of_files, total_size_of_files))
print('{:>16,} Dir(s){:>16,} bytes free'.format(no_of_directories, shutil.disk_usage('.').free))