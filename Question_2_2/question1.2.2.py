#encoding: utf-8

def convert_space(str):
  '''
  先頭と末尾以外の連続する空白を%2Dに変換する関数
  >>>convert_space_in_string('Mr John Smith')
  'Mr%20John%20Smith'
  '''

  #変換後の文字列
  converted_string = ''

  #引数で渡された文字列を空白で分割した文字列のリストに入れる
  splited_strs_list = str.split()

  #分割した文字列リストを'%20'を挟んだ文字列に置き換える
  for splited_str in splited_strs_list:
    converted_string = converted_string + splited_str + '%20'

  #文字列の後ろに'%20'がついたままなので、その部分をカット
  return converted_string[0:len(converted_string)-3]


def _test():
  import doctest 
  doctest.testmod()

if __name__ == '__main__':
  _test()