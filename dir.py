# TODO LIST
#implement first two lines of output
#implement collect_data and print_data functions

import os, time, shutil

class path:

    def info(path):
        data = {}
        data['name'] = os.path.basename(path)
        if os.path.isdir(path):
            data['field'] = 'DIR'
        else:
            data['field'] = 'FILE'
            data['file_size'] = os.path.getsize(path)
        data['last_mod_time'] = time.strftime('%d-%m-%Y  %H:%M', time.localtime(os.path.getmtime(path)))
        return data

    def print_cwd_data():
        dir_order = '{:<21}{:<15}{}'
        file_order = '{}{:>18,} {}'
        print('\n Directory of ' + os.getcwd() + '\n')
        for i in path.data:
            if i['name'] == os.pardir:
                continue
            if i['field'] is 'DIR':
                print(dir_order.format(i['last_mod_time'], '(DIR)', i['name']))
                if i['name'] is os.curdir:
                    print(dir_order.format(i['last_mod_time'], '(DIR)', os.pardir))
            else:
                print(file_order.format(i['last_mod_time'], i['file_size'], i['name']))
        print('{:>16,} File(s){:>15,} bytes'.format(path.no_of_files, path.total_size_of_files))
        print('{:>16,} Dir(s){:>16,} bytes free'.format(path.no_of_directories, path.free_vol_in_drive))

    data = []
    no_of_files = no_of_directories = total_size_of_files = 0
    free_vol_in_drive = shutil.disk_usage('.').free
    if os.path.abspath(os.pardir) is not os.path.abspath(os.sep):
        data.extend([info('.'), info('..')])
    for i in os.listdir('.'):
        if not i.startswith('.'):
             data.append(info(os.path.abspath(i)))
    for i in data:
        if i['field'] is 'FILE':
            no_of_files += 1
            total_size_of_files += i['file_size']
    no_of_directories = len(data) - no_of_files

path.print_cwd_data()