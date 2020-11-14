import random
import time
import string
def generate_hard_word():
    hard_word = ""
    while len(hard_word) < 35:
        hard_word += random.choice(string.ascii_lowercase)
        if len(hard_word) % 6 == 0:
            hard_word += " "
        hard_word += random.choice(string.ascii_uppercase)
        if len(hard_word) % 6 == 0:
            hard_word += " "
        hard_word += random.choice(string.digits)
        if len(hard_word) % 6 == 0:
            hard_word += " "
        hard_word += random.choice(string.ascii_lowercase)
        if len(hard_word) % 6 == 0:
            hard_word += " "
        hard_word += random.choice(string.ascii_uppercase)
        if len(hard_word) % 6 == 0:
            hard_word += " "
        hard_word += random.choice(string.punctuation)
        if len(hard_word) % 6 == 0:
            hard_word += " "
        hard_word += random.choice(string.ascii_lowercase)
        if len(hard_word) % 6 == 0:
            hard_word += " "
        hard_word += random.choice(string.ascii_lowercase)
    hard_word=hard_word.split()
    lst=[]
    for x in hard_word:
        x=list(x)
        random.shuffle(x)
        lst.append("".join(x))
    random.shuffle(lst)
    return " ".join(lst)

while 1>0:
    try:
        choice=input("please enter level of difficulty(1/2/3): ")
        if len(choice)<1 or len(choice)>1:
            raise NameError

    except NameError:
        continue
    else:
        if choice=="1" or choice=="2" or choice=="3":
            break
while 1>0:
    typos=input(r"do you want typos count?(y\n) ")
    if typos.lower() in ["y","n"]:
        break
list_of_word = ["thailnd", "i love you so much", "happy vibes"]
while 1>0:
    repeat=True
    last_score = ""
    high_score = 0
    if choice=="1":
        try:
            word = random.choice(list_of_word)
        except:
            print("run out of words")
            break
    elif choice=="3":
        word=generate_hard_word()
    while repeat:
        print("you need to type:\n"+word)
        result=""
        start=time.time()
        while 1>0:
            try:
                result=input()
                if len(result)<1:
                    raise NameError
            except NameError:
                continue
            else:
                break
        end=int(time.time()-start)
        accuracy=0
        if len(last_score)>0:
            print(last_score)
            if high_score>end:
                high_score=end
            print("Your fastest try is: " + str(high_score))
        else:
            high_score=end
        lol=list(map(lambda x,y:1 if x==y else 0,[letter for letter in word],[letter for letter in result]))
        if typos.lower()=="n":
            print("your time is:",end,"seconds\tyour accuracy is:",str(int((sum(lol)/len(lol))*100))+"%")
        else:
            print("your time is:",end,"seconds\tyour accuracy is:",str(int((sum(lol)/len(lol))*100))+"%\t and you have: "+str(len(lol)-sum(lol))+" typos")
        last_score="".join(["your last test time: ",str(end)," seconds\tyour last test accuracy is: ",str(int((sum(lol)/len(lol))*100))+"%"])
        check=""
        while check.lower() not in ["y","n"]:
            check=input(r"Do you want to repeat last test?(y\n) ")
        if check.lower()=="n":
            if word in list_of_word:
                list_of_word.remove(word)
            repeat=False
