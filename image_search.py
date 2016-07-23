import requests
import threading
import os
import cStringIO
import pygame

REQUESTS = {}
URL_BASE = 'https://api.cognitive.microsoft.com/bing/v5.0/images/search?q={query}&count={count}'
BING_API_KEY = os.environ.get('BING_API_KEY')

MAX_WIDTH = 600
MAX_HEIGHT = 450

def search_image(term):
    global REQUESTS
    r = requests.post(
        URL_BASE.format(query=term, count=3),
        headers={
            'Ocp-Apim-Subscription-Key': BING_API_KEY
        }
    ).json()
    results = r['value']
    img_data = None
    for result in results:
        try:
            img_data = requests.get(result['contentUrl']).content
            break
        except e:
            continue
    if img_data is not None:
        image = pygame.image.load(cStringIO.StringIO(img_data))
        # Resize Image
        ow, oh = image.get_size()
        if ((MAX_WIDTH / MAX_HEIGHT) * ow) > oh:
            image = pygame.transform.smoothscale(image, (MAX_WIDTH, int(MAX_HEIGHT*(oh * 1.0 / ow))))
        else:
            image = pygame.transform.smoothscale(image, (int(MAX_HEIGHT * (ow * 1.0/ oh)), MAX_WIDTH))
        REQUESTS[term] = image

def get_image(search_term):
    global REQUESTS
    if search_term not in REQUESTS:
        REQUESTS[search_term] = None
        thread = threading.Thread(target=search_image, args=(search_term,))
        thread.daemon = True
        thread.start()
    else:
        return REQUESTS[search_term]

if __name__ == 'main':
    while True:
        img = get_image('Foobar')
        if img is not None:
            print(img)
