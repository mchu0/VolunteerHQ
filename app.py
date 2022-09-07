import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv
import modal_blocks
from slack_sdk import WebClient

load_dotenv()

SLACK_BOT_TOKEN = os.getenv('SLACK_BOT_TOKEN')
SLACK_APP_TOKEN = os.getenv('SLACK_APP_TOKEN')

current_app_home_blocks = None

# Initializes your app with your bot token and socket mode handler
app = App(token=SLACK_BOT_TOKEN)
client = WebClient(token=SLACK_BOT_TOKEN)


@app.event("message")
def handle_message_events(body, logger):
    logger.info(body)


@app.command("/volunteerhq")
def open_tenant_request_form_command(ack, body, client):
    user_id = body["user_id"]
    ack()
    client.views_open(
        trigger_id=body["trigger_id"],
        view=modal_blocks.get_volunteer_preferences_form(user_id)
    )



@app.shortcut("open_volunteer_preferences_form")
def open_tenant_request_form_shortcut(ack, shortcut, client):
    user_id = shortcut["user"]["id"]
    ack()
    client.views_open(
        trigger_id=shortcut["trigger_id"],
        view=modal_blocks.get_volunteer_preferences_form(user_id)
    )


@app.view("request_form")
def handle_view_events(ack, body, logger):
    ack()
    user_id = body["user"]["id"]
    values = body["view"]["state"]["values"]
    office_preference = values["office_preference"]["static_select-action"]["selected_option"]["value"]
    volunter_activity = values["volunter_activity"]["static_select-action"]["selected_option"]["value"]
    vto_location = values["vto_location"]["static_select-action"]["selected_option"]["value"]
    scheduling_preferences = values["scheduling_preferences"]["static_select-action"]["selected_option"]["value"]
    volunteer_causes = values["volunteer_causes"]["static_select-action"]["selected_option"]["value"]
    skills = values["skills"]["static_select-action"]["selected_option"]["value"]
    sdg_list = [sdg["value"] for sdg in values["sdg"]
                ["multi_static_select-action"]["selected_options"]]
    alert_time_preference = values["alert_time_preference"]["static_select-action"]["selected_option"]["value"]

    publish_preference_in_home(user_id, office_preference, volunter_activity, vto_location,
                               scheduling_preferences, volunteer_causes, skills, sdg_list, alert_time_preference)
    send_volunteer_alerts(user_id)


@app.action("sign_up")
def handle_sign_up(ack, body, logger):
    ack()
    client.chat_postMessage(
        token=SLACK_BOT_TOKEN,
        channel=body["user"]["id"],
        blocks=modal_blocks.get_vto_signed_up(),
        text="VTO Event Registered!"
    )
    
    post_vto_in_home(body["user"]["id"])
    invite_user_to_vto()

@app.view("submitted_event")
def handle_share_event(ack, body, logger):
    ack()
    new_msg = modal_blocks.get_share_msg("Hey team, I just signed up for this VTO event. Come join me!")
    client.chat_postMessage(
        token=SLACK_BOT_TOKEN,
        channel="C03UTKAC0HX",
        blocks=new_msg,
        text="New Volunteer Events!"
    )

    
@app.action("share_event")
def handle_share_event(ack, body, logger):
    ack()
    client.views_open(
        trigger_id=body["trigger_id"],
        view=modal_blocks.get_share_msg_modal()
    )
    
@app.action("share_event_submitted")
def handle_share_event(ack, body, logger):
    ack()
    client.views_open(
        trigger_id=body["trigger_id"],
        view=modal_blocks.get_msg_modal()
    )
    

def send_volunteer_alerts(user_id):
    response = client.chat_postMessage(
        token=SLACK_BOT_TOKEN,
        channel=user_id,
        blocks=modal_blocks.get_vto_alerts(user_id),
        text="New Volunteer Events!"
    )


def publish_preference_in_home(user_id, office_preference, volunter_activity, vto_location, scheduling_preferences, volunteer_causes, skills, sdg_list, alert_time_preference):
    global current_app_home_blocks
    current_app_home_blocks = modal_blocks.get_copy_of_responses(user_id, office_preference, volunter_activity, vto_location,
                                                scheduling_preferences, volunteer_causes, skills, sdg_list, alert_time_preference)
    response = client.views_publish(
        token=SLACK_BOT_TOKEN,
        user_id=user_id,
        view=current_app_home_blocks,
        text="Preferences!"
    )


def invite_user_to_vto():
    client.conversations_invite(
        token=SLACK_BOT_TOKEN,
        channel="C0405ALGHKK",
        users="U03SE79DR4Z",
    )

def post_vto_in_home(user_id: str):
    global current_app_home_blocks
    current_app_home_blocks["blocks"].extend(modal_blocks.get_vto_event_home())
    client.views_publish(
        token=SLACK_BOT_TOKEN,
        user_id=user_id,
        view=current_app_home_blocks,
        text="Updating VTO events!"
    )

# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, SLACK_APP_TOKEN).start()
