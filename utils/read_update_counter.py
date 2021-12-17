from pathlib import Path


# Read and Update counter
def read_counter():
    # Read counter
    path = Path(__file__).parent.parent / "test_conf/counter.txt"
    f = open(path, 'r+')
    data = int(f.read())
    return data


# Read and Update counter
def read_and_update_counter():
    # Read counter
    path = Path(__file__).parent.parent / "test_conf/counter.txt"
    f = open(path, 'r+')
    data = int(f.read())
    # Update counter
    new_counter = str(data + 1)
    # Write new counter
    f.seek(0)
    f.write(new_counter)
    f.truncate()
    f.close()
    return new_counter
