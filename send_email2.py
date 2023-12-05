# Write a script in Python that sends an email if the condition exists in Excel that locate in share point 
# pip install pandas openpyxl Office365-REST-Python-Client




import pandas as pd
from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
import smtplib
from email.mime.text import MIMEText

# SharePoint credentials
sharepoint_url = "https://klatencor.sharepoint.com"
username = "Amit.Regev@kla-tencor.com"
password = "2wsx@WSX"

# Email credentials
sender_email = "Amit.Regev@kla-tencor.com"
receiver_email = "Amit.Regev@kla-tencor.com"
smtp_server = "smtp-mail.outlook.com"
smtp_port = 587
smtp_username = "Amit.Regev@kla-tencor.com"git
smtp_password = "2wsx@WSX"

# Read Excel file from SharePoint
def read_excel_from_sharepoint():
    ctx_auth = AuthenticationContext(sharepoint_url)
    if ctx_auth.acquire_token_for_user(username, password):
        ctx = ClientContext(sharepoint_url, ctx_auth)
        web = ctx.web
        ctx.load(web)
        ctx.execute_query()

        # Specify the path to the Excel file in SharePoint
        file_path = "https://klatencor.sharepoint.com/:x:/r/teams/IT-Israel/Shared%20Documents/Cellphones%20(Partner)/Cellphones%20asset%20management.xlsx"

        # Download the Excel file
        response = ctx.web.get_file_by_server_relative_path(file_path).download().execute_query()
        
        # Read the Excel file into a DataFrame
        df = pd.read_excel(pd.BytesIO(response.content))

        return df
    else:
        print("Failed to authenticate with SharePoint")
        return None

# Send email if the condition exists
def send_email_if_condition_exists(df):
    # Your condition logic goes here
    condition_exists = df['K'].any() == '=K2<TODAY()'

    if condition_exists:
        # Email content
        subject = "Condition Exists in Excel"
        body = "The condition you are looking for exists in the Excel file."

        # Compose the email
        message = MIMEText(body)
        message["Subject"] = subject
        message["From"] = sender_email
        message["To"] = receiver_email

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully")
    else:
        print("Condition does not exist in the Excel file")

if __name__ == "__main__":
    # Read Excel from SharePoint
    excel_df = read_excel_from_sharepoint()

    if excel_df is not None:
        # Check condition and send email if it exists
        send_email_if_condition_exists(excel_df)
