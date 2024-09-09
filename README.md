# simplest-tts
A TTS service using an AWS Polly voice.

## Setup
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## AWS Credentials
You need to have an [AWS account](https://us-east-1.console.aws.amazon.com/iam/home?region=us-east-1#/users$new?step=details) and create an access key for the AWS Polly service.
Create a credentials file at `~/.aws/credentials` with the following content:
```
[default]
aws_access_key_id = YOUR_ACCESS_KEY_ID
aws_secret_access_key = YOUR_SECRET_ACCESS_KEY
```

## Running the service
Once the virtual environment is activated, run the service:
```
python3 polly-tts-cli.py
```


You can also specify the AWS region and voice ID using command-line options:
```
python3 polly-tts-cli.py --region us-east-1 --voice Joanna
```


Available options:
- `--region`: Specify the AWS region (default: us-west-2)
- `--voice`: Specify the Polly voice ID (default: Nicole)

If you don't provide these options, the service will use the default values.

The service will be expecting text as input, until you press `Ctrl+C` to terminate the service.

## License
This project is licensed under the GNU General Public License v3.0. See the LICENSE file for details.