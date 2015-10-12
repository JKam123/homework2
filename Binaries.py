Num = 100 #The Number we want to change the base of
Count = Num #The value to change during process
Base = 7#The base we want the number to change to
Exp = 0 #The start exponent is 0
Output = "" #The string output

while Num > (Base**Exp): # If the Number is greater than the new base to the power of the exponent then loop should run.
    Mod = Count%(Base**(Exp+1)) #Calculate the mod of the Remaining number and the base and exonent
    Numeral = Mod/(Base**Exp) #Calculate the numeral
    Count= Count - Mod #Set the chaning value to it self minus the mod value
    Output = Output + str(Numeral) #Add the numeral to the output string
    Exp = Exp + 1


print Output #When the while loop ends print the output which is our number with a different base
    
