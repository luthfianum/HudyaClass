class Clinic:
  def __init__(self):
    self.queue = []
    self.name = None

  def run(self):
    while True:
      self.name = input("Please input your name: ")
      if((self.name) < 2):
        print("Your name should be more than 2 characters")
        continue
      check = self.check_queue()
        
      if not check:
        print("Your name is already in queue")
        continue

      self.queue.append(self.name.lower())

  def check_queue(self):
    if self.name.lower() in self.queue:
      return False
    return True


clinic = Clinic()
clinic.run()