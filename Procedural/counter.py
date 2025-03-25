# counter.py
count = 0

def increment():
    global count
    count += 1

def get_count():
    return count
