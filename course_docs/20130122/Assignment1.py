"""
Assignment 1
Due January 29, 2013

Create python code that encodes and decodes a string given a password
If you add your code to the 'encode' and 'decode' functions, and run it, it should print 'Success!'

"""

def encode(input, pwd):
    """ Takes two strings and transforms them into a third, encoded string """

    encoded_string = ''
	for i in range(math.ceiling(len(input)+len(pwd)/2)):
    	encoded_string += input[i]+pwd[i+1]
    return encoded_string


def decode(encoded, password):
    """ Takes an encoded string (from encode function) and a password and returns the orginal string"""

    decoded_string = ''

    return decoded_string


if __name__ == "__main__":

   teststring = "This is some text to be encoded"
   testpwd = "Password"
   print encode("Harry","Yankees")
   # assert(teststring != encode(teststring,testpwd))
   # assert(testpwd != encode(teststring,testpwd))
   # assert(encode(teststring,"wrongpwd") != encode(teststring,testpwd))
   # assert(teststring == decode(encoded,testpwd))
   # print "Success!"
