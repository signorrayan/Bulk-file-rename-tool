import os
from colorama import Fore, Style


def main():
    path = str(input("Enter the directory that you want to rename files in that: "))
    while not os.path.isdir(path):
        print(f"{Fore.RED}Enter the correct path!{Style.RESET_ALL}")
        path = str(input("Enter the directory that you want to rename files in that: "))
        
    os.chdir(path)
    pattern = str(input("Enter your pattern for name: "))
    given_ext = str(input("Enter the specific file extension you want to change their names: "))

    index = 0
    for f in sorted(os.listdir()):
        file_ext = os.path.splitext(f)[1] # to split the filename and its extension. Exp: [filename, .txt]
        if file_ext == given_ext:
            new_name = f"{pattern}{str(index).zfill(2)}{file_ext}"
            os.rename(f, new_name)
            index += 1
        else:
            continue
    print(f"{Fore.GREEN}Process finished.{Style.RESET_ALL}")


if __name__ == '__main__':
    main()
