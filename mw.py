import sys

def stars(count):
    return '*' * count


_string = sys.argv[1]
m_count = _string.count('m')
w_count = _string.count('w')
print(f'm ({m_count}) {stars(m_count)} \nw ({w_count}) {stars(w_count)}')