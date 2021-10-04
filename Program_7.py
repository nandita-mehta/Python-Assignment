email = input("Enter Email:")
print("The original string is : " + str(email))
company_name = email[email.index('@') + 1:email.index('.')]
print("The extracted company name is : " + str(company_name))
