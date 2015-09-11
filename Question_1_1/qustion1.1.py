#coding:utf-8
#Implement an algorithm to determine if a string has all unique characters.

def dup_char_str(str):

    #引数で渡された文字列中の文字を格納するリスト
    c_list = []

    #文字列を文字のリストに分解
    for character in str:
    	c_list.append(character)

    c_list.sort()

    #文字リスト中の連続する文字が重複していればTrueを返す
    counter = 0 
    while counter < (len(c_list) - 1):
    	if c_list[counter] == c_list[counter + 1]:
    		return True

    	counter = counter + 1

    #重複がなければFalseを返す
    return False


def _test():
	import doctest
	doctest.testmod()

if __name__ = '__main__':
	_test()
