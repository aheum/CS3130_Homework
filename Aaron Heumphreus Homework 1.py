# %%
import numpy as np
import pandas as pd
from numpy.random import default_rng
import math
import random
import time

# %%
def brute(argument):
    j=0
    total=0
    for i in argument:
        total=total+i*(x**j)
        j=j+1
    bruteforcetotal=total
    return bruteforcetotal


# %%
def horner(argument):
    coefficientsR=argument
    coefficientsR.reverse()
    j=0
    total=coefficientsR[0]
    for i in range(len(coefficientsR)-1):
        total=(x*total)+coefficientsR[i+1]
    hornertotal=total
    return hornertotal

# %%
def mklist(o,e):
    co=10**e
    coeff=[co]*o
    return coeff

# %%
#Small Test, n=10 d=2
x=2
n=10
d=2

coefficientssmall=mklist(n,d)
print(coefficientssmall)



# %%
#Small test Brute
start_time=time.time()
brutesmall=brute(coefficientssmall)
brutetime=("%s seconds" % (time.time() - start_time))

# %%
#Small test Horner
start_time=time.time()
hornersmall=horner(coefficientssmall)
hornertime=("%s seconds" % (time.time() - start_time))

# %%
print("Small Test Results")
print("Starting variables:")
print("x=",x)
print("n=",n)
print("d=",d)
print()
print("Brute Force Computation Time: ",brutetime)
print("Horner's Rule Computation Time: ",hornertime)
print()
print("Status of output for Horner's rule and Brute Force methods:")
if brutesmall == hornersmall:
    print("Success! Output same.")
else:
    print("Error. Outputs different.")
print("Outeput: ",brutesmall, hornersmall)

# %%
#Big Test, n=10000 d=20
x=2
n=100000
d=2000

coefficientsbig=mklist(n,d)

# %%
#Big test Brute
start_time=time.time()
brutebig=brute(coefficientsbig)
brutetime=("%s seconds" % (time.time() - start_time))

# %%
#Big test, Horner
start_time=time.time()
hornerbig=horner(coefficientsbig)
hornertime=("%s seconds" % (time.time() - start_time))

# %%
print("Big Test Results")
print("Starting variables:")
print("x=",x)
print("n=",n)
print("d=",d)
print()
print("Brute Force Computation Time: ",brutetime)
print("Horner's Rule Computation Time: ",hornertime)
print()
print("Status of output for Horner's rule and Brute Force methods:")
if brutebig == hornerbig:
    print("Success! Output same.")
else:
    print("Error. Outputs different.")

# %% [markdown]
# Project description:
# In this project, we will compare two different algorithms that are used to evaluate
# polynomials. The goal is to understand the importance of the efficiency of an algorithm.
# The first algorithm is the brute force method in which we evaluate polynomials in the
# usual way. The second algorithm uses the Horner’s Rule to evaluate polynomials. The
# polynomials to be evaluated have the following general form:
# P(x)=a0+a1x+a2x^2+...+anx^n


