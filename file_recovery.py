import os

def read_recovery_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            print(file.read().splitlines())
            return file.read().splitlines()
    return []

def write_recovery_file(file_path, urls):
    with open(file_path, 'w') as file:
        for url in urls:
            file.write(f'{url}\n')