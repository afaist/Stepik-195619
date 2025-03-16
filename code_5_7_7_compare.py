import timeit
from prettytable import PrettyTable

nums = list(range(1000))
call = f"compute([inc, square, dec], *{nums})"
funcs = f"""
def square(num):
    return num ** 2

def inc(num):
    return num + 1

def dec(num):
    return num - 1


"""

code = f"""
def compute(funcs, *args):
    comp = lambda x: [x:=func(x) for func in funcs][-1]
    return [comp(i) for i in args]


"""

code2 = """
def compute(funcs, *args):
    res = []
    for el in args: 
        tmp = el
        for f in funcs: tmp = f(tmp)
        res += [tmp]
    return res


"""
code3 = f"""
def compute(funcs, *args):
    return [args:=list(map(func, args)) for func in funcs][-1]


"""

mytable = PrettyTable()
mytable.field_names = [
    "count",
    "list comprehension",
    "classic",
    "map + list comprehension",
]
res = {}
for num in (10, 100, 1000, 10000):
    mytable.add_row(
        [
            num,
            timeit.timeit(stmt=funcs + code + call, number=num),
            timeit.timeit(stmt=funcs + code2 + call, number=num),
            timeit.timeit(stmt=funcs + code3 + call, number=num),
        ]
    )
print(mytable)
