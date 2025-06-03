>>> matrix_divided = __import__('2-matrix_divided').matrix_divided
>>> matrix_divided([[1, 2], [3, 4]], float('inf'))
Traceback (most recent call last):
TypeError: div must be a number

>>> matrix_divided()
Traceback (most recent call last):
TypeError: matrix_divided() missing required arguments 'matrix' and/or 'div'

>>> matrix_divided([[1, 2], [3, 4]])
Traceback (most recent call last):
TypeError: matrix_divided() missing required arguments 'matrix' and/or 'div'
