
# coding: utf-8

# In[117]:

def valid(answers,cod):
    import math
    _sum = 0
    for el in answers:
        _sum += len(el)
    _sum += len(cod)
    answer = math.sqrt(_sum)
    return (0 == answer - int(answer),answer)

def fillCrossvord(answer,size):
    size = int(size)
    crossword = pd.DataFrame([['z' for i in range(size)] for i in range(size)])
    return crossword
import random
import re
import pandas as pd


# In[118]:

import random
import re
import pandas as pd
def crossword(path,codeword,level):
    def valid(answers,cod):
        import math
        _sum = 0
        for el in answers:
            _sum += len(el)
        _sum += len(cod)
        answer = math.sqrt(_sum)
        return (0 == answer - int(answer),answer)

    def fillCrossvord(answer,size):
        size = int(size)
        crossword = pd.DataFrame([['z' for i in range(size)] for i in range(size)])
        return crossword

    if 0 > level and level >4:
        level = 3
    file = open(path)
    question = list()
    answer = list()
    temp = 2
    for el in file:
        if el[:9] == 'Questions':
            temp = 0   
        elif temp ==0 and el[:7] != "Answers":
            t = re.findall("\([0-9]+\)",el)
            count.append(t)
            _el = el[:-1]
            _el = _el.split(".")
            question.append(_el)
        if el[:7] == "Answers":
            temp =1
        elif temp ==1:
            _el = el[:-1]
            _el = _el.replace(" ","") 
            _el = _el.split(".")
            answer.append(_el[1])
    file.close()
    if not valid(answer,codeword)[0]:
        return "Invalid format Matrix should be a square matrix"
    else:
        mydict= {1:fill_words_crossword_1 ,2:fill_words_crossword_2,3:fill_words_crossword_3,4:fill_words_crossword_4}
        size = int(valid(answer,codeword)[1])
        frame_Question = pd.DataFrame([el[1] for el in question],columns= ['Question'], index=range(1,len(question)+1))
        frame_task = fillCrossvord(answer,size)
        x = mydict[level](frame_task,answer,codeword)
        for i in range(size,len(question)):
            t = ["-" for i in range(size)]
            x.loc[i] = t
        
        x['-'] = pd.DataFrame(["-" for i in range(len(question))])
        x['Question'] = pd.DataFrame([el[1] for el in question],columns= ['Question'], index=range(len(question)))
        ques = pd.DataFrame([el[1] for el in question],columns= ['Question'], index=range(1,len(question)+1))
    return x.iloc[:23]
crossword(r'C:\Users\Иван\Desktop\crossvord\var2.txt','кроссворд',4)


# In[119]:

def fill_words_crossword_1(crossword,answers,code):
    answers.extend(code.upper())
    temp = ''.join(answers).upper()
    i,k = 0,0
    while True:
        if i == crossword.shape[0]:
            return crossword
        for j in range(crossword.shape[0]):
            crossword.iloc[i][j] = temp[k]
            k+=1
        i +=1 
        if i == crossword.shape[0]:
            return crossword
        for j in range(crossword.shape[0]-1,-1,-1):
            crossword.iloc[i][j] = temp[k]
            k+=1
            if k == len(temp):
                return crossword
        i+=1


# In[120]:

def fill_words_crossword_2(crossword,answers,code):
    answers.extend(code.upper())
    temp = ''.join(answers).upper()
    j,k = 0,0
    while True:
        if j == crossword.shape[0]:
            return crossword
        for i in range(crossword.shape[0]):
            crossword.iloc[i][j] = temp[k]
            k+=1
        j +=1 
        if j == crossword.shape[0]:
            return crossword
        for i in range(crossword.shape[0]-1,-1,-1):
            crossword.iloc[i][j] = temp[k]
            k+=1
            if k == len(temp):
                return crossword
        j+=1


# In[121]:

def fill_words_crossword_3(crossword,answers,code):
    answer.extend(code)
    answers.sort(key = lambda x : x[0])
    temp = ''.join(answers).upper()
    
    i,k = 0,0
    while True:
        if i == crossword.shape[0]:
            return crossword
        for j in range(crossword.shape[0]):
            crossword.iloc[i][j] = temp[k]
            k+=1
        i +=1 
        if i == crossword.shape[0]:
            return crossword
        for j in range(crossword.shape[0]-1,-1,-1):
            crossword.iloc[i][j] = temp[k]
            k+=1
            if k == len(temp):
                return crossword
        i+=1


# In[115]:

def fill_words_crossword_4(crossword,answers,code):
    answers.extend(code.upper())
    answers.sort(key = lambda x : x[0])
    temp = ''.join(answers).upper()
    j,k = 0,0
    while True:
        if j == crossword.shape[0]:
            return crossword
        for i in range(crossword.shape[0]):
            crossword.iloc[i][j] = temp[k]
            k+=1
        j +=1 
        if j == crossword.shape[0]:
            return crossword
        for i in range(crossword.shape[0]-1,-1,-1):
            crossword.iloc[i][j] = temp[k]
            k+=1
            if k == len(temp):
                return crossword
        j+=1


# In[109]:




# In[77]:




# In[ ]:



