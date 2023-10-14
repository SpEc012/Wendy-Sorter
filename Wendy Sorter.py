import os
import re
import time
from tkinter import Tk, filedialog
from datetime import datetime
from rgbprint import gradient_scroll, Color, gradient_print

def print_gradient_header():
    header_text = r"""
          _________              __          
         /   _____/ ____________/  |_ ___.__.
         \_____  \ /  _ \_  __ \   __<   |  |
         /        (  <_> )  | \/|  |  \___  |
        /_______  /\____/|__|   |__|  /_____|
                \/                    \/      
    """
    gradient_print(header_text, start_color=Color(238, 93, 108), end_color=Color(206, 73, 147))

def filter_and_sort_lines(lines):
    filtered_lines = [line for line in lines if int(re.search(r'Reward balance: (\d+)', line).group(1)) >= 200]
    sorted_lines = sorted(filtered_lines, key=lambda x: int(re.search(r'Reward balance: (\d+)', x).group(1)))
    return sorted_lines

def select_file():
    Tk().withdraw()  # Prevent a root window from appearing
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

    if not file_path:
        print("[+] No file selected. Exiting...")
        time.sleep(2)  # Delay for 2 seconds before clearing the console
        return

    with open(file_path, 'r') as file:
        lines = file.readlines()

    sorted_lines = filter_and_sort_lines(lines)

    deleted_lines = len(lines) - len(sorted_lines)

    now = datetime.now()
    formatted_date = now.strftime("%Y-%m-%d_%H-%M-%S")
    sorted_file_name = f"sorted_{formatted_date}.txt"

    with open(sorted_file_name, 'w') as sorted_file:
        sorted_file.writelines(sorted_lines)

    print(f"[+] Deleted {deleted_lines} lines. Sorted file saved as {sorted_file_name}.")
    time.sleep(2)  # Delay for 2 seconds before clearing the console

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
        print_gradient_header()  # Print the gradient header

        gradient_print("[+] 1. Open Wendys.txt to sort", start_color=Color(238, 93, 108), end_color=Color(206, 73, 147))
        gradient_print("[+] 2. Exit", start_color=Color(238, 93, 108), end_color=Color(206, 73, 147))

        choice = input("[>] Enter your choice: ")

        if choice == '1':
            select_file()
        elif choice == '2':
            break
        else:
            print("[!] Invalid choice. Please try again.")
            time.sleep(2)  # Delay for 2 seconds before clearing the console

if __name__ == "__main__":
    main()
