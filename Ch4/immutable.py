# creating immutable data classes

from dataclasses import dataclass

# TODO: The "frozen" parameter makes the class immutable
@dataclass (frozen=True) 
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0

    def somefunc(self, newval):
        self.value2 = newval


obj = ImmutableClass()
print(obj.value1)   

# TODO: attemting to cahnge an immtuable class throwas an exception
obj.value1 = "change" # dataclasses.FrozenInstanceError: cannot assign to field 'value1'

# TODO: even functions with the class can't change anything
obj.somefunc(20) #dataclasses.FrozenInstanceError: cannot assign to field 'value2'