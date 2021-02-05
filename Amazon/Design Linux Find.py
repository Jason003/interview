# design for linux find
from enum import Enum
from abc import ABCMeta, abstractmethod
from collections import deque


class FileType(Enum):
    video = 1
    image = 2
    text = 3
    other = 4


class File:
    # children is list of File
    def __init__(self, name: str, size: int, type=None, is_directory=False, children=None):
        if children is None:
            children = []
        self.name = name
        self.size = size
        self.type = type
        self.is_directory = is_directory
        self.children = children


# build abstract class
class Filter(metaclass=ABCMeta):
    @abstractmethod
    def apply_filter(self, file: File):
        pass


# extend previous abstract class Filter
class MinSizeFilter(Filter):
    def __init__(self, size):
        self.size = size

    def apply_filter(self, file):
        return file.size >= self.size


class TypeFilter(Filter):
    def __init__(self, type):
        self.type = type

    def apply_filter(self, file):
        return file.type == self.type


# build FindCommand class
class FindCommand:
    def __init__(self, type=None, min_size=0):
        self.min_size_filter = MinSizeFilter(min_size)
        self.type_filter = TypeFilter(type)
        self.file_lst = []

    def get_required_file_list(self, file):
        queue = deque([file])
        while queue:
            cur_file = queue.popleft()
            if self.min_size_filter.apply_filter(cur_file) and self.type_filter.apply_filter(cur_file):
                self.file_lst.append(cur_file.name)
            for child in cur_file.children:
                queue.append(child)
        return self.file_lst