import speech
import drawing
from threading import Thread
import processing
import time

to_render = [processing.Slide("Heading",1,"LastSecondSlides"),False]
t1 = Thread(target=speech.main, args=(to_render,))
# t1.daemon = True
t1.start()
# time.sleep(3.0)
drawing.main(to_render)
to_render[1] = True # Quit signal
# t2.join()
