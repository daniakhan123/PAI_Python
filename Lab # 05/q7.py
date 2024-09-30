import re

def extract_emails(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    emails = re.findall(email_pattern, text)
    
    return emails

text = '''Hello, please contact us at DaniaKhan@example.com for more information.
You can also reach out to @FatehTextile.com or Zoni.Amjad@gmail.com.
'''

emails = extract_emails(text)
print("Extracted email addresses:", emails)
