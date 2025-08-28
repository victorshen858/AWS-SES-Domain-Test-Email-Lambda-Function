# AWS-SES-Domain-Test-Email-Lambda-Function
This AWS Lambda function sends a test email (to one or multiple email recipients wihtou using SNS) using **AWS SES**. It is designed to work with any verified SES domain in your AWS account.

# SES Test Email Lambda

This AWS Lambda function sends a test email using **AWS SES**. It is designed to be generic and work with any verified domain in your AWS account.

## Features

- Sends a test email to multiple recipients.
- Can use **built-in defaults** or **config.json** from S3.
- Fully configurable from the Lambda environment or event payload.
- CloudFormation and Terraform deployment supported.

## Requirements

1. AWS account with SES enabled.
2. Verified domain in SES.
3. Request production access in SES if sending to unverified recipients.
4. IAM role with `ses:SendEmail` permission for the Lambda.

## Configuration

Optional config.json:

```json
{
    "FROM_EMAIL": "do-not-reply@YOUR_VERIFIED_DOMAIN.com",
    "TO_EMAILS": [
        "test_user_1@YOUR_VERIFIED_DOMAIN.com",
        "test_user_2@YOUR_VERIFIED_DOMAIN.com"
    ],
    "SUBJECT": "SES Test Email",
    "BODY": "This is a test email sent via AWS SES using Lambda."
}
```
Place in an S3 bucket and provide bucket name in CONFIG_S3_BUCKET environment variable.

If missing, defaults inside Lambda are used.

## Deployment

### CloudFormation
```json
aws cloudformation deploy \
  --template-file ses-test-email.yaml \
  --stack-name ses-test-email-lambda \
  --capabilities CAPABILITY_NAMED_IAM
```

**Replace placeholders in the YAML:**

INSERT_ACCOUNT_ID_HERE → **your AWS account ID**

INSERT_ROLE_NAME_HERE → **IAM role name for Lambda**

INSERT_LAMBDA_CODE_BUCKET_HERE → **S3 bucket containing lambda_function.zip**

INSERT_OPTIONAL_CONFIG_BUCKET_HERE → **optional S3 bucket for config
**
## Testing

Invoke Lambda manually via AWS Console or CLI:
```json
aws lambda invoke \
  --function-name SESTestEmailLambda \
  response.json
```

Check response.json for success or error message.

### Notes

-do-not-reply@YOUR_VERIFIED_DOMAIN.com can be replaced with any SES verified email.\
-Ensure Lambda IAM role has permission: ses:SendEmail.\
-Multiple recipients can be added in TO_EMAILS.\
