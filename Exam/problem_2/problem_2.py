from pathlib import Path
from scipy.io import loadmat
from sklearn.model_selection import KFold
import torch
from torch.nn import CrossEntropyLoss
from torch.optim import Adam
from torch.utils.data import DataLoader
from dataset import CustomDataset
from model import Model
from sklearn.model_selection import train_test_split
from utilities import train, test

ROOT = Path(__file__).parent


def problem_2(
    data_path: str = ROOT / "digits.mat", labels_path: str = ROOT / "labels.mat"
):
    """Perform K-Fold validation and use those data to train a neural network. The training process utilizes early stopping to prevent overfitting.

    Args:
        data_path (str, optional): path to the data file. Defaults to ROOT/"digits.mat".
        labels_path (str, optional): path to the labels file. Defaults to ROOT/"labels.mat".
    """
    # Hyperparameters
    n_splits = 15
    lr = 0.001
    batch_size = 32
    num_epochs = 1000
    patient = 10

    # Load data from .mat files
    data = loadmat(data_path)["data"].T
    labels = loadmat(labels_path)["labels"].T.flatten()

    # K-Fold cross validation
    kf = KFold(n_splits, shuffle=True)

    # Keep track of currrent fold
    split = 0

    # Initialize average metrices
    avg_train_loss = 0
    avg_train_acc = 0
    avg_val_loss = 0
    avg_val_acc = 0
    avg_test_loss = 0
    avg_test_acc = 0

    # Perform k-fold cross validation
    for train_indices, test_indices in kf.split(data):
        # Split dataset into train, valid, and test set
        X_train, X_val, y_train, y_val = train_test_split(
            data[train_indices], labels[train_indices]
        )
        X_test, y_test = data[test_indices], labels[test_indices]

        # Convert numpy array to dataset
        train_dataset = CustomDataset(X_train, y_train)
        val_dataset = CustomDataset(X_val, y_val)
        test_dataset = CustomDataset(X_test, y_test)

        # Load train dataset into dataloader for batch training
        train_dataloader = DataLoader(train_dataset, batch_size)

        # Define features and classes
        in_shape = torch.from_numpy(data).size()
        num_classes = torch.unique(torch.from_numpy(labels)).size()[0]

        # Define model, loss function, and optimizer
        model = Model(in_shape, num_classes)
        loss_fn = CrossEntropyLoss()
        optimizer = Adam(model.parameters(), lr)

        # Initialize per fold metrices
        train_loss = 0
        train_acc = 0
        val_loss = 0
        val_acc = 0
        test_loss = 0
        test_acc = 0

        # Early Stop: store multiple losses
        es_loss_list = []

        # Train the model
        for epoch in range(num_epochs):

            # Batch training
            train_loss, train_acc, model = train(
                model, loss_fn, optimizer, train_dataloader
            )

            # Validate the model
            val_loss, val_acc, model = test(model, loss_fn, val_dataset)

            # Print per epoch metrices
            print(
                f"Epoch: {epoch+1}/{num_epochs},",
                f" train_loss:{train_loss:.5f},",
                f" train_acc: {train_acc:.3f},",
                f" val_loss:{val_loss:.5f},",
                f" val_acc:{val_acc:.3f}",
                end="\r",
            )

            # Early stop algorithm
            # Add latest loss to the end of the list
            es_loss_list.append(val_loss)

            # Remove first loss if the list is larger than patient
            if len(es_loss_list) > patient:
                es_loss_list = es_loss_list[1:]

            # Check if the list is not decreasing
            not_decreasing = all(a <= b for a, b in zip(es_loss_list, es_loss_list[1:]))

            # Stop training once val loss list not decreasing
            if not_decreasing and len(es_loss_list) == patient:
                break

        # Test the model
        test_loss, test_acc, model = test(model, loss_fn, test_dataset)

        # Print per fold metrices
        print(
            f"Fold: {split+1}/{n_splits},",
            f" test_loss:{test_loss:.5f},",
            f" test_acc:{test_acc:.3f},",
            f" train_loss:{train_loss:.5f},",
            f" train_acc: {train_acc:.3f},",
            f" val_loss:{val_loss:.5f},",
            f" val_acc:{val_acc:.3f}",
        )

        # Update average metrices
        avg_val_loss += val_loss / n_splits
        avg_val_acc += val_acc / n_splits
        avg_train_loss += train_loss / n_splits
        avg_train_acc += train_acc / n_splits
        avg_test_loss += test_loss / n_splits
        avg_test_acc += test_acc / n_splits

        # Update split
        split += 1

    # Print average metrices
    print(
        "----Average Metrices----\n",
        f"num_folds: {n_splits}\n",
        f"avg_test_acc: {avg_test_acc:.3f}\n",
        f"avg_train_acc: {avg_train_acc:.3f}\n",
        f"avg_val_acc: {avg_val_acc:.3f}\n",
        f"avg_test_loss: {avg_test_loss:.5f}\n",
        f"avg_train_loss: {avg_train_loss:.5f}\n",
        f"avg_val_loss: {avg_val_loss:.5f}",
    )


if __name__ == "__main__":
    problem_2()
