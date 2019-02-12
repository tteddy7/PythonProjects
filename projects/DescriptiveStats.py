# Calculate descriptive statistics for a list of numbers

# Import dependencies
import math

# Define function
def descriptiveStats():
  # Prepare to gather numbers
  numbersList = []
  stopGathering = 0

  # Gather list of numbers from user
  while (stopGathering == 0):
    enteredNumber = input('Please enter a number (press enter to stop): ')
    if (enteredNumber == ''):
      stopGathering = 1
    else:
      enteredNumber = float(enteredNumber)
      numbersList.append(enteredNumber)

  # Calculate sum of list
  listSum = 0
  for number in numbersList:
    listSum += number

  # Calculate mean
  listMean = listSum / len(numbersList)

  # Round mean based on user input
  roundTo = int(input('How many decimal places would your numbers rounded to? '))
  listMean = round(listMean, roundTo)

  # Calculate median
  medianList = numbersList
  medianList.sort()
  # Determine if list is even or odd length
  if (len(numbersList) % 2 == 0):
    # If it's even, grab the middle two numbers and average them
    medianTempNo1 = medianList[int(len(medianList) / 2)]
    medianTempNo2 = medianList[int((len(medianList) / 2) + 1)]
    listMedian = (medianTempNo1 + medianTempNo2) / 2
  else:
    # If it's odd, grab the middle number.
    listMedian = medianList[math.ceil(len(medianList) / 2)]

  # Calculate mode
  listMode = max(set(medianList), key=medianList.count)

  # Calculate range
  listMin = min(numbersList)
  listMax = max(numbersList)

  # Calculate variance
  listSqDiffsFromMean = []
  for number in numbersList:
    listSqDiffsFromMean.append((number - listMean) ** 2)
  listVar = 0
  for sqDiff in listSqDiffsFromMean:
    listVar += sqDiff
  listVar = round(listVar / len(numbersList), roundTo)
  
  # Calculate standard deviation and standard error
  listStDev = round(listVar ** 0.5, roundTo)
  listStErr = round(listStDev / len(numbersList), roundTo)

  # Ask user for confidence interval
  confInt = int(input('Please enter a confidence interval (90, 95, 99): '))
  if (confInt == 90):
    tStat = 1.64
  elif (confInt == 95):
    tStat = 1.96
  elif (confInt == 99):
    tStat = 2.58

  # Calculate confidence interval
  listLB = round(listMean - (tStat * listStErr), roundTo)
  listUB = round(listMean + (tStat * listStErr), roundTo)

  # Print data for user
  print(f'Mean:     {listMean}')
  print(f'Median:   {listMedian}')
  print(f'Mode:     {listMode}')
  print(f'Range:    [{listMin}, {listMax}]')
  print(f'Variance: {listVar}')
  print(f'Standard Deviation: {listStDev}')
  print(f'Standard Error:     {listStErr}')
  print(f'{confInt}% confidence interval:')
  print(f'  Lower Bound: {listLB}')
  print(f'  Upper Bound: {listUB}')

# Call function
descriptiveStats()