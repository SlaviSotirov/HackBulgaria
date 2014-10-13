import sys


def main():
    result_filename = "MEGATRON"
    reader_filename = ""
    result_file = open(result_filename, "w")
    for arg in sys.argv:
        if arg == sys.argv[0]:
            continue
        reader_filename = arg
        read_file = open(reader_filename, "r")
        result_file.write(read_file.read())
        result_file.write('\n')
        read_file.close()

    result_file.close()

if __name__ == '__main__':
    main()
