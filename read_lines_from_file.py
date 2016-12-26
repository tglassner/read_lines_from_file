def read_filedata():
    file_data = open('samplefile.txt', 'r')

    file_data_items = []
    for line in file_data:
        line = line.strip()
        file_data_items.append(line)

    print(file_data_items)
    file_data.close()

def main():
    read_filedata()

main()
