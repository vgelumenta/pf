def alphabets_upto(letter):
    for i in range (65, ord(letter)+1):
        yield chr(i)

if __name__ == "__main__":

    alphabets_upto_D = alphabets_upto('D')
    alphabets_upto_I = alphabets_upto('I')
    alphabets_upto_N = alphabets_upto('N')

    for alpha in alphabets_upto_D:
        print(alpha, end=" ")
    
    print()

    for alpha in alphabets_upto_I:
        print(alpha, end=" ")
    
    print()

    for alpha in alphabets_upto_N:
        print(alpha, end=" ")