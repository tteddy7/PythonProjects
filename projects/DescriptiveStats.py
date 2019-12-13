# Calculate descriptive statistics for a list of numbers
# By Ted Silbernagel

import math
from typing import List, Text, Dict

# Define function to gather numbers
def gatherNumbers() -> List[float]:
  # Prepare to gather numbers
  numbersList = []
  stopGathering = False

  # Gather list of numbers from user
  while stopGathering == False:
    enteredNumber = input('Please enter a number (press enter to stop): ')
    if enteredNumber == '':
      stopGathering = True
    else:
      numbersList.append(float(enteredNumber))
  return numbersList


def calcMean(data: List[float]) -> float:
  return sum(data) / len(data)


def calcMedian(data: List[float]) -> float:
  sorted_data = sorted(data)
  # Determine if list is even or odd length
  if not len(sorted_data) % 2:
    # If it's even, grab the middle two numbers
    return [
      sorted_data[int((len(sorted_data) / 2) - 1)],
      sorted_data[int(len(sorted_data) / 2)],
    ]
  else:
    # If it's odd, grab the middle number
    return sorted_data[len(sorted_data) // 2]


def calcMode(data: List[float]) -> float:
  sorted_data = sorted(data)
  return max(set(sorted_data), key=sorted_data.count)


def calcVariance(data: List[float]) -> float:
  mean = calcMean(data)
  return sum([((num - mean) ** 2) for num in data]) / len(data)


# Define function to calculate stats
def descriptiveStats(numbersList: List[float]) -> Dict[Text, float]:
  # Round based on user input
  roundTo = int(input('How many decimal places would you like your numbers '
                      'rounded to? '))

  # Set up return data dict
  returnData = {
    'mean': round(calcMean(numbersList), roundTo),
    'median': calcMedian(numbersList),
    'mode': calcMode(numbersList),
    'min': min(numbersList),
    'max': max(numbersList),
    'variance': round(calcVariance(numbersList), roundTo),
  }

  returnData['stDev'] = round(returnData['variance'] ** 0.5, roundTo)
  returnData['stErr'] = round(returnData['stDev'] / len(numbersList), roundTo)

  # Ask user for confidence interval
  returnData['confInt'] = int(input('Please enter a confidence interval '
                                    '(90, 95, 99): '))
  tStats = {
    90: 1.64,
    95: 1.96,
    99: 2.58,
  }

  # Calculate confidence interval
  returnData.update({
    'lowerBound': round(returnData['mean'] - (tStats[returnData['confInt']]
                                              * returnData['stErr']),
                        roundTo),
    'upperBound': round(returnData['mean'] + (tStats[returnData['confInt']]
                                              * returnData['stErr']),
                        roundTo),
  })

  # Return dict of data
  return returnData

# Call function to gather numbers and calculate descriptive stats
response = descriptiveStats(gatherNumbers())

# Print data for user
print(f'Mean:     {response["mean"]}')
print(f'Median:   {response["median"]}')
print(f'Mode:     {response["mode"]}')
print(f'Range:    [{response["min"]}, {response["max"]}]')
print(f'Variance: {response["variance"]}')
print(f'Standard Deviation: {response["stDev"]}')
print(f'Standard Error:     {response["stErr"]}')
print(f'{response["confInt"]}% confidence interval:')
print(f'  Lower Bound: {response["lowerBound"]}')
print(f'  Upper Bound: {response["upperBound"]}')
