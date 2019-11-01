from typing import Callable, Any


class Composer(object):
    def __init__(self, fn: Callable[[Any], Any], *args, **kwargs):
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.value: Any = None
        self.compute()

    @staticmethod
    def flatten_composers(c: Composer):
        d = c
        while isinstance(d, Composer):
            d = d.value
        return d

    def _nextValue(self, c: Callable[[Any], Any]):
        self.value = c(self.value)
        return self

    def __or__(self, c: Callable[[Any], Any]):
        return self._nextValue(c)

    def __gt__(self, c: Callable[[Any], Any]):
        return self._nextValue(c)

    def compute(self):
        value = self.fn(*self.args, **self.kwargs)
        self.value = Composer.flatten_composers(value)

    def then(self, call):
        return self._nextValue(call)

    @staticmethod
    def identity(idx: Any):
        return Composer(lambda x: x, idx)

