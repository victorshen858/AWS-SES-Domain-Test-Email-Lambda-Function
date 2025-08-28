import json
import boto3

# Initialize AWS SES client in desired region
ses_client = boto3.client('ses', region_name='us-gov-west-1')  # Change region if needed

def lambda_handler(event, context):
    """
    Sends a test email to recipients defined in config.json.
    """
    # Load configuration from event or use built-in defaults
    config = event.get('config', {
        "FROM_EMAIL": "do-not-reply@INSERT_YOUR_VERIFIED_DOMAIN_HERE.com",
        "TO_EMAILS": [
            "test_user_1@INSERT_VERIFIED_DOMAIN_HERE.com",
            "test_user_2@INSERT_VERIFIED_DOMAIN_HERE.com"
        ],
        "SUBJECT": "SES Test Email",
        "BODY": "This is a test email sent via AWS SES using Lambda."
    })

    from_email = config["FROM_EMAIL"]
    to_emails = config["TO_EMAILS"]
    subject = config["SUBJECT"]
    body_text = config["BODY"]

    try:
        response = ses_client.send_email(
            Source=from_email,
            Destination={'ToAddresses': to_emails},
            Message={
                'Subject': {'Data': subject},
                'Body': {'Text': {'Data': body_text}}
            }
        )
        return {
            'statusCode': 200,
            'body': f"Email sent successfully! Message ID: {response['MessageId']}"
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Error sending email: {str(e)}"
        }
