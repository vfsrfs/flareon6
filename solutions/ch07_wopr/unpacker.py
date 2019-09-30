def main(file_path):
    with open(file_path, 'rb') as f:
        pyc = f.read()

    header = b'\x42\x0d\x0d\x0a\x00\x00\x00\x00\x48\xcc\x8c\x5d\x04\x01\x00\x00'

    with open(file_path + ".pyc", 'wb') as f2:
        f2.write(header)
        f2.write(pyc)


if __name__ == '__main__':
    main("pyiboot02_cleanup")