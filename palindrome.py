word = int(input("enter the word:"))
n1 = word
if(word<0):
   print("negative")
else:
   newstr=str(word)
   m = newstr[::-1]
   if(m==word):
      print("palindrome")
   else:
      print("not palindrome")