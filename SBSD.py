import matplotlib.pyplot as plt
import numpy as np

def SBSD(data):
    """Predicts position of step occuring
input: vector of time-series data
output: index of predicted step"""

    N = len(data)

    # Array of probabilities
    p = []

    # Calculate sum of squares
    sumOfSquares = 0
    for i in range(N):
        sumOfSquares += data[i]**2
        
    # Calculate probabilities
    for i in range(N-1):
        # Calculate sum of past values
        Sp = sum(data[:i+1])
        # Calculate sum of future values
        Sf = sum(data[i+1:])

        
        p_i = (sumOfSquares - ((1/(i+1))*Sp**2) - (1/(N-(i+1)))*Sf**2)**(-(N-2)/2)

        p.append(p_i)
    

    return(p.index(max(p)))

def test():
    """Run a simple test of the SBSD function and plot results"""
    
    
    N = 100
    # Choose step position at random
    step = np.random.randint(10,N-10)

    # Create test data
    data1 = np.random.normal(0,1,step+1)
    data2 = np.random.normal(2,1,N-step-1)
    data = np.append(data1,data2)
    
    # Predict step position
    predictedStep = SBSD(data)
    
    # Plot data
    plt.plot(data)
    plt.axvline(predictedStep,color='r')
    plt.show()
    
    print(step)
    print(predictedStep)