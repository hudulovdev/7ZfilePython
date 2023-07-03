import py7zr

def create_7z(file_paths, output_file):
    with py7zr.SevenZipFile(output_file, 'w') as archive:
        for file_path in file_paths:
            archive.write(file_path)

# Example usage:
file_paths = ['file1.txt', 'file2.txt', 'file3.txt']
output_file = 'archive.7z'

create_7z(file_paths, output_file)
