import requests
import sys
import os

# replicated from https://blog.ruanbekker.com/blog/2020/11/06/sending-slack-messages-with-python/

# webhook:
# https://hooks.slack.com/services/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

SLACK_WEBHOOK_URL = 'https://hooks.slack.com/services/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'
SLACK_CHANNEL = "#dev_sec_ops"
ALERT_STATE = sys.argv[1]

alert_map = {
    # "emoji": {
    #     "up": ":white_check_mark:",
    #     "down": ":fire:"
    # },
    "text": {
        "up": "RESOLVED",
        "down": "FIRING"
    },
    # "message": {
    #     "up": "Everything is good!",
    #     "down": "Stuff is burning!"
    # },
    "color": {
        "up": "#32a852",
        "down": "#ad1721"
    }
}


def alert_to_slack(status):
    data = {
        "text": "Jenkins_Notifications",
        "username": "Jenkins",
        "channel": SLACK_CHANNEL,
        "attachments": [
        {
            "text": "test",
            "color": alert_map["color"][status],
            "attachment_type": "default",
            # "actions": [
            #     {
            #         "name": "Logs",
            #         "text": "Logs",
            #         "type": "button",
            #         "style": "primary",
            #         "url": log_url
            #     },
            #     {
            #         "name": "Metrics",
            #         "text": "Metrics",
            #         "type": "button",
            #         "style": "primary",
            #         "url": metric_url
            #     }
            # ]
        }]
    }
    r = requests.post(SLACK_WEBHOOK_URL, json=data)
    return r.status_code

alert_to_slack(ALERT_STATE)