import Tkinter
import random
'''wellcome to the ibarkay Gusess the Number Game'''

###code



def check():
    global trys
    #get the value from text_guess
    user_guess = int(txt_guss.get())

    #tell lower or higer
    if user_guess < computer_guess:
        msg = 'Higer!'
    elif user_guess > computer_guess:
        msg = 'lower'
    elif user_guess == computer_guess:
        msg = 'Correct!'
    else:
        msg = 'Somthing wwnt wrong...'

    trys +=1
    labl_trys['text'] =  "Try's "+str(trys)
    #show result
    if msg == 'Correct!':
        labl_result['fg']='green'
        labl_result['text']= msg
    else:
        labl_result["text"] = msg



def reset():
    global computer_guess
    computer_guess = random.randint(1,100)
    labl_result['fg']='black'
    labl_result['text']=''
#end code

#vars
computer_guess = random.randint(1,100)
trys = 0

#init 
root = Tkinter.Tk()
root.title('Guess the Number by ibarkay')

#creat wiget
txt_guss = Tkinter.Entry(root,width=3)
txt_guss.pack()

labl_title = Tkinter.Label(root, text="Wellcom to Gusee the Number!")
labl_title.pack()

labl_result = Tkinter.Label(root, text="Good luck",)
labl_result.pack()

labl_trys = Tkinter.Label(root, text="Try's "+str(trys))
labl_trys.pack(side='top')

btn_check = Tkinter.Button(root, text='Check', fg='green', command=check)
btn_check.pack(side='left')

btn_rest = Tkinter.Button(root, text='Reset', fg='red', command=reset)
btn_rest.pack(side='right')



#start the main tk loop
root.mainloop()
root.destroy()
