name:str = "Umar"
print(name)

#  Function Annotations

def add(x: int | float , y: int | float) -> int | float:
    return x + y

print(add(2, 3))  # Output: 5
print(add(2.5, 3.5))  # Output: 6.0

#  Type Aliases
from typing import List, Tuple
x : list[list[int]] = [[1, 2], [3, 4]]
# y : Tuple[int] = (1, 2,5) # Error: Tuple[int,int,int] is a valid type for y

y : dict[str, int] = {'a': 1, 'b': 2,'c' : 4}  # Corrected to a dictionary type

print(x)  # Output: [[1, 2], [3, 4]]
print(y)  # Output: (1, 2)


#  Custom Type

# type Vector = list[float]
# def add_vectors(v1: Vector, v2: Vector) -> Vector:
#     return [x + y for x, y in zip(v1, v2)]

# print(add_vectors([1.0, 2.0], [3.0, 4.0]))  # Output: [4.0, 6.0]

#  OR

vector = List[float]
def add_vectors(v1: vector, v2: vector) -> vector:
    return [x + y for x, y in zip(v1, v2)]

print(add_vectors([1.0, 2.0], [3.0, 4.0]))  # Output: [4.0, 6.0]

#  Optional parameters
from typing import Optional
def greet(name: str, age: Optional[int] = None) -> str:
    if age is not None:
        return f"Hello, {name}! You are {age} years old."
    else:
        return f"Hello, {name}!"
    

print(greet("Alice"))  # Output: Hello, Alice!
print(greet("Bob", 25))  # Output: Hello, Bob! You are 25 years old.


# Sequence Types
from typing import Sequence, Union
# Sequence is a generic type that can be used to specify a sequence of elements.Like list, tuple, etc.
def process_sequence(seq: Sequence[Union[int, str]]) -> None:
    for item in seq:
        print(item)

process_sequence([1, 2, 3])  # Output: 1 2 3


# Callable Types
from typing import Callable

def apply_function(func: Callable[[int], int], value: int) -> int:
    return func(value)

def square(x: int) -> int:
    return x * x

sqr = apply_function(square, 5)  # Output: 25
print(sqr)

#  Generic Types
from typing import TypeVar, Generic
T = TypeVar('T')
class Box(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value

    def get_value(self) -> T:
        return self.value

def get_item(lst: list[T], index: int) -> T:
    return lst[index]

print(get_item([1, 2, 3], 1))  # Output: 2