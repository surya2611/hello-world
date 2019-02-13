# TODO LIST
#implement first two lines of output
#implement collect_data and print_data functions

import os, time, shutil

collect_data = {'file': [], 'path': [], 'last_mod_time': [], 'is_directory': [], 'file_size': []}
print_data = []
dir_order = '{:<21}{:<15}{}'
file_order = '{}{:>18} {}'

print_data.append('\n Directory of ' + os.getcwd() + '\n')

if os.path.abspath(os.pardir) != os.path.abspath(os.sep):
    file = [os.curdir, os.pardir]

for i in os.listdir('.'):
    if i.startswith('.'):
        continue
    file.append(i)

collect_data['file'] = file

no_of_directories = 0

for j in file:
    path = (os.path.abspath(j))
    collect_data['path'].append(path)
    if j == os.pardir:
        path = os.getcwd()
    last_mtim = time.localtime(os.path.getmtime(path))
    last_mod_time = (time.strftime('%d-%m-%Y  %H:%M', last_mtim))
    collect_data['last_mod_time'].append(last_mod_time)

    if os.path.isdir(j):
        collect_data['is_directory'].append(True)
        no_of_directories += 1
        collect_data['file_size'].append(0)
        print_data.append(dir_order.format(last_mod_time, '(DIR)', j))
    else:
        collect_data['is_directory'].append(False)
        file_size = os.path.getsize(path)
        collect_data['file_size'].append(file_size)
        print_data.append(file_order.format(last_mod_time, file_size, j))

no_of_files = len(file) - no_of_directories
total_size_of_files = sum(collect_data['file_size'])

print_data.append('{:>16,} File(s){:>15,} bytes'.format(no_of_files, total_size_of_files))
print_data.append('{:>16,} Dir(s){:>16,} bytes free'.format(no_of_directories, shutil.disk_usage('.').free))

for i in print_data:
    print(i)