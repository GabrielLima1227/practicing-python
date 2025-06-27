email = input("What's your email address? ")

print(f"Username: {email.split('@')[0]}")
print(f"Domain: {email.split('@')[1]}")
# 0r
print(f"Username: {email[0:email.find("@"): 1]}")
print(f"Domain: {email[email.find("@") + 1::1]}")