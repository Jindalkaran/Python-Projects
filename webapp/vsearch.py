def search4letters(arg,letters='aeiou'):
    letter=set(letters)
    found=letter.intersection(set(arg))
    return str(found)

def karan(me):
    me=me*2
    return me
