#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    directories = dir(hidden_4)

    for directory in directories:
        if directory[:2] != "__":
            print(directory)
