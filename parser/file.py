from numpy import array
from numpy import concatenate
from numpy import transpose


def slice_by(it, n):
    return zip(*[it[i::n] for i in range(n)])

class FileParser:
    def __init__(self, RowParser):
        self.row = RowParser()
        self.names = list(self.row.names)
        self._data = None

    def append(self, filename):
        parsed_data = self._parse(filename)
        if self._data is None:
            self._data = parsed_data
        else:
            self._data = concatenate((self._data, parsed_data), axis=0)


    def _parse(self, filename):
        with open(filename, 'r') as datafile:
            lines = datafile.readlines()[self.row.drop_lines:]
            return array([self.row.parse(*line) for line in slice_by(lines, self.row.lines)])

    def get(self, *params, transposed=False):
        idxs = [self.names.index(param) for param in params]
        data = None
        if len(idxs) == 1:
            idx = idxs[0]
            data = self._data[:, idx:(idx + 1)]
        else:
            data = concatenate(list(self._data[:, idx:(idx + 1)] for idx in idxs), axis=1)
        return data if not transposed else transpose(data)

    @property
    def data(self):
        return self._data

    @property
    def row_number(self):
        return len(self._data)
