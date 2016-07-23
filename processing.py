import hashlib
import random

class Slide(object):
  def __init__(self, typ, theme, content):
    self.type = typ
    self.theme = theme
    self.content = content

def str_hash(s):
  return int(hashlib.md5(s).hexdigest()[:8], 16)

def select_fancy_word(words):
  return max(words,key=lambda w: len(w))

class Processor(object):
  def __init__(self):
    self.cur_loc = 0
  def process(self, parts):
    whole_text = u"".join(parts)
    words = whole_text.split(" ")

    slide = words[self.cur_loc:]
    prev_words = words[:self.cur_loc]
    h = str_hash(u" ".join(prev_words))
    random.seed(h)

    move_to_next = False
    slide_type = None
    content = u" ".join(slide)
    theme = random.randint(0,1)

    # ============ Da Rules

    if random.random() < 0.5: # Heading
      slide_type = "Heading"
      max_words = 6
      if random.random() < 1.0:
        content = select_fancy_word(slide)
        max_words = 10
      if len(slide) > max_words:
        move_to_next = True
    else:
      slide_type = "Bullets"

      bullets = []
      cur_word = 0
      for i in xrange(3):
        if cur_word >= len(slide):
          break
        n = random.randint(4,7)
        bullet = slide[cur_word:(cur_word+n)]
        cur_word += n
        bullets.append(u" ".join(bullet))
      if len(slide) > cur_word:
        move_to_next = True
      content = bullets

    # ==== Final stuff
    if move_to_next:
      print("Moving on to next slide")
      self.cur_loc = len(words)

    structure = Slide(slide_type, theme, content)
    print([self.cur_loc, slide])
    print([slide_type, theme, content])
    return structure


