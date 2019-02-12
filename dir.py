# TODO LIST
#implement code for the case of not having parent directory
#implement first two lines of output
#separate computing logic from printing logic

import os, time, shutil

output = []
output.append('\n Directory of ' + os.getcwd() + '\n')
if os.path.abspath(os.pardir) != os.path.abspath(os.sep):
    file = [os.curdir, os.pardir]


for i in os.listdir('.'):
    if i.startswith('.'):
        continue
    file.append(i)

total_size_of_files = no_of_directories = 0
name = ''

for j in file:
    path = os.path.abspath(j)
    if j == os.pardir:
        path = os.getcwd()
    last_mtim = time.localtime(os.path.getmtime(path))
    f_time = time.strftime('%d-%m-%Y  %H:%M', last_mtim)

    if os.path.isdir(j):
        no_of_directories += 1
        output.append('{:<20} {:<15}{}'.format(f_time, '(DIR)', j))
    else:
        total_size_of_files += os.path.getsize(j)
        output.append('{:<20} {:>14,} {}'.format(f_time, os.path.getsize(j), os.path.basename(j)))

no_of_files = len(file) - no_of_directories

output.append('{:>16,} File(s){:>15,} bytes'.format(no_of_files, total_size_of_files))
output.append('{:>16,} Dir(s){:>16,} bytes free'.format(no_of_directories, shutil.disk_usage('.').free))

for i in output:
    print(i)