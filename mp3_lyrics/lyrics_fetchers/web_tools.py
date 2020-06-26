import requests

def get_webpage(url):
    try:
        response = requests.get(url)
        html_doc = response.text
        return html_doc
    except Exception as e:
        print("Error: ", e)
        return e
