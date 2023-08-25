# bit op
# & ampersand - bitwise conjunction = simply and
# | bar - bitwise disjunction = simply or
# ~ tilde - bitwise negation = simply !
# ^ caret - bitwise exclusive or xor = dapat isa lang true
# >> digraphs pair - bitwise shift
# <<

# important: these must be int !float
# logop not working in bit level ops
# bitop are strict, it deal with every bit separately

# 0000 0000

x = 4  # 100
y = 1  # 1
a = x & y  # 000 /
b = x | y  # 101 /
c = ~x  # 1111 1011 x
d = x ^ 5  # 000 /
e = x >> 2  # 001 /
f = x << 2  # 1 0000 /
print(a, b, c, d, e, f)
