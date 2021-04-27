
def write_file(code:str, fileName = 'verilog.txt'):
    print("Writing a file..")
    try:
        f = open(fileName, "a")
        f.write(code)
        f.close()
    except Exception:
        print("Error, Could not write to file")


def read_file(fileName = 'verilog.txt'):
    print("Now reading the file..")
    try:
        f = open(fileName, "r")
        for line in f.readlines():
            print(line)
        f.close()
    except Exception:
        print("Error, Could not read to file")