#Assignment: Take a string input and print the number of occurrences of each character.
string = "Raj Pathak"
count = {} 
  
for char in string: 
   if char in count: 
      count[char] += 1
   else: 
      count[char] = 1

print ("The number of Occurrence of each character: in '{}' is:\n {}".format(string, str(count)))
