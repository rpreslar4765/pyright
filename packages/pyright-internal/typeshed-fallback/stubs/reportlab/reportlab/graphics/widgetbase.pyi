from _typeshed import Incomplete
from typing import Final

from reportlab.graphics import shapes
from reportlab.lib.attrmap import *
from reportlab.lib.validators import *

__version__: Final[str]

class PropHolder:
    def verify(self) -> None: ...
    def __setattr__(self, name, value) -> None: ...
    def getProperties(self, recur: int = 1): ...
    def setProperties(self, propDict) -> None: ...
    def dumpProperties(self, prefix: str = "") -> None: ...

class Widget(PropHolder, shapes.UserNode):
    # TODO: draw should probably be marked abstract
    def draw(self) -> None: ...
    def demo(self) -> None: ...
    def provideNode(self) -> shapes.Shape: ...
    def getBounds(self) -> tuple[float, float, float, float]: ...

class ScaleWidget(Widget):
    x: Incomplete
    y: Incomplete
    contents: Incomplete
    scale: Incomplete
    def __init__(self, x: int = 0, y: int = 0, scale: float = 1.0, contents: Incomplete | None = None) -> None: ...
    def draw(self): ...

class CloneMixin:
    def clone(self, **kwds): ...

class TypedPropertyCollection(PropHolder):
    def __init__(self, exampleClass, **kwds) -> None: ...
    def wKlassFactory(self, Klass): ...
    def __getitem__(self, x): ...
    def __contains__(self, key) -> bool: ...
    def __setitem__(self, key, value) -> None: ...
    def __len__(self) -> int: ...
    def getProperties(self, recur: int = 1): ...
    def setVector(self, **kw) -> None: ...
    def __getattr__(self, name): ...
    def __setattr__(self, name, value): ...
    def checkAttr(self, key, a, default: Incomplete | None = None): ...

def tpcGetItem(obj, x): ...
def isWKlass(obj): ...

class StyleProperties(PropHolder):
    def __init__(self, **kwargs) -> None: ...
    def __setattr__(self, name, value) -> None: ...

class TwoCircles(Widget):
    leftCircle: Incomplete
    rightCircle: Incomplete
    def __init__(self) -> None: ...
    def draw(self): ...

class Face(Widget):
    x: int
    y: int
    size: int
    skinColor: Incomplete
    eyeColor: Incomplete
    mood: str
    def __init__(self) -> None: ...
    def demo(self) -> None: ...
    def draw(self): ...

class TwoFaces(Widget):
    faceOne: Incomplete
    faceTwo: Incomplete
    def __init__(self) -> None: ...
    def draw(self): ...
    def demo(self) -> None: ...

class Sizer(Widget):
    contents: Incomplete
    fillColor: Incomplete
    strokeColor: Incomplete
    def __init__(self, *elements) -> None: ...
    def add(self, node, name: Incomplete | None = None) -> None: ...
    def getBounds(self): ...
    def draw(self): ...

class CandleStickProperties(PropHolder):
    strokeWidth: Incomplete
    strokeColor: Incomplete
    strokeDashArray: Incomplete
    crossWidth: Incomplete
    crossLo: Incomplete
    crossHi: Incomplete
    boxWidth: Incomplete
    boxFillColor: Incomplete
    boxStrokeColor: Incomplete
    boxStrokeWidth: Incomplete
    boxStrokeDashArray: Incomplete
    boxLo: Incomplete
    boxMid: Incomplete
    boxHi: Incomplete
    boxSides: Incomplete
    position: Incomplete
    candleKind: Incomplete
    axes: Incomplete
    chart: Incomplete
    def __init__(self, **kwds) -> None: ...
    def __call__(self, _x, _y, _size, _color): ...

def CandleSticks(**kwds): ...
def test() -> None: ...
