import IPA_classes as ipa_c

expression = ""

def ipa_key(elem, user_input):
    global expression
    expression = expression + str(elem)
    user_input.set(expression)

def clear_key(user_input, sonority):
    global expression
    user_input.set("")
    sonority.set("")
    expression = ""

def done_key(user_input):
    try:
        global expression
        result = ipa_c.sounds_to_obj_MOP(expression)
        user_input.set(result)
        expression = result
    except:
        user_input.set(" error ")
        expression = ""

def ssg_key(user_input, sonority):
    try:
        global expression
        result = ipa_c.sounds_to_obj_SSG(expression)
        sonority.set(result)
        expression = ""
    except:
        sonority.set(" error ")
        expression = ""
