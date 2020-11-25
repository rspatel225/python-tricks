class Indenter:
    def __init__(self):
        self.level = 0

    # indentation starts with 1 additional tab
    def __enter__(self):
        self.level += 4
        return self

    # there is no close to this resource because it doesn't apply
    def __exit__(self, exc_type, exc_value, exc_tb):
        self.level -= 4

    # print using spaces
    def print(self, string):
        print(' ' * self.level + string)

with Indenter() as indent:
    indent.print('1st level')
    with indent:
        indent.print('2nd level')
    indent.print('1st level again')