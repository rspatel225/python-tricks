class ManagedFile:
    def __init__(self, name, mode='w'):
        self.name = name
        self.mode = mode

    # when used in a with statement this function will be called and opens the file
    def __enter__(self):
        self.file = open(self.name, self.mode)
        return self.file

    # upon leaving the with block this funciton will be called and close the file
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

with ManagedFile('./info.txt') as f:
    f.write('changed using context manager')

with ManagedFile('./info.txt', 'r') as f:
    print(f.read())
