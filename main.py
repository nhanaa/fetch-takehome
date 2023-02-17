import sys
import csv

def main():
  # Arguments error handling
  if len(sys.argv) != 3:
    print("Invalid number of arguments")
    return

  try:
    if not (float(sys.argv[1]).is_integer() and int(sys.argv[1]) >= 0):
      print("Invalid number of points")
      return
  except ValueError:
      print("Invalid number of points")
      return

  points_to_spend = int(sys.argv[1])
  filename = sys.argv[2]

  # Read the csv and add all transactions into a list
  transactions = []
  with open(filename, "r") as file:
    csvreader = csv.reader(file)
    for row in csvreader:
      transactions.append(row)

  # Sort the transactions by date and time from oldest to newest
  sorted_transactions = sorted(transactions[1:], key=lambda x : x[2])

  # Initialize a map to keep track of the balances of the payers
  balances = {}

  for payer, points, timestamp in sorted_transactions:
    # Initialize the payer if not already
    if payer not in balances:
      balances[payer] = 0

    points = int(points)
    if points_to_spend > 0:
      if points_to_spend >= points:
        points_to_spend -= points
      else:
        leftover = abs(points_to_spend - points)
        points_to_spend = 0
        balances[payer] += leftover
    else:
      balances[payer] += points

  for payer, balance in balances.items():
    print(f"\"{payer}\": {balance}")


if __name__ == "__main__":
  main()
