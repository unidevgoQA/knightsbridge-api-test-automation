from pathlib import Path


# Read counter number
def read_counter():
    # read counter
    path = Path(__file__).parent / "test_conf/counter.txt"
    f = open(path, 'r+')
    data = int(f.read())
    # update counter
    new_counter = str(data + 1)
    # write new counter
    f.seek(0)
    f.write(new_counter)
    f.truncate()
    f.close()
    return new_counter
