#encoding: utf-8

def space_string(string):


#new string

  inserted_string = ''

#string will be inserted

  insert_string = '%20'

#list inserted string
  char_list = list(string)

#check each string one by one and insert '' on vacant  
#リスト化した文字を一つ一つ参照して、文字がからの('')の場合、文字を挿入する。
        
#counter will be increased
  counter = 0
    
  char_list_size = len(char_list)
  current_last_char = char_list[0]

  while counter < char_list_size:
    if char_list[counter] == '':
      inserted_string = inserted_string + insert_string
        
    else:
      inserted_string = inserted_string + current_last_char 
      current_last_char = char_list[counter]
    counter = counter + 1 
    
          

  return inserted_string