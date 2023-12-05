import requests
import pandas as pd
from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
import smtplib
from email.mime.text import MIMEText

# SharePoint credentials
sharepoint_url = "https://your-sharepoint-url.com/sites/your-site"
client_id = "your-client-id"
client_secret = "your-client-secret"
tenant_id = "your-tenant-id"

# Email credentials
sender_email = "your-email@example.com"
smtp_server = "smtp.example.com"
smtp_port = 587
smtp_username = "smtp-username"
smtp_password = "smtp-password"

# Read Excel file from SharePoint
def read_excel_from_sharepoint():
    # Get access token using client credentials (client ID and client secret)
    token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"
    token_data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
        'resource': 'https://graph.microsoft.com'
    }
    token_response = requests.post(token_url, data=token_data).json()
    access_token = token_response['access_token']

    # Authenticate with SharePoint using access token
    ctx_auth = AuthenticationContext(sharepoint_url)
    ctx_auth.acquire_token_for_app(client_id, client_secret)
    ctx = ClientContext(sharepoint_url, ctx_auth)

    # Specify the path to the Excel file in SharePoint
    file_path = "/sites/your-site/Shared Documents/YourExcelFile.xlsx"

    # Download the Excel file
    response = ctx.web.get_file_by_server_relative_path(file_path).download().execute_query()
    
    # Read the Excel file into a DataFrame
    df = pd.read_excel(pd.BytesIO(response.content))

    return df

# Send email if the condition exists
def send_email_if_condition_exists(df):
    # Your condition logic goes here
    condition_exists = df['B'].any() == 'YourCondition'

    if condition_exists:
        # Extract the receiver email from the "B" column
        receiver_email = df.loc[df['B'] == 'YourCondition', 'B'].values[0]

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
        print(f"Email sent successfully to {receiver_email}")
    else:
        print("Condition does not exist in the Excel file")

if __name__ == "__main__":
    # Read Excel from SharePoint
    excel_df = read_excel_from_sharepoint()

    if excel_df is not None:
        # Check condition and send email if it exists
        send_email_if_condition_exists(excel_df)
