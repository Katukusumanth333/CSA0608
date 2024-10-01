words=["abc","car","ada","racer","cool"]
palindrome=next((word for word in words if word == word[::-1]),"")
print("The first paldromic is:",palindrome)
