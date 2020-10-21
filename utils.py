import os


def create_project_dir(directory):
    if not os.path.exists(directory):
        print('[-] Crating project directory: ' + directory)
        os.makedirs(directory)


def write_list_to_file(filename, list):
    print("[-] Writing results to file: ", filename)
    with open(str(filename), 'wt') as f:
        for e in list:
            f.write(e + os.linesep)


def delete_file_contents(path):
    open(path, 'w').close()

