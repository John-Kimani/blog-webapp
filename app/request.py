import urllib.request,json
from app.models import Quote


def get_random_qoutes():
    '''
    Function that consume random quote api
    '''
    get_quote_url = 'http://quotes.stormconsultancy.co.uk/random.json'
    get_quote_data = urllib.request.urlopen(get_quote_url)
    quote_response = json.loads(get_quote_data.read())
    random_quote = None

    if quote_response:
        '''
        condition that set requested data
        '''
        quote_message = quote_response.get('quote')
        author = quote_response.get('author')
    random_quote = Quote(author, quote_message)
    return random_quote