from typing import List, Dict, Tuple, Set, Optional, Any, Union, Callable, TypeVar, Generic, Iterable, Iterator, Sequence, Mapping, MutableMapping, FrozenSet, ByteString, Sized, Container, Hashable, Reversible, SupportsInt, SupportsFloat, SupportsComplex, SupportsBytes, SupportsAbs, SupportsRound, ContextManager, AsyncContextManager, AsyncIterable, AsyncIterator, Awaitable, Coroutine, Generator, AsyncGenerator, Type, NewType, NoReturn, AnyStr, Text, BinaryIO
#Now we will use the imported lists, dictionaries, tuples, sets, and other types in our code to demonstrate their usage.
list_example: List[int] = [1, 2, 3, 4, 5]
dict_example: Dict[str, int] = {"one": 1, "two": 2, "three": 3}
tuple_example: Tuple[int, str, float] = (1, "hello", 3.14)
set_example: Set[int] = {1, 2, 3, 4, 5}
optional_example: Optional[int] = None  
any_example: Any = "This can be any type"
union_example: Union[int, str] = "This can be an int or a string"
callable_example: Callable[[int, int], int] = lambda x, y: x + y
iterable_example: Iterable[int] = [1, 2, 3]


#Match case statement in Python
#The match case statement is a powerful control flow structure that allows you to match patterns against values
#Example of using match case statement
def http_status(status_code: int) -> str:
    match status_code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status Code"
print(http_status(200))  # Output: OK
print(http_status(404))  # Output: Not Found