import os
rootdir = '/Users/qikpod/pythonworkspace/test'
def get_dir_name(root_dir_path , dir_path):
    rootdirlist = root_dir_path.split(os.sep)
    rootlist = dir_path.split(os.sep)
    dirpath = list(set(rootlist).difference(rootdirlist))
    st = os.sep.join(dirpath)
    return st