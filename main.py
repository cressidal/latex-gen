from percentages import *
from latex_gen import *

a = pcQuant()
b = incDecQuant()
c = wotPc()

question_list = [a,b,c]

print(wrapQuestion(question_list))
