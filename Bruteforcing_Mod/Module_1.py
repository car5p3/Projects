import random
import pyautogui
from requests.models import guess_filename

chars = "abcdefghijklmnopqrstuvwxyz)(-+*&^%$#@!~`;:'/?><,.|\ "
charslist = list(chars)
password =pyautogui.password("Enter a password :")
guesspassword = ""
while( guesspassword != password):
    guesspassword = random.choices(charslist,k=len(password))

    print("<=================="+ str(guesspassword)+ "==================>")

    if(guesspassword==list(password)):
        print("Your password is : "+ "".join(guesspassword))
        break