alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

should_continue= True
def cipherText(encodeOrDecode,text,shift_amount):
    result_text = ""
    for letter in text:
        if letter in alphabets:
            if encodeOrDecode == "Encode":
                new_letter_index = alphabets.index(letter)+shift_amount
            else:
                new_letter_index = alphabets.index(letter)-shift_amount
            new_letter_index %= len(alphabets)
            result_text += alphabets[new_letter_index]
        else:
            result_text +=letter       
    print(f"Here is {direction}d code", result_text)

while should_continue:
    direction = input("Type 'Encode to encrypt.\nType 'Decode to decrypt.\n")
    message = input("Type your message.\n").lower()
    shift_num = int(input("Type the shift number.\n"))
    cipherText(direction,message,shift_num)
    restart = input("Type 'yes' to continue and 'no' to discontine\n")
    if restart == 'no':
        should_continue = False
        print("Thanks for using cypher programe. See you soon!")