import copy
import string

def parse_process(expression, dict_data):
     string_rep = dict_data.replace("{", "")
     string_rep = string_rep.replace("}", "")
     string_data = string_rep

     # Converting string to dictionary
     Dict = dict((x.strip(), y.strip())
                for x, y in (element.split(':')
                             for element in string_data.split(', ')))
     dict_da = {}
     for i in Dict:
        dict_value = Dict[i].replace("'", "")
        dict_value = Dict[i].replace('"', "")
        i = i.replace("'", "")
        i = i.replace('"', "")
        dict_da[i] = dict_value
     dict_data = dict_da
     # To find parentesis value
     if '(' and ')' in expression:
         find_parenthes_value = expression[expression.find("(")+1:expression.find(")")]
         count =0
         for l in find_parenthes_value:
             if l.isupper():
                 try:
                        if dict_data[l]:
                            if count == 1:
                                del dict_data[l]
                            else:
                                count = count+1
                 except:
                     pass
     # To find OR expression
     if '(' and ')' not in expression and 'or' in expression:
         count = 0
         for l in expression:
             if l.isupper():
                 try:
                     if dict_data[l]:
                         if count == 1:
                             del dict_data[l]
                         else:
                             count = count + 1
                 except:
                     pass
     # Replace And Or
     copy_deep = copy.copy(expression)
     if 'and' in copy_deep or 'or' in copy_deep:
             copy_deep = copy_deep.replace("and", "")
             copy_deep = copy_deep.replace("or", "")

     for i in dict_data:
         if i in expression:
            copy_deep = copy_deep.replace(i, dict_data[i].lower())
         else:
             copy_deep = copy_deep.replace(i, i)

     for i in dict_data:
         if i in expression:
            copy_deep = copy_deep.replace(i,"")
         else:
             copy_deep = copy_deep.replace(i, i)

     for i in list(copy_deep):
         if i == ')' or i == '(':
             copy_deep = copy_deep.replace(i, " ")
         elif i.isupper():
             copy_deep = copy_deep.replace(i, "")
     fresh_word = copy_deep.replace("'", " ")
     fresh_word_caps = string.capwords(fresh_word)
     fresh_word_final = fresh_word_caps.replace(" ", "")
     return fresh_word_final


if __name__ == '__main__':
    user_expression = input("Enter your expression: ")
    user_dict = input("Enter your dictionary: ")


    if user_expression.strip() != '' and user_dict.strip() != '':
        get_output = parse_process(user_expression,user_dict)
        print(get_output)
    else:
        print("Enter valid data in the below format!")
        print("Enter your expression: A and B and C <--(like that)")
        print("Enter your dictionary: {'A':'Hello', 'B':'World', 'C':'Buddy', 'D':'Test'}")
        exit()
