from abc import ABC, abstractmethod
from pandas import DataFrame


class Serializable(ABC):
    """
    An abstract base class for objects that can be serialized
    and saved to a file.

    This class defines a common interface for saving an object's
    state,ensuring that any class inheriting from it will have a
    `Save` method.
    """

    @abstractmethod
    def Save(self, data: DataFrame, filename: str,
             extention: str = "csv") -> None:
        """
        Saves the object's data to a file.

        This is an abstract method and must be implemented by any
        concrete class that inherits from `Serializable`.

        Args:
            filename (str): The name of the file to which the data
            will be saved.
            extention (str, optional): The file extension.
            Defaults to "csv".
        """
        pass
