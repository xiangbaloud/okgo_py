#!/usr/bin/python

import random

class Dise(object):
  def __init__(self, sides):
    self.sides = sides
  def roll(self):
    return random.randint(1, self.sides)

d = Dise(6)
d1 = Dise(6)
print d.roll(), d1.roll()
