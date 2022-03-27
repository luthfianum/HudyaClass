class MoneySaver:
  
  def __init__(self):
    self.budget = 0
    self.log = []

  def set_budget(self, budget):
    self.budget = budget

  def run(self):
    budget = int(input("Masukkan budget bulanan anda: "))
    self.set_budget(budget)

    while True:
      item = input("Masukkan nama pengeluaran: ")
      amount = int(input("Masukkan jumlah pengeluaran: "))

      if item == "break":
        break

      self.log.append({
        "activity": item,
        "amount": amount,
        "balance_before": self.budget,
        "balance_after": self.budget - amount
      })
      self.set_budget(self.budget - amount)
    
    print("Pencatatan Keuangan: ")
    for item in self.log:
      print(f"{item['activity']} - {item['amount']}")


money = MoneySaver()
money.run()