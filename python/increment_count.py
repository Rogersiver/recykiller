import shelve

def increment_can_count():
    s = shelve.open('counter', writeback=True)
    try:
        s['key1']['count'] += 1
    finally:
        s.close()
increment_can_count()

