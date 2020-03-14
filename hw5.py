import numpy as np
import matplotlib.pyplot as plt
import math as math

def generatePoints(size, sigma_sqr):
    S = []
    for i in range(size):
        y = int (np.random.uniform(0, 3))
        if (y == 0):
            mu = [-1, 0]
        elif (y == 1):
            mu = [1, 0]
        else:
            mu = [0, 1]
        x_0 = np.random.normal(mu[0], sigma_sqr)
        x_1 = np.random.normal(mu[1], sigma_sqr)
        _x = np.array((x_0, x_1))
        S.append([_x, y])
    return S

#def plotDecisionBoundary()

def kNN(k, S, x):
    dist = [ [math.sqrt((x[0] - s[0][0])**2 + (x[1] - s[0][1])**2), s[1]] for s in S]
    dist = sorted(dist, key=lambda entry: entry[0])
    dist = dist[0: k]
    dist_y = [s[1] for s in dist]
    return max(set(dist_y), key = dist_y.count)

def predictionError(k, S, X):
    errors = 0
    for x in X:
        if (x[1] != kNN(k, S, x[0])):
            errors = errors + 1
    return float(errors) / float(len(X))

S = generatePoints(300, 0.15)

print (kNN(5, S, [0.5, 0.9]))

def ex_1_1():
    S = generatePoints(300, 0.10)
    K = [1, 2, 5, 10]
    for k in K:
        x_plane = [0.01 * a for a in range(-150, 150)]
        discrete_domain = [[a,b] for a in x_plane for b in x_plane]
        discrete_image = [ [kNN(k, S, [a,b]) for b in x_plane] for a in x_plane]
        plt.contourf(x_plane, x_plane, discrete_image)
        plt.grid()
        plt.title("k = " + str(k))
        plt.savefig("hw5_graphs/E1Q1/decisionBoundary k = " + str(k) + ".pdf")
        plt.close()

def ex_1_2():
    sigma_sqr = [0.05, 0.10, 0.15, 0.20, 0.25]
    k = [1, 2, 5, 10]
    errors = []
    for ssq in sigma_sqr:
        errors_ssq = []
        for _k in k:
            errors_k = []
            for i in range(50):
                S = generatePoints(300, ssq)
                errors_k = errors_k + [predictionError(_k, S[0 : 200], S[200 : 300])]
            errors_ssq.append([np.mean(errors_k), np.std(errors_k)])
        errors = errors + [errors_ssq]
    print errors
    plt.errorbar(k, [a[0] for a in errors[4]], yerr = [a[1] for a in errors[4]], fmt = '.')
    plt.grid()
    plt.title("$\sigma(x_i)^2$ fixed at 0.25")
    plt.xlabel("k")
    plt.ylabel("Mean and std deviation of the error [$\mu(e)$ and $\sigma(e)$]")
    plt.savefig("hw5_graphs/E1Q2/sigma_fixed.pdf")
    plt.close()

    plt.errorbar(sigma_sqr, [a[2][0] for a in errors], yerr = [a[2][1] for a in errors], fmt = '.')
    plt.grid()
    plt.title("K fixed at 5")
    plt.xlabel("$\sigma(x_i)^2$")
    plt.ylabel("Mean and std deviation of the error [$\mu(e)$ and $\sigma(e)$]")
    plt.savefig("hw5_graphs/E1Q2/k_fixed.pdf")
    plt.close()

#ex_1_1()
ex_1_2()
