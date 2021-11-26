alpha=[chr(i) for i in range(97,97+26)]

def encrypt(text):
    res=''
    for c in text:
        if(c.isalpha()):
            res=res + alpha[ (10+alpha.index(c))%26 ]
        else:
            res=res+c
    return res

def decrypt(text):
    res=''
    for c in text:
        if(c.isalpha()):
            res=res + alpha[ (alpha.index(c)-10)%26 ]
        else:
            res=res+c
    return res





message = "this is a sample text. 3 times 3 is 9"
message ='''
dro mvel scx'd dro locd zvkmo dy psxn k vyfob
cy dro lkb sc grobo s qy
wo kxn wi pbsoxnc kd dro dklvo nysxq crydc
nbsxusxq pkcd kxn drox go dkvu cvyg
kxn iye mywo yfob kxn cdkbd ez k myxfobckdsyx gsdr tecd wo
kxn dbecd wo s'vv qsfo sd k mrkxmo xyg
dkuo wi rkxn, cdyz, zed fkx dro wkx yx dro teuolyh
kxn drox go cdkbd dy nkxmo, kxn xyg s'w csxqsxq vsuo
'''


message=message.lower()
#encrypted = encrypt(message)
decrypted = decrypt(message) # decrypting the encrypted message

print("encrypted :",encrypted)
print("decrypted :",decrypted)

