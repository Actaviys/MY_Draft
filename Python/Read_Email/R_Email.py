from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import datetime
import os
import pickle

def get_gmail_service():
    SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
    creds = None
    
    # Завантажуємо токен доступу, якщо він є
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # Якщо немає дійсного токену, виконуємо автентифікацію
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('client_secret_985666306500-s30kdpb2ht20kre40otpksrpuusndfv4.apps.googleusercontent.com.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Зберігаємо токен для подальшого використання
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('gmail', 'v1', credentials=creds)

def get_recent_emails(hours):
    service = get_gmail_service()
    query_time = (datetime.datetime.utcnow() - datetime.timedelta(hours=hours)).isoformat() + 'Z'
    
    results = service.users().messages().list(userId='me', q=f'after:{query_time}').execute()
    messages = results.get('messages', [])

    for message in messages:
        msg = service.users().messages().get(userId='me', id=message['id']).execute()
        headers = msg['payload']['headers']
        sender = next(header['value'] for header in headers if header['name'] == 'From')
        subject = next((header['value'] for header in headers if header['name'] == 'Subject'), '(Без теми)')
        print(f'Відправник: {sender}')
        print(f'Тема: {subject}')
        print('-' * 40)

# Виклик функції: читаємо листи за останні 3 години
get_recent_emails(3)
