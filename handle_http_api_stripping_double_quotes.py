import json

def lambda_handler(event, context):
    #replicates HTTP API stripping double quotes
    input1_headers = {
    'cookie': 'csrftoken=WvWLrENu05ETxo8ywkCOb9b8xxxxasdasdasd123242423423424; sessionid=35lg1231231dsktufyb8ulkhje0hn4uqc7m7; messages=60fd922b12313131231231231312adsasdcb$[[\"__json_message\"\0540\05430\054\"Items must be selected in order to perform actions on them. No items have been changed.\"]]',
    }
    
    #replicates REST API cookie payload
    input2_headers = {
    'cookie': 'csrftoken=WvWLrENu05ETxo8ywkCOb9b8xxxxasdasdasd123242423423424; sessionid=35lg1231231dsktufyb8ulkhje0hn4uqc7m7; messages="60fd922b12313131231231231312adsasdcb$[[\"__json_message\"\0540\05430\054\"Items must be selected in order to perform actions on them. No items have been changed.\"]]"',
    }

    #change input1_headers with input2_headers to observe cookie handling
    cookie_components = input1_headers['cookie'].split('; ')
    
    messages_value = None
    
    for component in cookie_components:
        key, value = component.split('=', 1)
        if key == 'messages':
            messages_value = value
            break
    
    #----Check if 'messages' value was found
    if messages_value:
        #if messages_value starts and ends with double quotes, then do nothing
        if messages_value.startswith('"') and messages_value.endswith('"'):
            print('message value already starts with doble quotes ""')
        else:
            #else, if messages_value does not start and end with double quotes "", then add them to start and end
            messages_value = f'"{messages_value}"'
            print(messages_value)
    else:
        print("No 'messages' found in the input headers.")
    
    
    return {
            'statusCode': 200,
            'body': json.dumps('Hello from Lambda!')
        }
