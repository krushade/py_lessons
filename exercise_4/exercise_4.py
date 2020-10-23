import os


path = os.path.realpath(__file__)
dir_name = os.path.dirname(path)
list_dir = os.listdir(dir_name)
sort_list = []


def sh(files):
<<<<<<< HEAD
    for line in files:
        splt = line.splitlines()
        for s in splt:
            sh_str = s.split('/')
            for t in sh_str:
                if t.endswith('.sh'):
                    with open('sorted_sh.txt', 'a') as sorted_files:
                        sorted_files.write(f"{t}\n")

=======
        for line in files:
            splt = line.splitlines()
            for s in splt:
                sh_str = s.split('/')
                for t in sh_str:
                    if t.endswith('.sh'):
                        with open('sorted_sh.txt', 'a') as sorted_files:
                            sorted_files.write(f"{t}\n")
>>>>>>> 9a959e176bc36c82cd6cbfb703d93e9f9bc2a60f

if __name__ == '__main__':
    for x in list_dir:
        if x.endswith('job'):
            sort_list.append(x)

if __name__ == '__main__':
    for x in list_dir:
    if x.endswith('job'):
        sort_list.append(x)


    for job_file in sort_list:
        with open(job_file, 'r') as file:
            sh(file)
