class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        # data = open(self.file_path)
        # for line in data:
        #     print(line[0:-1])
        # data.close()
        with open(self.file_path, "r", encoding="utf-8") as data:
            lines = data.readlines()
            for line in lines:
                print(line[0:-1])

    def find_char_count(self, character):
        count = 0
        with open(self.file_path, "r", encoding="utf-8") as data:
            lines = data.readlines()
            for line in lines:
                if "*" in line:
                    count += line.count("*")
        return count


if __name__ == "__main__":

    file_reader = FileReader("demo_file.txt")
    file_reader.read_file()
    total_star_count = file_reader.find_char_count("*")
    print("Number of '*' found:", total_star_count)
