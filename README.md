# LastSecondSlides
Use the Google speech-to-text API to generate presentation slides as you talk! A collaboration with [Marc Mailhot](http://mlht.ca/).
Marc wrote the slide renderers and Bing Search with PyGame, and I wrote the Google Voice API interfacing code and the code to process the speech, decide on slide content and tie together the modules. Made for [TerribleHack IV](http://terriblehack.website/), a hackathon for intentionally funny and stupid projects.

Includes two themes: 90s and corporate, as well as three slide types: heading, bullet points, and picture.

It can use Bing image search to find images based on what you say.

**Note:** This was a fun 5-hour project for a fun hackathon, it stops working and crashes often due to multithreading issues we didn't bother to debug and isn't actually useful.

## Demo Video

See here:

<https://www.youtube.com/watch?v=chgOZumnXQo>

The voice recognition quality in the video is rather bad because it was a noisy room and I was using a crappy microphone.

## Getting it running

1. Set up a virtualenv if you want and know what that is.
1. Install portaudio for pyAudio
1. Install the dependencies of pygame, mostly SDL and related packages, see the pygame website for this.
1. `pip install -r requirements.txt`
1. Set yourself up with a Google Cloud Speech API account and a Bing Image Search API key
1. `export GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/credentials-key.json`
1. `export BING_API_KEY=yourkeygoeshere`
1. `python main.py`
1. Start saying things!

## Screenshots

![screenshot](http://imgur.com/BEwcZr5.png)
![screenshot](http://imgur.com/fTOdIte.png)
![screenshot](http://imgur.com/pBlBuJa.png)
![screenshot](http://imgur.com/C1G2aEV.png)
![screenshot](http://imgur.com/8wAQUS6.png)
![screenshot](http://imgur.com/XBYpi3B.png)
