# Create a welcome message.
# Input: a name as a string
# Result: a string
def welcome_message(a:str) -> str:
   message = "Hello, " + a + "."

   return message


message = welcome_message("lsindhu@calpoly.edu")
print(message)
