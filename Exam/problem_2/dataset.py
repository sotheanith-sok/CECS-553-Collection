from torch.utils.data import Dataset
import torch
import numpy as np


class CustomDataset(Dataset):
    """An implementation of torch.utils.data.Dataset .

    Args:
        Dataset (Class): generic pytorch dataset class.
    """

    def __init__(self, X: np.ndarray, y: np.ndarray):
        """Initialize the dataset

        Args:
            X (np.ndarray): data.
            y (np.ndarray): labels.
        """
        super(CustomDataset, self).__init__()
        self.X = torch.from_numpy(X).float()
        self.y = torch.from_numpy(y)

    def __getitem__(self, index: int) -> tuple:
        """Return data and label based on index.

        Args:
            index (int): index.

        Returns:
            tuple: data, label
        """
        return self.X[index], self.y[index]

    def __len__(self) -> int:
        """Return dataset length

        Returns:
            int: length
        """
        return self.X.shape[0]
