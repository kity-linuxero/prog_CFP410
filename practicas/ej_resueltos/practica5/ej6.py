# Escriba una función que valide una _dirección de e-mail_ (retorne True o False según el caso).
# La dirección de e-mail se compone de `<nombre>@<sub-dominio>.<dominio>.<dominio2>.

def isEmailValid(a_email):
    invalid = not (
        ('@' in a_email) and 
        ('.' in a_email) and 
        (a_email.count('@') == 1) and
        (a_email[-1]!='.') and
        (a_email[0]!='@')
        ) # Verifica si hay una @ y '.'. Si no hay, Directamente descarta
    if invalid:
        return False
    else: # Verifico el dominio.
        email, domains = a_email.split("@")
        
        if invalid:
            return False
        else:
            return True


    