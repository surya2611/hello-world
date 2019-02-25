# TODO LIST
#implement collect_data and print_data functions
import os, time, shutil

class Path:
    def __init__(self):
        pass

    def name(self, path):
        return os.path.basename(path)

    def last_modified_time(self, path):
        return time.strftime('%d-%m-%Y  %H:%M', time.localtime(os.path.getmtime(path)))

    def is_directory(self, path):
        return os.path.isdir(path)

    def is_file(self, path):
        return os.path.isfile(path)

    def files(self):
        return len([i for i in os.listdir('.') if not i.startswith('.') and self.is_file(i)])

    def directories(self):
        return len([i for i in os.listdir('.') if not i.startswith('.') and self.is_directory(i)]) + 2

    def size(self, path):
        if self.is_file(path):
            return os.stat(path).st_size

    def children(self):
        return [i for i in os.listdir('.') if not i.startswith('.')]

    def parent(self):
        return [i for i in os.path.abspath('.').split('\\')]

cwd = Path()
free_vol_in_drive = shutil.disk_usage('.').free
total_size_of_files = sum([cwd.size(i) for i in cwd.children() if cwd.is_file(i)])
def print_cwd_data():
    dir_order = '{:<21}{:<15}{}'
    file_order = '{}{:>18,} {}'
    print('\n Directory of ' + os.getcwd() + '\n')
    if len(cwd.parent()) > 1:
        print(dir_order.format(cwd.last_modified_time('.'), '(DIR)', '.'))
        print(dir_order.format(cwd.last_modified_time('.'), '(DIR)', '..'))
    for i in cwd.children():
        if cwd.is_directory(i):
            print(dir_order.format(cwd.last_modified_time(i), '(DIR)', cwd.name(i)))
        else:
            print(file_order.format(cwd.last_modified_time(i), cwd.size(i), cwd.name(i)))
    print('{:>16,} File(s){:>15,} bytes'.format(cwd.files(), total_size_of_files))
    print('{:>16,} Dir(s){:>16,} bytes free'.format(cwd.directories(), free_vol_in_drive))

print(print_cwd_data())