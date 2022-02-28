import shelve
s = shelve.open('counter.db')
try:
    s['key1'] = { 'count': 1}
finally:
    s.close()