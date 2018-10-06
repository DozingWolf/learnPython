from functools import reduce


def prod(L):
    def product(a , b):
        result = a*b
        return result
    result_output = reduce(product,L)
    return result_output


output = prod([3, 5, 7, 9])
print('right result is :',3 * 5 * 7 * 9)
print('and ,u r result is:')
print(output)
