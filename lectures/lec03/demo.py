print(f'This is a test of formatted strings: {1+2}')

print('This is a test of formatted strings: {}'.format(1+2))

# >>> '{:s}'.format('foo')
# 'foo'
# >>> '{:10s}'.format('foo')    # field width 10
# 'foo       '
# >>> '{:<10s}'.format('foo')   # field width 10, left (<) justified
# 'foo       '
# >>> '{:^10s}'.format('foo')   # field width 10, center (^) justified
# '   foo    '
# >>> '{:>10s}'.format('foo')   # field width 10, right (>) justified
# '       foo'

# >>> '{:d}'.format(42)
# '42'
# >>> '{:10d}'.format(42)
# '        42'
# >>> '{:<10d}'.format(42)
# '42        '
# >>> '{:^10d}'.format(42)
# '    42    '
# >>> '{:>10d}'.format(42)
# '        42'

# >>> '{:f}'.format(3.14159265358979)
# '3.141593'
# >>> '{:.2f}'.format(3.14159265358979)
# '3.14'
# >>> '{:10.2f}'.format(3.14159265358979)
# '      3.14'
# >>> '{:<10.2f}'.format(3.14159265358979)
# '3.14      '
# >>> '{:^10.2f}'.format(3.14159265358979)
# '   3.14   '
# >>> '{:>10.2f}'.format(3.14159265358979)
# '      3.14'
# >>> '{:10.6f}'.format(3.14159265358979)
# '  3.141593'
# >>> '{:10.6f}'.format(3.1)
# '  3.100000'

# >>> '{:g}'.format(3.14159265358979)
# '3.14159'
# >>> '{:.2g}'.format(3.14159265358979)
# '3.1'
# >>> '{:10.2g}'.format(3.14159265358979)
# '       3.1'
# >>> '{:<10.2g}'.format(3.14159265358979)
# '3.1       '
# >>> '{:^10.2g}'.format(3.14159265358979)
# '   3.1    '
# >>> '{:>10.2g}'.format(3.14159265358979)
# '       3.1'
# >>> '{:10.6g}'.format(3.14159265358979)
# '   3.14159'
# >>> '{:10.6g}'.format(3.1)
# '       3.1'

name='Lorem'

def say_hello(name_input):
    print(f'Hello, {name_input}!')

say_hello(name)
