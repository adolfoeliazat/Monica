import requests
from templates.generic import GenericTemplate
from templates.text import TextTemplate
import sys,os


def process(action,parameter):
    output ={}
    try:
        url = 'https://api.chucknorris.io/jokes/random'
        r = requests.get(url)
        joke = r.json()['value']
        template = GenericTemplate()
        template.add_element(title=joke,buttons=[
            {
                "type": "postback",
                "title": "One more!",
                "payload": "more!joke"
            },
        ])
        output['action'] = action
        output['success'] = True
        output['output'] = template.get_message()
    except Exception as E:
        print E
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print exc_type, fname, exc_tb.tb_lineno
        error_message = 'I couldn\'t find any Joke '
        error_message += '\nPlease ask me something else, like:'
        error_message += '\n  - Tell me a Joke'
        error_message += '\n  - I\'m bored'
        error_message += '\n  - You are boring'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output

if __name__ == '__main__':
    print process('joke','parameter')