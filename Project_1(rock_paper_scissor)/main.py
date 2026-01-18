import random

def optcheck(msg,opt1,opt2,opt3):
    ans=input(msg).lower()

    while ans!=opt1 and ans!=opt2 and ans!=opt3:
          print(f"please enter input in {opt1}/{opt2}/{opt3} only ")
          ans=input(msg).lower()

    return ans


def rock_paper_scissors():

    comp_score=0
    you_score=0

    again="y"
    while again=="y":

        computer=random.choice([1,2,3])
        youstr=optcheck(''' r-Rock\n p-Paper\n s-Scissor\n\n Enter ur input :    \n''',opt1='r',opt2='p',opt3='s').lower()
        
        dict={'r':1,'p':2,'s':3}
        rev_dict={1:'Rock 🪨',2:'Paper 📰',3:'Scissors ✄'}

        you=dict[youstr]


        print(f"You chose : {rev_dict[dict[youstr]]} \nComputer chose : {rev_dict[computer]}\n")

        if computer==you:
            print("It's a Draw! (ᵕ— ᴗ —)\n")
        else:
            if computer==1 and you==2:
                print("You Win! ( ദ്ദി ˙ᗜ˙ )\n")
                you_score+=1
            elif computer==1 and you==3:
                print("You Lose! .·°՞(っ-ᯅ-ς)՞°·.\n")
                comp_score+=1
            elif computer==2 and you==1:
                print("You Lose! .·°՞(っ-ᯅ-ς)՞°·.\n")
                comp_score+=1
            elif computer==2 and you==3:
                print("You Win! ( ദ്ദി ˙ᗜ˙ )\n")
                you_score+=1
            elif computer==3 and you==1:
                print("You Win! ( ദ്ദി ˙ᗜ˙ )\n")
                you_score+=1
            elif computer==3 and you==2:
                print("You Lose! .·°՞(っ-ᯅ-ς)՞°·.\n")
                comp_score+=1
            else:
                print("Something went wrong!\n")
        again=optcheck("Roll again?(y) or Exit!(n) : \n", opt1="y",opt2="n",opt3=None).lower()
    print(f"Your score: {you_score}\nComputer\'s score: {comp_score} ")

rock_paper_scissors()
