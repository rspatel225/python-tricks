from contextlib import contextmanager

@contextmanager
def managed_file(name, mode):
    # the try until the yeild is similar to __enter__
    try:
        f = open(name, mode)
        yield f
    # finally is similar to __exit__
    finally:
        f.close()

with managed_file('./info.txt', 'w') as f:
    f.write('changed with decorator context manager')

with managed_file('./info.txt', 'r') as f:
    print(f.read())