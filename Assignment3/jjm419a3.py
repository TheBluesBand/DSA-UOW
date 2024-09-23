import os




if __name__ == '__main__':
    # Test the function
    file_name = "a3-sample.txt"
    filePath = os.path.join(os.path.dirname(__file__), file_name)
    file = open(filePath, 'r', encoding="utf-8")