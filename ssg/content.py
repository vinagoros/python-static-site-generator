from yaml import load, FullLoader
import re
from collections.abc import Mapping

class Content(Mapping):

    __delimiter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)

    def load(self,cls,string):
        split_regex = self.__regex.split(string,2)
        _, fm, content = split_regex[0], split_regex[1], split_regex[2]
        load(fm,Loader=FullLoader)
        return cls(metadata, content)