import numpy as np


def split_train_test(data, test_ratio, random_seed):
    np.random.seed(random_seed)
    shuffled_data = np.random.permutation(len(data))
    print(shuffled_data)
    test_set_size = int(len(data) * test_ratio)
    test_set = shuffled_data[:test_set_size]
    train_set = shuffled_data[test_set_size:]
    return data.iloc[train_set], data.iloc[test_set]