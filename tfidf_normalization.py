from scipy import sparse
def proses(X):
    return sparse.csr_matrix(X/X.sum(1))