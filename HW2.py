import sys
from pathlib import Path

def sort_file(path, file_type_dict):
    all_file_set = set()
    for element in path.iterdir():
        if element.is_file():
            all_file_set.add(element.name)
            for key in file_type_dict:
                if element.name.rsplit('.', 2)[-1] in set(key):
                    file_type_dict[key].append(element.name)
                file_type_dict[('unknown', )].extend(
                    all_file_set - set(file_type_dict[key]))
        else:
            sort_file(element, file_type_dict)
    return file_type_dict


def output_result_sort(file_type_dict):
    for key, value in file_type_dict.items():
        title_string = str(key).center(78, '-')
        print(title_string)
        for file in value:
            print(file)
    unknown_type_files = []
    for unknown_file in file_type_dict[('unknown', )]:
        unknown_type_files.append(unknown_file.rsplit('.', 2)[-1])

    print(' unknown type '.center(78, '-'))
    print(set(unknown_type_files))


def main():
    file_type_dict = {
        ('jpeg', 'png', 'jpg', 'svg'): [],
        ('avi', 'mp4', 'mov', 'mkv'): [],
        ('doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx'): [],
        ('mp3', 'ogg', 'wav', 'amr'): [],
        ('zip', 'gz', 'tar'): [],
        ('unknown', ): []
    }
    if len(sys.argv) <= 1:
        path = Path('')
    else:
        path = Path(sys.argv[1])
    if path.exists():
        if path.is_dir:
            file_type_dict = sort_file(path, file_type_dict)
            output_result_sort(file_type_dict)
        else:
            print(f'{path.absolute} is file')

    else:
        print(f'path {path.absolute()} not exist')


if __name__ == '__main__':
    main()