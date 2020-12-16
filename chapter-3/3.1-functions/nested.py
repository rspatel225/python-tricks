def pace(speed):
    def walk(dist):
        return 2.5 * dist
    def run(dist):
        return 6 * dist
    if speed == 'slow':
        return walk
    else:
        return run

if __name__ == '__main__':
    func = pace('slow')
    print(func)