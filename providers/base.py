from abc import ABC, abstractmethod


class BaseScraper(ABC):

    @abstractmethod
    def buscar(self):
        pass