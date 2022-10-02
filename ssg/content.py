from yaml import load, FullLoader
import re
from collections.abc import Mapping

class Content(Mapping):

    __delimiter = r"^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)

    def load(cls,string):
        _, fm, content = cls.__regex.split(string,2)
        load(fm,Loader=FullLoader)
        return cls(metadata, content)

    def __init__(self, metadata, content):
        self.data = metadata
        self.data.update(("content",content))

    