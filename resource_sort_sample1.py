# vmstatなどで出力したリソース状況をPythonに取り込んで
# リソース順などに並べ替える処理の一部
# 最終的にはファイルをインプットとして、
# 並べなおしたファイルを出力する

class Resource:
    """
    list型として受け取りアンパックして代入する
    受け取るlistの順序が正しい前提となるクラス
    resouce_list[0]: date
    resouce_list[1]: cpu
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
resouce1 = ['2020/9/18 11:00', 73]
resouce2 = ['2020/9/18 11:05', 65]
resouce3 = ['2020/9/18 11:10', 67]

# Sort元のデータをクラスのリストとして作る
resoucelists = []
resoucelists.append(Resource(resouce1))
resoucelists.append(Resource(resouce2))
resoucelists.append(Resource(resouce3))

print(resoucelists)

# CPUの降順に並べなおす
resoucelists.sort(key=lambda x: -x.cpu)

print(resoucelists)