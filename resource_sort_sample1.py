# vmstatなどで出力したリソース状況をPythonに取り込んで
# リソース順などに並べ替える処理の一部
# 最終的にはファイルをインプットとして、
# 並べなおしたファイルを出力する

class Resource:
    """
    list型として受け取りアンパックして代入する
    受け取るlistの順序が正しい前提となるクラス
    resource_list[0]: date
    resource_list[1]: cpu
    """
    _date: str
    _cpu: int
    def __init__(self, resource_lists: list):
        self._date, self._cpu = resource_lists
    
    def __repr__(self):
        return f'{self._date}, {self._cpu}'
    
    @property
    def date(self):
        return self._date

    @property
    def cpu(self):
        return self._cpu

# 代入用のデータ（最終はここをファイルインプットとする）
resource1 = ['2020/9/18 11:00', 73]
resource2 = ['2020/9/18 11:05', 65]
resource3 = ['2020/9/18 11:10', 67]

# Sort元のデータをクラスのリストとして作る
resourcelists = []
resourcelists.append(Resource(resource1))
resourcelists.append(Resource(resource2))
resourcelists.append(Resource(resource3))

print(resourcelists)

# CPUの降順に並べなおす
resourcelists.sort(key=lambda x: -x.cpu)

print(resourcelists)