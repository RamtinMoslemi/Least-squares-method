import numpy as np
import torch
from sklearn import datasets
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt


class PCA:
    def __init__(self, train_data):
        # find mean image
        self.psi = train_data.mean(axis=0)
        # normalize the matrix
        a = train_data - self.psi
        # perform the SVD
        u, d, v = torch.svd(a.T)
        self.principle_components = u.T
        self.eigen_values = d

    def reconstruct_image(self, orig, k):
        pc = self.principle_components[:k]
        w = (orig - self.psi) @ pc.T
        recon = w @ pc + self.psi
        return recon

    def plot_eigen_values(self):
        plt.plot(self.eigen_values)
        plt.title('Eigen values')
        plt.show()


def plot_losses(train_losses, test_losses, log=True):
    k = range(1, len(train_losses) + 1)
    y_lab = ''
    if log:
        train_losses = np.log(train_losses)
        test_losses = np.log(test_losses)
        y_lab = 'log of '
    plt.plot(k, train_losses, label='Train')
    plt.plot(k, test_losses, label='Test')
    plt.title('Reconstruction Loss')
    plt.ylabel(y_lab + 'mean squared error')
    plt.xlabel('number of principal components')
    plt.legend()
    plt.show()


def reconstruction_loss(original_image, reconstructed_image):
    diff = original_image - reconstructed_image
    mse = torch.sum(diff.T @ diff) / original_image.shape[0]
    return mse


def show_results(pca, train_data, test_data, max_k=100, print_losses=False):
    train_losses, test_losses = list(), list()
    for k in range(1, max_k + 1):
        # train data
        train_recon = pca.reconstruct_image(orig=train_data, k=k)
        train_loss = reconstruction_loss(train_data, train_recon)
        train_losses.append(train_loss)
        # test data
        test_recon = pca.reconstruct_image(orig=test_data, k=k)
        test_loss = reconstruction_loss(test_data, test_recon)
        test_losses.append(test_loss)
        # print losses
        if print_losses:
            print(f'{k} principal components: train_loss={train_loss:.2f}, test_loss={test_loss:.2f}')
    plot_losses(train_losses, test_losses)


if __name__ == '__main__':
    # load the dataset
    faces = datasets.fetch_olivetti_faces()
    # convert to tensor
    faces_data = torch.from_numpy(faces.data)
    # split the data into train and test set
    train_set, test_set = train_test_split(faces_data, test_size=0.1)
    # perform PCA
    principal_component_analysis = PCA(train_set)
    # show the eigen values
    principal_component_analysis.plot_eigen_values()
    # show the results
    show_results(principal_component_analysis, train_set, test_set)
