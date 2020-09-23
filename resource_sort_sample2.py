import csv


class Resource:
    """
    list型として受け取りアンパックして代入する
    受け取るlistの順序が正しい前提となるクラス
    resource_list[0]: date
    resource_list[1]: idle
    resource_list[2]: sys
    resource_list[3]: user
    resource_list[4]: cpu

    ※date, cpu以外のgetterは検証では不要だったので割愛
    """
    _date: str
    _idle: str
    _sys: str
    _user: str
    _cpu: str
    def __init__(self, resource_lists: list):
        self._date, self._idle, self._sys, self._user, self._cpu = resource_lists
    
    def __repr__(self):
        return f'{self._date}, {self._cpu}'
    
    @property
    def date(self):
        return self._date

    @property
    def cpu(self):
        return int(self._cpu)

FILENAME = 'sample2.csv'
resourcelists = []
with open(FILENAME, 'rt') as f:
    reader = csv.reader(f)
    next(reader) # ヘッダーをスキップする
    for row in reader:
        resourcelists.append(Resource(row))

print(resourcelists)

## CPUの最大値を求める
print(max(resourcelists, key=lambda x: x.cpu))

## CPUの降順に並べなおす
resourcelists.sort(key=lambda x: -x.cpu)
print(resourcelists)