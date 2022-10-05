from os import path, mkdir


class FileUtil:
    def __new__(cls):
        raise TypeError('Static classes cannot be instantiated')

    @staticmethod
    def checkExistFolder(folderPath) -> bool:
        return path.exists(folderPath)

    @staticmethod
    def createDirectory(folderPath) -> bool:
        try:
            if path.exists(folderPath):
                print(f"File exists: {folderPath}")
                return True
            else:
                mkdir(folderPath)
                print(f"File created: {folderPath}")
                return True
        except Exception as ex:
            print(ex)
            return False

    @staticmethod
    def checkExistFile(path_to_file) -> bool:
        return path.exists(path_to_file)


folderPath = "/tmp"

result = FileUtil.checkExistFolder(folderPath)
print(result)

# result = FileUtil.createDirectory(f"{folderPath}/abc")
# print(result)

# result = FileUtil.checkExistFile(f"{folderPath}/abc/test.txt")
# print(result)
