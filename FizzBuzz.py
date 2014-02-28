#!/usr/bin/env python
print ', '.join([''.join(['Buzz' if i % 3 == 0 else ''] + ['Fizz' if i % 5 == 0 else '']) if i % 3 == 0 or i % 5 == 0 else str(i) for i in range(1,101)])