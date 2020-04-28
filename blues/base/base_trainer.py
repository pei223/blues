from abc import ABCMeta, abstractmethod
from .base_dataset import BaseDataset
from blues.tables.learning_table import LearningTable


class BaseTrainer(metaclass=ABCMeta):

    def __init__(self, learning_table: LearningTable, train_dataset: BaseDataset, result_path: str, num_epochs: int,
                 test_dataset: BaseDataset = None, callback_functions: list = None):
        self._learning_table = learning_table
        self._train_dataset = train_dataset
        self._result_path = result_path
        self._num_epochs = num_epochs
        self._test_dataset = test_dataset
        self._callback_functions = callback_functions

    @abstractmethod
    def run(self):
        pass