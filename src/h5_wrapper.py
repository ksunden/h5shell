import h5py


class H5Explorer(object):
    def __init__(self, filename, mode="r"):
        self.__file = h5py.File(filename, mode)
        self.__working_dir = "/"

    @property
    def working_dir(self):
        return self.__working_dir

    def change_dir(self, new_dir="/"):
        if not new_dir.startswith("/"):
            new_dir = "{}/{}".format(self.__working_dir, new_dir)

        if new_dir in self.__file:
            self.__working_dir = new_dir
        else:
            raise ValueError("Directory {} does not exist.".format(new_dir))

    def list_groups(self):
        return [ k for k, v in self.__file[self.__working_dir].items()
                 if isinstance(v, h5py.Group) ]

    def list_datasets(self):
        return [ k for k, v in self.__file[self.__working_dir].items()
                 if isinstance(v, h5py.Dataset) ]
