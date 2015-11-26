#encoding: utf-8

def sort_str(str1,str2):

  '''
  挿入したふたつの文字列の片方が、もう片方の並び替えになっているかどうかを決定するメソッド
  >>>sort_str(abcd,cabd)
  True
  >>>sort_str(abcd,efgh)
  False
  '''

  #挿入するふたつの文字列をリストに分解する

  splited_str1 = str1.split()
  splited_str2 = str2.split()

  #リスト分解した文字列をソートする

  sorted_str1 = splited_str1.sort()
  sorted_str2 = splited_str2.sort()

  #ソートした文字列が一致するか否かを判定する。

  if sorted_str1 == sorted_str2:
    return True

  else:
    return False 
