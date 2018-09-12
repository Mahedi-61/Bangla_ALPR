"""setting root directory for the main project"""

import os

def root_path():
    return os.path.dirname(__file__)


def data_path():
    return os.path.join(root_path(), "data")


def dataset_path():
    return os.path.join(root_path(), "dataset")


def libs_path():
    return os.path.join(root_path(), "libs")


def src_path():
    return os.path.join(root_path(), "src")


def darknet_path():
    return os.path.join(root_path(), "libs", "darknet")