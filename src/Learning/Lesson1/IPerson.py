from abc import ABC, abstractmethod


class IPerson:
    @abstractmethod
    def load_data_source(self):
        pass

    def extract_text(self):
        pass
