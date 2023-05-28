from counter import Counter
from genarator import Generator
'''
name = "Andrii"
#for i in iter(name):#range
#    print(i)
try:
    iterator = iter(name)
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
except StopIteration:
    print()
'''
'''
#Counter
counter = Counter(9)
for i in counter:
    print(i)
'''
#Generator
generator = Generator(0)
res = generator.Raise_to_the_degrees_F(122345, 500)
print(res)
for item in generator.Raise_to_the_degrees_F(122345, 500):
    print(f"{item}\n")