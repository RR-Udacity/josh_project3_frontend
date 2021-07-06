import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = True
    POSTGRES_URL="project3-db.postgres.database.azure.com"  #TODO: Update value
    POSTGRES_USER="psql_admin" #TODO: Update value
    POSTGRES_PW="Password1"   #TODO: Update value
    POSTGRES_DB="project3-db"   #TODO: Update value
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = 'LWd2tzlprdGHCIPHTd4tp5SBFgDszm'
    SERVICE_BUS_CONNECTION_STRING ='Endpoint=sb://joshnotificationqueue.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=s1GqISsWQEQc6kKRGrwyowgsvdahTH0FZV1jc5cyDIQ=' #TODO: Update value
    SERVICE_BUS_QUEUE_NAME ='joshnotificationqueue'
    ADMIN_EMAIL_ADDRESS: 'Clark.Kent@joshhaines.com'
    SENDGRID_API_KEY = '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' #Configuration not required, required SendGrid Account

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False