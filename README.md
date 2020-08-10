# gather-login-notifier

## How to use

1. Please set the environment variables

```
export SLACK_WEBHOOK_URL="https://your.slack.webhook.url"
export GATHER_SPACE_URL="https://your.gather.space.url"
```

2. Set a job to execute the script

```
# for crontab
00 * * * * python app.py
```
