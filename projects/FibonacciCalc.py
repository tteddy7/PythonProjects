# Generate the nth term in the Fibonacci sequence

# Define function
def fibonacciGen():
  # Get n term from user
  print('This program will get you a specific number in the Fibonacci sequence.')
  nTerm = int(input('Please enter which number in the sequence you would like: '))
  
  # Check to see if they picked 1 or 2
  if nTerm < 4:
    if nTerm == 1:
      fibNo = 0
      # Print calculation for user
      print(f'The {nTerm}st number in the Fibonacci sequence is {fibNo}')
    elif nTerm == 2:
      fibNo = 1
      # Print calculation for user
      print(f'The {nTerm}nd number in the Fibonacci sequence is {fibNo}')
    elif nTerm == 3:
      fibNo = 1
      # Print calculation for user
      print(f'The {nTerm}rd number in the Fibonacci sequence is {fibNo}')
  # Otherwise will need to generate
  else:
    # Initialise the loop at 3
    prevNo1 = 0
    prevNo2 = 1
    fibNo = 1
    # Start the loop to generate the Fibonacci number
    for i in range(3, nTerm):
      prevNo1 = prevNo2
      prevNo2 = fibNo
      fibNo = prevNo1 + prevNo2
    # Print calculation for user
    print(f'The {nTerm}th number in the Fibonacci sequence is {fibNo}')

# Call function
fibonacciGen()