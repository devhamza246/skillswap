from datetime import timezone
import requests
import base64
from conf.settings import ZOOM_ACCOUNT_ID, ZOOM_CLIENT_ID, ZOOM_SECRET_KEY
from .models import ZoomAccessToken

account_id = ZOOM_ACCOUNT_ID
client_id = ZOOM_CLIENT_ID
client_secret = ZOOM_SECRET_KEY

combined_string = f"{client_id}:{client_secret}"

# Base64 encode the combined string
base64_encoded_token = base64.b64encode(combined_string.encode("utf-8")).decode("utf-8")


def get_access_token():
    url = f"https://zoom.us/oauth/token?grant_type=account_credentials&account_id={account_id}"
    response = requests.post(
        url, headers={"Authorization": f"Basic {base64_encoded_token}"}
    )
    if response.status_code == 200:
        access_token = response.json().get("access_token")
        zoom_access_token_obj = ZoomAccessToken.objects.create(
            access_token=access_token
        )
        return zoom_access_token_obj.access_token
    else:
        return None


def create_meeting(start_time, meeting_invitee):
    invitees_list = []
    if meeting_invitee:
        invitees_list.append({"email": meeting_invitee})
    body = {
        "agenda": "My Meeting",
        "default_password": False,
        "duration": 60,
        "password": "123456",
        "pre_schedule": False,
        "settings": {
            "allow_multiple_devices": True,
            "approval_type": 2,
            "audio": "telephony",
            "audio_conference_info": "test",
            "focus_mode": True,
            "host_video": True,
            "jbh_time": 10,
            "join_before_host": False,
            "meeting_invitees": invitees_list,
            "participant_video": False,
            "private_meeting": False,
            "registrants_confirmation_email": True,
            "registrants_email_notification": True,
            "registration_type": 1,
            "watermark": False,
            "continuous_meeting_chat": {
                "enable": True,
                "auto_add_invited_external_users": True,
            },
            "push_change_to_calendar": False,
            "resources": [
                {
                    "resource_type": "whiteboard",
                    "resource_id": "X4Hy02w3QUOdskKofgb9Jg",
                    "permission_level": "editor",
                }
            ],
        },
        "start_time": start_time.strftime("%Y-%m-%dT%H:%M:%S"),
        "template_id": "Dv4YdINdTk+Z5RToadh5ug==",
        "timezone": "UTC",
        "topic": "My Meeting",
        "type": 2,
    }
    access_token = ZoomAccessToken.objects.all().first()
    if access_token and access_token.created > (
        timezone.now() - timezone.timedelta(minutes=60)
    ):
        access_token = access_token
    else:
        access_token = get_access_token()

    headers = {
        "Authorization": f"Bearer {access_token}",
    }
    response = requests.post(
        "https://api.zoom.us/v2/users/me/meetings", headers=headers, json=body
    )

    if response.status_code == 201:
        meeting_link = response.json()["start_url"]
        return meeting_link
    else:
        return None
