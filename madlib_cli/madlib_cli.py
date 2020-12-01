
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
    return (content)

read('assets/madlib_source.txt')




def merge(path):
    questions=['Somthing i like doing...',"Another thing i love ....","Guess My major  ....",
    "Enter a verb ends with ing :P ....","Write another verb my dear ^.^  ...."
    ]
    values=[]
    
    for i in questions:
        question= input(i)
        values.append(question)
    dataText = read(path)
    answer=dataText.format(*values)   
    return answer
with open('assets/madlib_result.txt', 'w') as file:
    file.write(merge('assets/madlib_source.txt'))


print(merge('assets/madlib_source.txt'))


def parse(path):
    data=re.findall(r"\{(.*?)\}",read(path))
    return data
print(parse('assets/madlib_source.txt'))    



 

 
  

  

