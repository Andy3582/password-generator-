

import random
import string 

print("Hello , welcome to Password generator !")


length = int( input( "n\enter the lenght of password :"))

lower= string.ascii_lowercase
upper= string.ascii_uppercase
num	= string.digits
symbols = string.punctuation

all = lower + upper + num + symbols 


temp = random.sample( all+length)

password = "".join(temp )

print(password)





