import re
with open("emails.txt", "r") as file:
    text = file.read()
emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)
with open("extracted_emails.txt", "w") as file:
    for email in emails:
        file.write(email + "\n")
print("Email addresses found:")
for email in emails:
    print(email)
print("Total emails found:", len(emails))
print("Emails saved to extracted_emails.txt")