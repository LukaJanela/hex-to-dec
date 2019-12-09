#start_over variable controls outer loop and terminates whole program if it's false
start_over = True

while start_over:
    print ('\n-------This program converts hexadecimal to decimal-------\n')

    #takes hex input as string and reverses it
    #reversal is needed so I can start from the back of the number
    # therefore going up in powers(0, 1, 2...)
    hex_input = input('Input your hexadecimal number: ')[::-1]

    #decimal output adds up every number in for loop
    #power is used in for loop to raise 16 to the appropriate power
    decimal_output = 0
    power = 0

    #dictionary of hexadecimal characters to convert A-F, a-f to decimal numbers
    hex_dict = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15, 'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}

    #iterates over inputted string
    for char in hex_input:
        #if a char is in above dictionary, find it's value, raise 16 to the power variable and multiply by this value
        if char in hex_dict:
            decimal_output += hex_dict[char] * (16**power)
            power += 1
        #if char is not in dictionary, then it's just a decimal as string
        else:
            #convert it to integer and do the same operations on it as above
            decimal_output += int(char) * (16**power)
            power += 1

    print ('Your decimal number is: ' + str(decimal_output) + '\n')
    
    #yes_no variable controls inner loop, when user has to input y/n to start over or terminate program
    yes_no = True

    while yes_no:
        #ask user for input
        terminator = input ('Would you like to continue? (y/n): ')

        #if answer's y, get out of this loop and start the program from again (outer loop is still true)
        if terminator == 'y':
            yes_no = False
        #if answer's n, get out of both loops, therefore, terminating program altogether
        elif terminator == 'n':
            yes_no = False
            start_over = False
        #if user inputs anything else than y/n, it's incorrect input, therefore we ask him again for input
        else:
            continue

