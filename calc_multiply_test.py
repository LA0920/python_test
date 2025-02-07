#Test 1: Verification of multiplication function
#Positive test
def test_multiply():
    #Define the first number
    a = 2
    #Define the second number
    b = 3
    #Perform the multiplication operation
    multiply = a * b
    #Check if the user gets the expected value
    assert multiply == 6
    print("Test passed! The product of " + str(a) + " and " + str(b) + " is equal to " + str(multiply) + "!")