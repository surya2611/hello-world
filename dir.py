# TODO LIST
#implement first 2 lines of the program
#implement collect_data and print_data functions
import os, time, shutil, sys

class Path:
    def __init__(self, path):
        self.path = path

    def name(self):
        return os.path.basename(self.path)

    def last_modified_time(self):
        return time.strftime('%d-%m-%Y  %H:%M', time.localtime(os.path.getmtime(self.path)))

    def is_directory(self):
        return os.path.isdir(self.path)

    def is_file(self):
        return os.path.isfile(self.path)

    def files(self):
        return [i for i in self.children() if Path(i).is_file()]

    def directories(self):
        return [i for i in self.children() if Path(i).is_directory()]

    def size(self):
        if self.is_file():
            return os.stat(self.path).st_size

    def children(self):
        if self.is_directory():
            return [i for i in os.listdir(self.path) if not i.startswith('.')]

    def parent(self):
        return os.pardir

cwd = Path('.')

if len(sys.argv) is 2:
    if os.path.isdir('./' + sys.argv[1]):
        os.chdir('./' + sys.argv[1])
    else:
        cwd = Path('./' + sys.argv[1])

cwd.free_vol_in_drive = shutil.disk_usage('.').free
if cwd.is_directory():
    cwd.no_of_files = len(cwd.files())
    cwd.total_size_of_files = sum([Path(file).size() for file in cwd.files()])
    if cwd.parent():
        cwd.no_of_directories = len(cwd.directories()) + 2
    else:
        cwd.no_of_directories = len(cwd.directories())
else:
    cwd.no_of_files = 1
    cwd.total_size_of_files = cwd.size()
    cwd.no_of_directories = 0

def print_dir_data(cwd):
    dir_order = '{:<21}{:<15}{}'
    file_order = '{}{:>18,} {}'
    print('\n Directory of ' + os.getcwd() + '\n')
    if cwd.is_directory():
        if cwd.parent():
            print(dir_order.format(cwd.last_modified_time(), '<DIR>', cwd.name()))
            print(dir_order.format(cwd.last_modified_time(), '<DIR>', cwd.parent()))
        for i in cwd.children():
            if Path(i).is_directory():
                print(dir_order.format(Path(i).last_modified_time(), '<DIR>', Path(i).name()))
            else:
                print(file_order.format(Path(i).last_modified_time(), Path(i).size(), Path(i).name()))
    else:
        print(file_order.format(cwd.last_modified_time(), cwd.size(), cwd.name()))
    print('{:>16,} File(s){:>15,} bytes'.format(cwd.no_of_files, cwd.total_size_of_files))
    print('{:>16,} Dir(s){:>16,} bytes free'.format(cwd.no_of_directories, cwd.free_vol_in_drive))

print_dir_data(cwd)