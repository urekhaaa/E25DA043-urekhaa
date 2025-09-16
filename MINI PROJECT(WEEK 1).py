import re #regular expressions

print("=== Password Strength Checker ===")  #basic string topic
password = input("Enter your password: ")

length_ok = len(password) >= 8        #string manipulation                
upper_ok = re.search(r"[A-Z]", password) is not None  #regular expressions
lower_ok = re.search(r"[a-z]", password) is not None  
digit_ok = re.search(r"[0-9]", password) is not None  
special_ok = re.search(r"[@$!%*#?&]", password) is not None

if length_ok and upper_ok and lower_ok and digit_ok and special_ok: #conditional formating
    print("✅ Strong Password")
else:
    print("❌ Weak Password. Fix the following:")
    if not length_ok:
        print("- Password must be at least 8 characters long")
    if not upper_ok:
        print("- Must contain an uppercase letter")
    if not lower_ok:
        print("- Must contain a lowercase letter")
    if not digit_ok:
        print("- Must contain a digit")
    if not special_ok:
        print("- Must contain a special character (@, $, !, %, *, #, ?, &)")
