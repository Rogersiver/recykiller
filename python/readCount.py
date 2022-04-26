import shelve

s = shelve.open('counter.db')
try:
    count = s['key1']
finally:
    print(s['key1'])
    s.close()
