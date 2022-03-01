import shelve
s = shelve.open('counter.db')
try:
    s['thursday'] = { 'count': 1}
    s['friday'] = { 'count': 1}
    s['saturday'] = { 'count': 1}
    s['sunday'] = { 'count': 1}
finally:
    s.close()