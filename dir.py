# TODO LIST
#implement first two lines of output
#implement collect_data and print_data functions

import os, time, shutil

collect_data = []
print_data = []
dir_order = '{:<21}{:<15}{}'
file_order = '{}{:>18} {}'

print_data.append('\n Directory of ' + os.getcwd() + '\n')

if os.path.abspath(os.pardir) != os.path.abspath(os.sep):
    collect_data = [{'file': os.curdir}, {'file': os.pardir}]

for i in os.listdir('.'):
    if i.startswith('.'):
        continue
    collect_data.append({'file': i})

no_of_directories = 0
total_size_of_files = 0

for j in collect_data:
    path = os.path.abspath(j['file'])
    if j['file'] == os.pardir:
        path = os.getcwd()
    last_mtim = time.localtime(os.path.getmtime(path))
    j['last_mod_time'] = time.strftime('%d-%m-%Y  %H:%M', last_mtim)

    if os.path.isdir(j['file']):
        j['is_directory'] = True
        no_of_directories += 1
        print_data.append(dir_order.format(j['last_mod_time'], '(DIR)', j['file']))
    else:
        j['is_directory'] = False
        j['file_size'] = os.path.getsize(path)
        total_size_of_files += j['file_size']
        print_data.append(file_order.format(j['last_mod_time'], j['file_size'], j['file']))
    j['path'] = path

no_of_files = len(collect_data) - no_of_directories
free_vol_in_drive = shutil.disk_usage('.').free
collect_data.append({'no_of_files': no_of_files,
                     'no_of_directories': no_of_directories,
                     'total_size_of_files': total_size_of_files,
                     'free_vol_in_drive': free_vol_in_drive
                     })

print_data.append('{:>16,} File(s){:>15,} bytes'.format(no_of_files, total_size_of_files))
print_data.append('{:>16,} Dir(s){:>16,} bytes free'.format(no_of_directories, free_vol_in_drive))

for i in print_data:
    print(i)