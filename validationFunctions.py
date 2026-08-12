import turtle

def inputValidation(title:str,text:str,listElements:list[str],screen:turtle.Screen) -> str:
    """Returns a String if the user input is a valid element."""

    while True:
        try:
            entry= screen.textinput(title,text).lower()
            lowerList=list(map(str.lower,listElements)) #Transform the list elements in lower case

        except Exception as e:
            turtle.TK.messagebox.showinfo(title="Alert",message=e)  

        else:

            if entry in lowerList:
                return entry
            elif entry == "" or entry == " ":
                message=f"Space is an invalid option, please select one of this options {listElements}"
            else:
                message=f"{entry} is an invalid option, please select one of this options {listElements}"

            turtle.TK.messagebox.showinfo(title="Alert",message=message)  
