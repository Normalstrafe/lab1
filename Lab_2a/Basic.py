# 2.i Task
print("-------------------------------------------------------->")
print("First constant",False)
print("Second constant",__debug__)
print("Third constant",None)
#2.ii Task
print("-------------------------------------------------------->")
x= [1,2,3,4,5,6]
print("First function:",abs(10))
print("Second function",all(x))
#2.iii Task
print("-------------------------------------------------------->")
Y = 1
if Y == "True":
    print("X : True ")
else:
    print("X !: True")


while Y < 5:
    print("X =",Y)
    Y=Y+1
#2.iv Task
print("-------------------------------------------------------->")
A = "r";
e = "first"
try:
    print("Ділю число на символ", 10/A, "?")
except Exception as A:
    print(A);
finally:
    print("ну таке собі)");
#2.v Task
print("-------------------------------------------------------->")
with open('add tools.txt', 'w') as opened_file:
    opened_file.write('Function is work');
print("-------------------------------------------------------->")
import math
def SQRT(x):
    return math.sqrt(x)
SQR = lambda x: math.sqrt(x)
print(SQR(25));
