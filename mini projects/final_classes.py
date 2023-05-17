# final classes are classes that cannot be extended or subclasses
from typing import final

@final
class FinalClass:
    pass

class SubClass(FinalClass):
    pass