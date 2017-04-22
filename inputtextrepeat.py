def inputtextrepeat(prompt):
    while True:
        try:
            value=input(prompt)
        except TypeError:
            print("Sorry, try that again please")
            continue
        if value is 