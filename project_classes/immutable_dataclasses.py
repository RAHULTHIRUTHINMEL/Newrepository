from dataclasses import dataclass

@dataclass(frozen=True)  # frozen parameter makes immutable
class ImmutableClass:
    value1 : str = "Value1"
    value2 : int = 0


    def somefunc(self, newval):
        self.value2 = newval



obj = ImmutableClass()
print(obj.value1)

obj.value1 = "another value"
print(obj.value1)
obj.somefunc(20)