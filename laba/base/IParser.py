import abc
from .NodeVal import NodeVal

class IParser(abc.ABC):
  _node_val: NodeVal

  def __init__(self) -> None:
    self._node_val = NodeVal()

  @abc.abstractmethod
  def parse(self, inp: str, *args, **kwargs) -> NodeVal:
    pass

  def clear(self):
    self._node_val.clear()