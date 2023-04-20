import os.path as osp
import time

TODO_FILENAME = "todo_list.txt"


def get_current_timestamp():
    return time.strftime("%Y-%m-%d, %H:%M:%S")


def show_list(entries_list: str) -> None:
    print("Current tasks:")
    for i, entry in enumerate(entries_list):
        print(f"\t{i + 1}: {entry}")
    print('')


def input_to_int(user_input: str, array_len=1) -> int:
    try:
        user_input = int(user_input)
        if array_len == 1:
            return user_input
        else:
            if 1 <= user_input <= array_len:
                return user_input
            else:
                print(f"Error: user input is outside of [1, {array_len}] range")
                return 0
    except ValueError:
        print(f"Error: '{user_input}' is not an integer")
        return -1


def read_todo_file(filename=TODO_FILENAME):
    data = []
    if osp.exists(filename):
        with open(filename, 'r') as f:
            timestamp = f.readline()
            for line in f.readlines():
                data.append(line.strip('\n'))
            return data, timestamp


def write_todo_file(data: list, filename=TODO_FILENAME):
    with open(filename, 'w') as f:
        f.writelines(get_current_timestamp() + '\n')
        f.writelines('\n'.join(data))
