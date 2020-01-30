import numpy as np


class SPE(object):

    def __init__(self, fname):
        self._fid = open(fname, 'rb')
        self._load_info()

    def  _load_info(self):
        self._xdim = np.int64(self.read_at(42, 1, np.int16)[0])
        self._ydim = np.int64(self.read_at(656, 1, np.int16)[0])
        if self._ydim > 65536:
            self._ydim = 1
        self._numframes = np.int64(self.read_at(1446, 1, np.int16)[0])
        self._offset = np.float64(self.read_at(3263, 1, np.float64))
        self._dx = np.float64(self.read_at(3271, 1, np.float64))
        self._datatype = np.int64(self.read_at(108, 1, np.int16)[0])

    def get_size(self):
        return (self._xdim, self._ydim, self._numframes)
        
    def read_at(self, pos, size, ntype):
        self._fid.seek(pos)
        return np.fromfile(self._fid, ntype, size)

    def load_data(self):
        datatype_map = {0 : np.float32, 1 : np.int32, 2 : np.int16, 3 : np.uint16}
        data = self.read_at(4100, self._xdim * self._ydim * self._numframes, datatype_map\
                            [self._datatype]).reshape((self._numframes, self._xdim)).T

        return np.concatenate((np.arange(self._offset, self._offset+(self._xdim-.5)*self._dx, \
                                self._dx, dtype=np.float)[:, np.newaxis], data), axis=1)

    def close(self):
        self._fid.close()


def load_spe(fname):
    fid = SPE(fname)
    data = fid.load_data()
    fid.close()
    return data


def load_txt(fname):
    return np.loadtxt(fname, delimiter = "\t")


if __name__ == "__main__":
    import sys
    data = load(sys.argv[-1])
