# TODO LIST
#implement first two lines of output
#implement collect_data and print_data functions

import os, time, shutil

def collect_data():
#collects the data of current directory

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
        else:
            j['is_directory'] = False
            j['file_size'] = os.path.getsize(path)
            total_size_of_files += j['file_size']
        j['path'] = path

    no_of_files = len(collect_data) - no_of_directories
    free_vol_in_drive = shutil.disk_usage('.').free
    collect_data.append({'no_of_files': no_of_files,
                         'no_of_directories': no_of_directories,
                         'total_size_of_files': total_size_of_files,
                         'free_vol_in_drive': free_vol_in_drive
                         })
    return collect_data

def print_data(collect_data):
    #prints the data of current directory

    i=0
    dir_order = '{:<21}{:<15}{}'
    file_order = '{}{:>18} {}'

    print('\n Directory of ' + os.getcwd() + '\n')
    while i < (len(collect_data)-1):
        if collect_data[i]['is_directory']:
            print(dir_order.format(collect_data[i]['last_mod_time'], '(DIR)', collect_data[i]['file']))
        else:
            print(file_order.format(collect_data[i]['last_mod_time'], collect_data[i]['file_size'], collect_data[i]['file']))
        i += 1

    print('{:>16,} File(s){:>15,} bytes'.format(collect_data[i]['no_of_files'], collect_data[i]['total_size_of_files']))
    print('{:>16,} Dir(s){:>16,} bytes free'.format(collect_data[i]['no_of_directories'], collect_data[i]['free_vol_in_drive']))

data = collect_data()
print_data(data)