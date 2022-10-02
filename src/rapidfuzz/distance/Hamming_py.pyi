from typing import Any, Callable, Dict, Hashable, Optional, Sequence, TypeVar

from typing_extensions import Protocol

from rapidfuzz.distance import Editops, Opcodes

class _ScorerAttributes(Protocol):
    _RF_ScorerPy: Dict

def _attr_decorator(func: Any) -> _ScorerAttributes:
    return func

_StringType = Sequence[Hashable]
_S1 = TypeVar("_S1")
_S2 = TypeVar("_S2")

@_attr_decorator
def distance(
    s1: _S1,
    s2: _S2,
    *,
    processor: Optional[Callable[..., _StringType]] = None,
    score_cutoff: Optional[int] = None
) -> int: ...
@_attr_decorator
def normalized_distance(
    s1: _S1,
    s2: _S2,
    *,
    processor: Optional[Callable[..., _StringType]] = None,
    score_cutoff: Optional[float] = 0
) -> float: ...
@_attr_decorator
def similarity(
    s1: _S1,
    s2: _S2,
    *,
    processor: Optional[Callable[..., _StringType]] = None,
    score_cutoff: Optional[int] = None
) -> int: ...
@_attr_decorator
def normalized_similarity(
    s1: _S1,
    s2: _S2,
    *,
    processor: Optional[Callable[..., _StringType]] = None,
    score_cutoff: Optional[float] = 0
) -> float: ...
def editops(
    s1: _S1,
    s2: _S2,
    *,
    processor: Optional[Callable[..., _StringType]] = None
) -> Editops: ...
def opcodes(
    s1: _S1,
    s2: _S2,
    *,
    processor: Optional[Callable[..., _StringType]] = None
) -> Opcodes: ...
