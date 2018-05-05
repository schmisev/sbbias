import math
import itertools

# Setup
score = (0, 0)
time = 0 # min
q_a = 0.5
q_b = 1 - q_a
depth = 20
rate = 3/90

# Helper functions
def poisson(r, t, k):
    return (math.exp(-r*t))*(math.pow(r*t,k)/math.factorial(k))

def timeline(i, j, q_a, q_b):
    return ((q_a ** i) * (q_b ** j)) * math.factorial(i + j)/(math.factorial(j)*math.factorial(i))

# Calculation
def win_probability(score, time, q_a, q_b, depth, rate):
    p = 0
    for i in range(depth):
        j = 0
        while True:
            if (score[0] + i - (score[1] + j)) <= 0:
                # Checking for losing score
                break
            probability = poisson(rate, 90 - time, i + j) * timeline(i, j, q_a, q_b)
            p = p + probability
            j = j + 1
        i += 1
    return p

def bias(score, time, q_a, q_b, depth, rate):
    return win_probability(score, time, q_a, q_b, depth, rate) - win_probability((0, 0), 0, q_a, q_b, depth, rate)

print(bias((1, 0), 10, 0.5, 0.5, 20, 3/90))