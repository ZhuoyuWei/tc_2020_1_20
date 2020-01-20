import h5py
import sys
import scipy.sparse
import sklearn.decomposition
import pandas as pd

dataset_location = sys.argv[1]
dataset_h5 = h5py.File(dataset_location)
print('###########################################dataset_h5############################################')
print(dataset_h5)
counts_h5 = dataset_h5["data"]["counts"]
print('###########################################counts_h5############################################')
print(counts_h5)
counts = scipy.sparse.csc_matrix((
  counts_h5["x"][()],
  counts_h5["i"][()],
  counts_h5["p"][()]),
  counts_h5["dims"][()]
)
print('###########################################counts############################################')
print(counts)
cell_ids = counts_h5["rownames"][()].astype(str)
print('###########################################cell_ids############################################')
print(cell_ids)