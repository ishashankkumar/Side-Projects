# A test file to test Consumer Producer Model with Python's ThreadPoolExecutor.

from concurrent.futures import ThreadPoolExecutor
from Queue import Queue


class ConsumerProducer(object):

  def __init__(self):
    self.q = Queue(maxsize=10)
    self.counter = 0

  def random_gem(self, dd):
    return self.q.put(dd)

  def playbook(self):
    with ThreadPoolExecutor(max_workers=5) as executor:
        for x in [i for i in range(100)]:
            executor.submit(self.random_gem(x))
            if self.q.full():
                executor.submit(self.empty_queue())

  def empty_queue(self):
      if not self.q.empty():
        self.q.get(block=False)


if __name__ == "__main__":
    t = ConsumerProducer()
    t.playbook()
    print list(t.q.queue)
