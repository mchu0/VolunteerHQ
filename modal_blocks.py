def get_volunteer_preferences_form(user_id: str):
    sdg_options = ["No Poverty", "Zero Hunger", "Good Health and Well-Being", "Quality Education", "Gender Equality", "Clean Water and Sanitation", "Affordable and Clean Energy", "Decent Work and Economic Growth",
                   "Industry, Innovation and Infrastructure", "Reduced Inequalities", "Sustainable Cities and Communities", " Responsible Consumption and Production", "Climate Action", "Life Below Water"]
    sdg_options_list = []
    for option in sdg_options:
        sdg_options_list.append(
            {
                "text": {
                    "type": "plain_text",
                    "text": option,
                    "emoji": True
                },
                "value": option
            })

    office_options = ["Amsterdam, Netherlands - Gustav Mahlerlaan 2970 (The Edge)", "Atlanta, Georgia, USA - Salesforce Tower Atlanta", "Auckland, New Zealand - 188 Quay St", "Austin, Texas, USA - 600 Congress Ave.", "Bangalore, India - Torrey Pines EG", "Bangalore, India - Umiya Business Bay Tower 1", "Bangkok, Thailand - T-One Building", "Barcelona, Spain - Can Rabia 3-5", "Bellevue, Washington, USA - 929 108th Ave NE", "Berlin, Germany - Kurfurstendamm 194", "Boston, Massachusetts, USA - 500 Boylston Street", "Brisbane, Australia - Waterfront Place", "Brussels, - Cantersteen 47", "Buenos Aires, Argentina - Juana Manso 999",
                      "Burlington, Massachusetts, USA - 5 Wall St", "Cambridge, Massachusetts, USA - 955 Massachusetts Avenue", "Canberra, Australia - 10 Bourke St", "Carlton, Australia - 551 Swanston Street", "Casablanca, Morocco - Blvd Sidi Mohamed Ben Abdellah", "Charlotte, North Carolina, USA - 5200 77 Center Dr", "Chicago, Illinois, USA - 111 West Illinois St", "Dallas, Texas, USA - 2300 N Field St", "Deerfield Beach, Florida, USA - 1166 West Newport Center Dr", "Denver, - 1681 Chestnut Street", "Denver, Colorado, USA - 17th Street Plaza", "Dublin, Ireland - 78 Sir John Rogerson's Quay", "Dublin, Ireland - Sandyford Business Park (The Atrium)", "Dublin, Ireland - The Oval Building", "Dusseldorf, Germany - Elisabethstrasse 11", "Espoo, Finland - Keilaranta 1", "Frankfurt, Germany - 30 Ulmenstrasse", "Fukuoka, Japan - 8-1 Hakataekichuogai (JR JP Hakata)", "Geneva, - Pont Rouge IWGGeneva, - Pont Rouge IWG", "Grenoble, France - 29 Blvd des Alpes", "Gurgaon, India - DLF Building No.8", "Gurgaon, India - One Horizon Center", "Halifax, Nova Scotia, Canada - 1505 Barrington St", "Hellerup, Denmark - Strandvejen 125", "Hillsboro, Oregon, USA - 2035 NE Cornelius Pass", "Hiroshima, Japan - Inari Ohashi Centre", "Hong Kong, Hong Kong - 39 Queens Road Central", "Hyderabad, India - Divyasree Orion Block 4", "Irvine, California, USA - 200 Spectrum Center", "Jena, Germany - Leutragraben 2-4", "Kirkland, Washington, USA - Kirkland Urban North", "Knoxville, Tennessee, USA - 2095 Lakeside Centre", "Lisbon, - Torres de Lisboa", "London, United Kingdom - Blue Fin", "London, United Kingdom - Salesforce Tower London", "Lyon, France - Le Grand Hotel-Dieu", "Madrid, Spain - Paseo de la Castellana 79", "Manchester, United Kingdom - 1 St. Peter`s Square", "Mclean, Virginia, USA - 8280 Greensboro Drive", "Melbourne, Australia - 277 William Street", "Melbourne, Australia - 55 Collins St", "Mexico City, Mexico, Mexico - Montes Urales 424", "Milan, Italy - Corso Europa 15", "Morges, Switzerland - Lake Geneva Center Building A", "Mumbai, India - 701 Plot No C70 BG Block", "Munich, Germany - 31-37 Erika-mann-Strasse (Kontorhaus)", "Nagoya, Japan - Lucent Tower Level 40", "Nantes, France - 30 Boulevard Vincent Gache", "NYC, New York, USA - Salesforce Tower New York", "Osaka, Japan - 1-1 Ofukacho Kita-Ku", "Palo Alto, California, USA - 181 Lytton Ave", "San Francisco, California, USA - 500 Howard Street", "San Francisco, California, USA - Salesforce East", "San Francisco, California, USA - Salesforce Tower San Francisco", "San Francisco, California, USA - Salesforce West", "Seattle, Washington, USA - NorthEdge", "Singapore, Singapore - 5 Temasek Blvd", "Tokyo, Japan - 1-1-1 Otemachi", "Vienna, - Wiedner Gurtel 13", "Zurich, Switzerland - Ernst-Nobs-Platz 1"]

    office_options_list = []
    for option in office_options:
        office_options_list.append({
            "text": {
                "type": "plain_text",
                "text": option,
                "emoji": True
            },
            "value": option
        },)

    volunter_activities_options = [
        "Volunteer Event", "Donation Opportunity", "Pro Bono Event"]
    volunter_activities_list = []
    for volunter_activity in volunter_activities_options:
        volunter_activities_list.append({
            "text": {
                "type": "plain_text",
                "text": volunter_activity,
                "emoji": True
            },
            "value": volunter_activity
        },)

    vto_location_options = ["In-person VTO",
                            "Virtual VTO", "Hybrid VTO", "Any"]
    vto_location_list = []
    for vto_location in vto_location_options:
        vto_location_list.append({
            "text": {
                "type": "plain_text",
                "text": vto_location,
                "emoji": True
            },
            "value": vto_location
        },)

    frequency_options = ["Weekly", "Biweekly", "Monthly"]
    frequency_list = []
    for frequency in frequency_options:
        frequency_list.append({
            "text": {
                "type": "plain_text",
                "text": frequency,
                "emoji": True
            },
            "value": frequency
        },)

    scheduling_options = ["Morning", "Afternoon", "Evening", "No Preference"]
    scheduling_list = []
    for scheduling in scheduling_options:
        scheduling_list.append({
            "text": {
                "type": "plain_text",
                "text": scheduling,
                "emoji": True
            },
            "value": scheduling
        },)

    volunteer_cause_options = ["Arts, Culture & Humanities", "Animal Welfare", "Education", "Environment", "Health", "Human Services",
                               "International & Foreign Affairs", "Mutual & Membership Benefit", "Public & Societal Benefit", "Religion Related", "Workforce Development", "Surprise"]
    volunteer_cause_list = []
    for volunteer_cause in volunteer_cause_options:
        volunteer_cause_list.append({
            "text": {
                "type": "plain_text",
                "text": volunteer_cause,
                "emoji": True
            },
            "value": volunteer_cause
        },)

    skills_options = ["Customer Service", "Design Thinking and Innovation", "Finance", "Human Resources", "Legal",
                      "Marketing & Communications", "Operations", "Project Management", "Sales", "Strategy", "Technology/Data Management"]
    skills_list = []
    for skill in skills_options:
        skills_list.append({
            "text": {
                "type": "plain_text",
                "text": skill,
                "emoji": True
            },
            "value": skill
        },)

    volunteer_preferences_form = {
        "type": "modal",
        "callback_id": "request_form",
        "submit": {
            "type": "plain_text",
            "text": "Submit",
                "emoji": True
        },
        "close": {
            "type": "plain_text",
            "text": "Cancel",
            "emoji": True
        },
        "title": {
            "type": "plain_text",
            "text": "Volunteering Preferences",
            "emoji": True
        },
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Hey <@" + user_id + "> !\n\nWe'd love to hear your preferences to alert the proper volunteer events for you!",
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "input",
                "block_id": "office_preference",
                        "element": {
                            "type": "static_select",
                            "placeholder": {
                                    "type": "plain_text",
                                "text": "Select an item",
                                        "emoji": True
                            },
                            "options": office_options_list,
                            "action_id": "static_select-action"
                        },
                "label": {
                            "type": "plain_text",
                            "text": "Which office are you based in?",
                            "emoji": True
                        }
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": "We'll use this office location to recommend volunteering activities near you. "
                    }
                ]
            },
            {
                "type": "input",
                "block_id": "volunter_activity",
                        "element": {
                            "type": "static_select",
                            "placeholder": {
                                    "type": "plain_text",
                                "text": "Select an item",
                                        "emoji": True
                            },
                            "options": volunter_activities_list,
                            "action_id": "static_select-action"
                        },
                "label": {
                            "type": "plain_text",
                            "text": "What type of volunter activities are you interested in?",
                            "emoji": True
                        }
            },
            {
                "type": "input",
                "block_id": "vto_location",
                        "element": {
                            "type": "static_select",
                            "placeholder": {
                                    "type": "plain_text",
                                "text": "Select an item",
                                        "emoji": True
                            },
                            "options": vto_location_list,
                            "action_id": "static_select-action"
                        },
                "label": {
                            "type": "plain_text",
                            "text": "What type of VTO event are you interested in?",
                            "emoji": True
                        }
            },
            {
                "type": "input",
                "block_id": "scheduling_preferences",
                        "element": {
                            "type": "static_select",
                            "placeholder": {
                                    "type": "plain_text",
                                "text": "Select an item",
                                        "emoji": True
                            },
                            "options": scheduling_list,
                            "action_id": "static_select-action"
                        },
                "label": {
                            "type": "plain_text",
                            "text": "When would you like to attend VTO events?",
                            "emoji": True
                        }
            },
            {
                "type": "input",
                "block_id": "volunteer_causes",
                        "element": {
                            "type": "static_select",
                            "placeholder": {
                                    "type": "plain_text",
                                "text": "Select an item",
                                        "emoji": True
                            },
                            "options": volunteer_cause_list,
                            "action_id": "static_select-action"
                        },
                "label": {
                            "type": "plain_text",
                            "text": "Types of Volunteer Causes",
                            "emoji": True
                        }
            },
            {
                "type": "input",
                "block_id": "skills",
                        "element": {
                            "type": "static_select",
                            "placeholder": {
                                    "type": "plain_text",
                                "text": "Select an item",
                                        "emoji": True
                            },
                            "options": skills_list,
                            "action_id": "static_select-action"
                        },
                "label": {
                            "type": "plain_text",
                            "text": "Skills (for help with Pro Bono work)",
                            "emoji": True
                        }
            },
            {
                "type": "input",
                "block_id": "sdg",
                "element": {
                    "type": "multi_static_select",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Select options",
                        "emoji": True
                    },
                    "options": sdg_options_list,
                    "action_id": "multi_static_select-action"
                },
                "label": {
                    "type": "plain_text",
                    "text": "Preferred Sustainable Development Goals",
                    "emoji": True
                }
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": "Take the Accelerate the Sustainable Development Goals (SDGs) Trail or go to <https://www.globalgoals.org/|https://www.globalgoals.org/> to learn about the SDGs."
                    }
                ]
            },
            {
                "type": "input",
                "block_id": "alert_time_preference",
                        "element": {
                            "type": "static_select",
                            "placeholder": {
                                    "type": "plain_text",
                                "text": "Select an item",
                                        "emoji": True
                            },
                            "options": [
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": "Anytime",
                                        "emoji": True
                                    },
                                    "value": "Anytime"
                                },
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": "Morning",
                                        "emoji": True
                                    },
                                    "value": "Morning"
                                },
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": "Afternoon",
                                        "emoji": True
                                    },
                                    "value": "Afternoon"
                                }
                            ],
                            "action_id": "static_select-action"
                        },
                "label": {
                            "type": "plain_text",
                            "text": "When would you like to receive alerts?",
                            "emoji": True
                        }
            }
        ]
    }
    return volunteer_preferences_form


def get_vto_alerts(user_id: str):
    events = [
        {
            "url": "https://powerofus.force.com/vfx/s/volunteer-activity/a1D7y00000024xBEAQ/swn-real-talk-acommunity-support-series?tabset-3b46d=f7647",
            "title": "SWN Real Talk Community Support Series",
            "shift_date": "Aug 23, 2022",
            "shift_time_range": "1pm-2pm",
            "shift_duration": "0.5",
            "description": "Prepared content , prepped presentation and presented to a group of 35 audiences of Industries Cloud WIT",
            "sdg_impact_area": "Gender Equality",
            "city": "any city",
            "img_url": "https://api.slack.com/img/blocks/bkb_template_images/Streamline-Beach.png"
        },
        {
            "url": "https://powerofus.force.com/vfx/s/volunteer-activity/a1D1E00000FKcy4UAD/sales-cloud-pm-x-zooniverse-monthly-vto-activity",
            "title": "Sales Cloud PM x Zooniverse Monthly VTO Activity",
            "shift_date": "Aug 30, 2022",
            "shift_type": "In Person and Virtual",
            "shift_time_range": "8:30am-10am",
            "shift_duration": "1.5",
            "description": "For the VTO, we will be pinning penguins based on the photo provided for Zooniverse.",
            "sdg_impact_area": "15: Life On Land",
            "city": "San Francisco",
            "img_url": "https://api.slack.com/img/blocks/bkb_template_images/tripAgent_1.png"
        },
        {
            "url": "https://powerofus.force.com/vfx/s/volunteer-activity/a1D7y000000JxnaEAC/meals-on-wheels-cards-for-seniors-muley-day-vto",
            "title": "Meals on Wheels Cards for Seniors - Muley Day VTO",
            "shift_date": "9/1/2022",
            "shift_type": "In Person",
            "shift_time_range": "12:00pm-1:00pm",
            "shift_duration": "1",
            "description": "Join us in the San Francisco Tower on 9/1/22 for an in-office Muley Day & Servicetrace acquisition anniversary celebration! Along with some sweet treats and a sizzle real over lunch, in-office VTO will be offered for Meals on Wheels San Francisco.",
            "sdg_impact_area": "Good Health and Well-Being",
            "city": "San Francisco",
            "img_url": "https://api.slack.com/img/blocks/bkb_template_images/tripAgent_3.png"
        },
    ]
    event_blocks_list = []
    for e in events:
        block_list = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*<" + e["url"] + "|"+e["title"] + ">*\n" + e["description"] + "\n" + e["shift_date"] + " - " + e["shift_time_range"] + " " + e["shift_duration"] + " hour(s)"
                },
                "accessory": {
                    "type": "image",
                            "image_url": e["img_url"],
                    "alt_text": "Windsor Court Hotel thumbnail"
                }
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "plain_text",
                                "text": "SDG Impact Area: " + e["sdg_impact_area"]
                    },

                    {
                        "type": "plain_text",
                                "text": "City: " + e["city"]
                    }
                ]
            },
            {
			"type": "input",
			"element": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select options",
					"emoji": True
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "1:00pm-1:30pm",
							"emoji": True
						},
						"value": "value-0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "1:30pm-2:00pm",
							"emoji": True
						},
						"value": "value-1"
					}
				],
				"action_id": "static_select-action"
			},
			"label": {
				"type": "plain_text",
				"text": "Choose a shift",
				"emoji": True
			}
		},
            {
                "type": "actions",
                        "elements": [
                            {
                                "type": "button",
                                "action_id": "sign_up",
                                "text": {
                                        "type": "plain_text",
                                        "emoji": True,
                                        "text": "Sign Up"
                                },
                                "style": "primary",
                                "value": "click_me_123"
                            },
                            {
                                "type": "button",
                                "action_id": "share_event",
                                "text": {
                                        "type": "plain_text",
                                        "emoji": True,
                                        "text": "Share"
                                },
                                "value": "click_me_123"
                            },
                             {
                                "type": "button",
                                "text": {
                                        "type": "plain_text",
                                        "emoji": True,
                                        "text": "Donate to the Cause"
                                },
                                "value": "click_me_123"
                            },
                            {
                                "type": "button",
                                "text": {
                                        "type": "plain_text",
                                        "emoji": True,
                                        "text": "Register Interest"
                                },
                                "value": "click_me_123"
                            }
                        ]
            },
            {
                "type": "divider"
            },
        ]

        event_blocks_list.extend(block_list)

    app_home_alerts = [
        {
            "type": "section",
            "text": {
                    "type": "plain_text",
                    "text": ":tada: NEW VOLUNTEER EVENTS NEAR YOU! :tada:",
            }
        },
        {
            "type": "divider"
        },
    ]

    app_home_alerts.extend(event_blocks_list)
    return app_home_alerts


def get_copy_of_responses(user_id, office_preference, volunter_activity, vto_location, scheduling_preferences, volunteer_causes, skills, sdg_list, alert_time_preferences):
    blocks_array = {
        "type": "home",
        "blocks": [
                {
                    "type": "header",
                    "text": {
                            "type": "plain_text",
                        "text": "Volunteer Alert Preferences:"
                    }
                },
            {
                    "type": "section",
                    "text": {
                            "type": "mrkdwn",
                        "text": "Hi! <@" + user_id + "> Welcome to your home page! You can edit your VTO Alert Preferences here!",
                    }

                    },
            {
                    "type": "actions",
                    "elements": [
                            {
                                "type": "button",
                                "text": {
                                        "type": "plain_text",
                                        "text": "Reset Preferences",
                                                "emoji": True
                                },
                                "value": "create_project"
                            },
                        {
                                "type": "button",
                                "text": {
                                        "type": "plain_text",
                                        "text": "Help",
                                                "emoji": True
                                },
                                "value": "help"
                                }
                    ]
                    },
            {
                    "type": "context",
                    "elements": [
                            {
                                "type": "image",
                                "image_url": "https://api.slack.com/img/blocks/bkb_template_images/placeholder.png",
                                "alt_text": "placeholder"
                            }
                    ]
                    },
            {
                    "type": "section",
                    "text": {
                            "type": "mrkdwn",
                        "text": "*Preferences*"
                    }
                    },
            {
                    "type": "divider"
                    },
            {
                    "type": "section",
                    "text": {
                            "type": "mrkdwn",
                        "text": ":office: *Office*\n" + office_preference
                    },
                    "accessory": {
                        "type": "button",
                        "text": {
                                "type": "plain_text",
                                "text": "Edit",
                                        "emoji": True
                        },
                        "value": "public-relations"
                    }
                    },
            {
                    "type": "divider"
                    },
            {
                    "type": "section",
                    "text": {
                            "type": "mrkdwn",
                        "text": ":goal_net: *Preferred Sustainable Development Goals*\n" + ", ".join(sdg_list)
                    },
                    "accessory": {
                        "type": "button",
                        "text": {
                                "type": "plain_text",
                                "text": "Edit",
                                        "emoji": True
                        },
                        "value": "public-relations"
                    }
                    },
            {
                    "type": "divider"
                    },
            {
                    "type": "section",
                    "text": {
                            "type": "mrkdwn",
                        "text": ":salesforce-alert: *Alert Time*\n" + alert_time_preferences
                    },
                    "accessory": {
                        "type": "button",
                        "text": {
                                "type": "plain_text",
                                "text": "Edit",
                                        "emoji": True
                        },
                        "value": "public-relations"
                    }
                    },
            {
                    "type": "divider"
                    },
            {
                    "type": "section",
                    "text": {
                            "type": "mrkdwn",
                        "text": ":farmer: *Volunteer Activity*\n" + volunter_activity
                    },
                    "accessory": {
                        "type": "button",
                        "text": {
                                "type": "plain_text",
                                "text": "Edit",
                                        "emoji": True
                        },
                        "value": "public-relations"
                    }
                    },
            {
                    "type": "divider"
                    },
            {
                    "type": "section",
                    "text": {
                            "type": "mrkdwn",
                        "text": ":computer: *VTO Location*\n" + vto_location
                    },
                    "accessory": {
                        "type": "button",
                        "text": {
                                "type": "plain_text",
                                "text": "Edit",
                                        "emoji": True
                        },
                        "value": "public-relations"
                    }
                    },
            {
                    "type": "divider"
                    },
            {
                    "type": "section",
                    "text": {
                            "type": "mrkdwn",
                        "text": ":calendar: *Schedule*\n" + scheduling_preferences
                    },
                    "accessory": {
                        "type": "button",
                        "text": {
                                "type": "plain_text",
                                "text": "Edit",
                                        "emoji": True
                        },
                        "value": "public-relations"
                    }
                    },
            {
                    "type": "divider"
                    },
            {
                    "type": "section",
                    "text": {
                            "type": "mrkdwn",
                        "text": ":salesforce-lead: *Volunteer Causes*\n" + volunteer_causes
                    },
                    "accessory": {
                        "type": "button",
                        "text": {
                                "type": "plain_text",
                                "text": "Edit",
                                        "emoji": True
                        },
                        "value": "public-relations"
                    }
                    },
            {
                    "type": "divider"
                    },
            {
                    "type": "section",
                    "text": {
                            "type": "mrkdwn",
                        "text": ":success21: *Skills*\n" + skills
                    },
                    "accessory": {
                        "type": "button",
                        "text": {
                                "type": "plain_text",
                                "text": "Edit",
                                        "emoji": True
                        },
                        "value": "public-relations"
                    }
                    },
            {
                    "type": "divider"
                    },
        ]
    }
    return blocks_array


def get_vto_signed_up():
    msg_blocks_arr = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": ":calendar: |   *VTO EVENT REGISTERED*  | :calendar: "
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Congrats! You've registered for a VTO event.\n Feel free to share the event with your friends and family! Thanks for making the world a better place :earth_spin:"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*<https://powerofus.force.com/vfx/s/volunteer-activity/a1D7y00000024xBEAQ/swn-real-talk-acommunity-support-series?tabset-3b46d=f7647|SWN Real Talk Community Support Series>* \n `08/23/2022 1:00pm-1:30pm 0.5 hour(s)`"
            },
            "accessory": {
                "type": "button",
                "action_id": "share_event",
                "text": {
                    "type": "plain_text",
                    "text": "Share",
                    "emoji": True
                }
            }
        }
    ]

    return msg_blocks_arr


def get_vto_event_home():
    blocks = [{
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":calendar: |   *UPCOMING VTO EVENT(S)*  | :calendar: "
        }
        },
        {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*<https://powerofus.force.com/vfx/s/volunteer-activity/a1D7y00000024xBEAQ/swn-real-talk-acommunity-support-series?tabset-3b46d=f7647|SWN Real Talk Community Support Series>* \n `08/23/2022 1:00pm-1:30pm 0.5 hour(s)`"
        },
        "accessory": {
            "type": "button",
            "text": {
                "type": "plain_text",
                "text": "Share",
            }
        }
    },
        {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":moneybag: |   *YOUR DONATION(S)*  | :moneybag: "
        }
        }]
    return blocks


def get_share_msg_modal():
    modal = {
	"type": "modal",
    'callback_id': 'submitted_event',
	"submit": {
		"type": "plain_text",
		"text": "Share",
		"emoji": True
	},
	"close": {
		"type": "plain_text",
		"text": "Cancel",
		"emoji": True
	},
	"title": {
		"type": "plain_text",
		"text": "Share VTO event",
		"emoji": True
	},
	"blocks": [
		{
			"type": "divider"
		},
  {
			"type": "input",
			"element": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Channels",
					"emoji": True
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "#general",
							"emoji": True
						},
						"value": "value-0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "#muley_slackers_slackathon",
							"emoji": True
						},
						"value": "value-1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "#random",
							"emoji": True
						},
						"value": "value-2"
					}
				],
				"action_id": "static_select-action"
			},
			"label": {
				"type": "plain_text",
				"text": "Select a channel to share VTO in:",
				"emoji": True
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": ":calendar: |   *VTO EVENT!*  | :calendar: "
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*<https://powerofus.force.com/vfx/s/volunteer-activity/a1D7y00000024xBEAQ/swn-real-talk-acommunity-support-series?tabset-3b46d=f7647|SWN Real Talk Community Support Series>*\n Prepared content , prepped presentation and presented to a group of 35 audiences of Industries Cloud WIT\n Aug 23, 2022 - 1:00pm-1:30pm 0.5 hour(s) "
			},
			"accessory": {
				"type": "image",
				"image_url": "https://api.slack.com/img/blocks/bkb_template_images/Streamline-Beach.png",
				"alt_text": "Windsor Court Hotel thumbnail"
			}
		},
		{
			"type": "context",
			"elements": [
				{
					"type": "plain_text",
					"text": "SDG Impact Area: Gender Equality"
				},
				{
					"type": "plain_text",
					"text": "City: any city"
				}
			]
		},
		{
			"type": "input",
			"block_id": "team_msg",
			"label": {
				"type": "plain_text",
				"text": "Attach a message?",
				"emoji": True
			},
			"element": {
				"type": "plain_text_input",
				"multiline": True
			},
			"optional": True
		}
	]
}
    return modal


def get_share_msg(text: str):
    blocks = [{
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": "Michelle has shared a VTO event - \"" + text + "\"",
				"emoji": True
			}
		},
        {
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": ":calendar: |   *VTO EVENT!*  | :calendar: "
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*<https://powerofus.force.com/vfx/s/volunteer-activity/a1D7y00000024xBEAQ/swn-real-talk-acommunity-support-series?tabset-3b46d=f7647|SWN Real Talk Community Support Series>*\n Prepared content , prepped presentation and presented to a group of 35 audiences of Industries Cloud WIT\n Aug 23, 2022 - 1:00pm-1:30pm 0.5 hour(s) "
			},
			"accessory": {
				"type": "image",
				"image_url": "https://api.slack.com/img/blocks/bkb_template_images/Streamline-Beach.png",
				"alt_text": "Windsor Court Hotel thumbnail"
			}
		},
		{
			"type": "context",
			"elements": [
				{
					"type": "plain_text",
					"text": "SDG Impact Area: Gender Equality"
				},
				{
					"type": "plain_text",
					"text": "City: any city"
				}
			]
		},
   {
                "type": "actions",
                        "elements": [
                            {
                                "type": "button",
                                "action_id": "sign_up",
                                "text": {
                                        "type": "plain_text",
                                        "emoji": True,
                                        "text": "Sign Up"
                                },
                                "style": "primary",
                                "value": "click_me_123"
                            },
                            {
                                "type": "button",
                                "action_id": "share_event",
                                "text": {
                                        "type": "plain_text",
                                        "emoji": True,
                                        "text": "Share"
                                },
                                "value": "click_me_123"
                            }
                        ]
            },
    ]
    return blocks