# 【配列をファイルに出力するサンプル】
# お問い合わせ集計結果をマークダウンの書式で配列にセットし、配列を一気に
# マークダウンファイルとして出力する。
#

# ファイルに出力する配列
lst = ["| | 件数 | 前日比 |",
       "| ------------: | ----: | ------: |",
       "| 手持ち | 9 件 | +2 件 |",
       "| 入り | 4 件 | +3 件 |",
       "| 3件以上 | 0 件 | +0 件 |",
       "| 1週間以上 | 3 件 | +0 件 |",
       "| アクション日 | 4 件 | +0 件 |",
       ""
      ]

# ファイルに出力する
# ここでは、ファイル名を”timothy.md” として出力する
with open('timothy.md', 'w') as file:
    file.write('\n'.join(lst))
