# スープの名前を出力したいだけなのですが、このスクリプトを実行すると
# 別のメッセージも出力されてしまいます。
# `wovendojo/cook.py`を必要に応じて修正し、この余計なprint文を
# 回避してください。`cook.py`からコードを削除しては
# いけませんが、追加するのは構いません。

from wovendojo.cook import soup

print(f"I like {soup}.")
