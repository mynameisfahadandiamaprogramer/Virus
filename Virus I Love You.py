import os
c=input("say me 'i love you \n or\n ready to shutdown your computer :")
while True:

        if c == 'i love you':
            c = input("say Again 'i love you \n or\n ready to shutdown your computer :")
        else:
            s = os.system("shutdown /r /t 1")
            print(s)
