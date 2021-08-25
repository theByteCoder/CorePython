from typing import Any, Callable

add: Callable[[Any, Any], Any] = lambda a, b: a + b

print(add(2, 3))
