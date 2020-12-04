
import re


def welcoming():
    print(f"""
    *************************************************

            Welcome in the Madlib Game ....
            Are you Ready to have fun with me ? 
            I will be asking you to guess things about me  
            and be prepared to laugh hard
            LET'S GO ....

    *************************************************
    """)

welcoming() 


def read(path):
    with open(path,'r') as file:
     content = file.read()
    return content

read('assets/madlib_source.txt')


def questions():
    questions=['Somthing i like doing...',"Another thing i love ....","Guess My major  ....",
    "Enter a verb ends with ing :P ....","Write another verb my dear ^.^  ...."
    ]
    values=[]
    
    for i in questions:
        question= input(i)
        values.append(question)
    return values

def merge(text,answers):
    dataText = text
    answer=dataText.format(*answers)
    print(answer)   # returning the input that were answered by the user using formating the whole text, and replace it with the appended words (answers)
    return answer

with open('assets/madlib_result.txt', 'w') as file:
    file.write(merge(read('assets/madlib_source.txt'),questions()))
# print(merge('assets/madlib_source.txt',questions()

def parse(path):
    data=re.findall(r"\{(.*?)\}",read(path)) #finds all words between {}, and send then in a list 
    return data
print(parse('assets/madlib_source.txt'))    



 

 
  

  

