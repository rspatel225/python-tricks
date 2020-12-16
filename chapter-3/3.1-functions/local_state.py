def multiple_by(num):
    def mult(x):
        # num is still remebered after mult is returned
        return x * num
    return mult

if __name__ == '__main__':
    times3 = multiple_by(3)
    print(times3(10))
    
