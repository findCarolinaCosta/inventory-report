from abc import ABC, abstractmethod


class Importer(ABC):
    @staticmethod
    @abstractmethod
    def import_data(cls, path):
        raise NotImplementedError
