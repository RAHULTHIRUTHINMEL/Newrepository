import os

colors = {
    "red" : "\033[91m",
    "base" : "\033[0m"
}




def get_files_path(extension= '.txt'):
    files_path = os.path.join(os.curdir, "words_directory")
    files_full_path = [os.path.join(files_path, f) for f in os.listdir(files_path) if f.endswith(extension)]
    return files_full_path


def find_word_in_files(str_to_find):
    all_files = get_files_path()
    for file in all_files:
        with open(file, 'r') as f:
            lines = f.readlines()
            #print(len(lines))
            for line in lines:
                if str_to_find in line:
                    #print(line)
                    matched_lin_prettifies = line.replace(
                        str_to_find, f"{colors['red']} {str_to_find} {colors['base']}"
                    )
                    print(f"{file} : {matched_lin_prettifies}")


