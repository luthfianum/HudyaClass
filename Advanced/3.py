class OnlineDating:

  def __init__(self):
    self.girls = [
      {"name": "Ayu", "age": 23, "match": True},
      {"name": "Fiani", "age": 28, "match": False},
      {"name": "Vivian", "age": 23, "match": True},
    ]

    self.swiped = []

  def run(self):
      name = input("Masukkan nama anda: ")
      print(f"Hello, {name} welcome to Online Dating")

      for item in self.girls:
        print(f"Name: {item['name']}")
        print(f"Age: {item['age']}")

        action = input("What's your action? (Y/N)")

        if action.lower() == "y":
          self.swiped.append(item)
        elif action.lower() == "n":
          self.swiped.append(item)
        elif action.lower == "logout":
          print('')
          break

dating_app = OnlineDating()
dating_app.run()