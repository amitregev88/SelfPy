# Write script in python that send en email if condition exists in excel





# To send an email based on a condition in an Excel file, you can use Python with libraries such as `openpyxl` for reading Excel files and `smtplib` for sending emails. Here's a basic script that demonstrates how to do this:

# ```python

import openpyxl  '''for reading Excel file '''
import smtplib  ''' for sending emails'''
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Define the condition you want to check in the Excel file
condition_column = 'K'  # Change this to the column where your condition exists
condition_value = '=K2<TODAY()'  # Change this to the value you're looking for

# Load the Excel file
excel_file = 'your_excel_file.xlsx'  # Replace with the path to your Excel file
workbook = openpyxl.load_workbook(excel_file)
sheet = workbook.active

# Check the condition in the Excel file
for row in sheet.iter_rows(min_row=2, values_only=True):
    if row[1] == condition_value:  # Assuming the condition column is the second column (B)
        # If the condition is met, send an email
        subject = "Condition Met!"
        body = "The condition you were looking for exists in the Excel file."

        # Configure the email
        sender_email = 'your_email@gmail.com'  # Replace with your email
        sender_password = 'your_password'  # Replace with your email password
        receiver_email = 'receiver_email@gmail.com'  # Replace with the recipient's email

        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            server.quit()
            print("Email sent successfully!")
        except Exception as e:
            print("Email could not be sent. Error:", str(e))

# Close the Excel file
workbook.close()
```

Make sure to replace the placeholders with your actual values, such as the Excel file path, condition column, condition value, sender and receiver email addresses, and sender's email password. Additionally, you may need to allow less secure apps in your email account settings or generate an "App Password" for Gmail if you encounter authentication issues.

Best Regards,
Amit Regev
CORP/IT
 

Please consider the environment before printing this e-mail.
