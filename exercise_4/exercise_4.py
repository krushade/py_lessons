import os
path = os.path.realpath(__file__)
dir_name = os.path.dirname(path)
list_dir = os.listdir(dir_name)
sort_list = []

for x in list_dir:
    if x.endswith('job'):
        sort_list.append(x)


if __name__ == '__main__':

    def sh(files):
        for line in files:
            splt = line.splitlines()
            for s in splt:
                sh_str = s.split('/')
                for t in sh_str:
                    if t.endswith('.sh'):
                        with open('sorted_sh.txt', 'a') as sorted_files:
                            sorted_files.write(f"{t}\n")


    for job_file in sort_list:
        with open(job_file, 'r') as file:
            sh(file)
