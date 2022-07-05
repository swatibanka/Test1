
s = 'this is My First Python programming class and i am learNING python string and its function'

#Question 1
q1 = s[0:301:3]
print(q1)

#Question2
q2=s[::-1]
print(q2)

#question3
q3=s.upper()
q3_1=q3.split()
print(q3_1)

#question4
q4=s.lower()
print(q4)

#question5
q5=s.capitalize()
print(q5)

#question6
q6 = """ isalnum() will check whether all the character of the given string is either Alphabet or Number. It returns True 
        if any of this condition(Alphabet or Number) satisfied.
        isalpha() will check whether all the character of the given string is Alphabet. It returns True only when all characters
        are Alphabet. 
        """
#question 7
#expand tab is a built-in method of python which replace all the character of a string to a specified white space.
#example: str.expandtabs(tab size = 6)

q7='this\tis\tmy\tfirst\tday\tof\tcoding'
q7_1=q7.expandtabs(8)
print(q7_1)

#question 8
#strip trim from both left and right, lstrip from left or beginning and rstrip from right or end.
q8= "    Welcome to my first day of coding       "
q8_1 = q8.strip()
q8_2 = q8.lstrip()
q8_3 = q8.rstrip()
print(q8_1)
print(q8_2)
print(q8_3)

#question9
q9 = "This is my first day of coding"
print(q9.replace('This is','Welcome to'))

#question10
#Python string center makes the given string center align by using the specific character as the filling character.
#If filling character is not specified, it will take space as bydefault.

q10 = "ClassofBasicPython"
print(q10.center(25,'#'))
print(q10.center(30))
print(q10.center(35,'@'))

#question11
Q11 = """" Complier translate the entire source code in one single run where as Interpreter translate it line by line. 
Complier take less time to run than interpreter.
To check on the errors are easier in Interpreter than Complier, as in case of error rest of the code will stop running in interpreter
"""

#question12
Q12 = """As per my understanding Python is an Interpreter. In simple terms, python translate the entire source code line by line.
Instead of translating the source code to some machine code like some other languages(C++ and Java), it translate to bytecode and
this bytecode is exectued by Interpreter.

One more advantage is Python Interpreter is platform independent.
"""

#Question 13
Q13="""Data Science and Data Analytics are one of the most important areas with the applications of python programming.

Libraries like numpy, pandas, scipy etc help the user to extract data, read and analyzise data.
With the help of matplot lib and Seaborn, user can generate various kind of graphs, which helps in providing various insights
    of the companies.
"""

