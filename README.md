# Quantum at the Dunes 2026 in Natal
## Lecture Notes on Introduction to Classical Shadows

The challenge:
# A Classical Shadows Challenge: Estimating Overlap between two single qubit quantum states
In the lecture we discussed how classical shadows estimate linear observables.

Now the question:
What happens if the quantity to estimate is *the overlap between two quantum states*?

This challenge asks you to formulate, analyze, and code a small example of classical shadow estimators for the **trace inner product** (Hilbert–Schmidt overlap): $\mathrm{tr}(\rho\sigma)$ for $\rho$, $\sigma$ a pure quantum state. With this appraoch, the purity, $\mathrm{tr}(\rho^2)$ can be easily deducted by setting $\sigma=\rho$.

## Your Task
Using the **single qubit** shadow protocol we saw in the lecture, do the following:

### Define the 'Single-Shot' Estimator 
Using the classical shadows protocol that we studied in the three lectures, how do you construct an unbiased estimator for $\mathrm{tr}(\rho\sigma)$?


### Analyze your 'Single-Shot' estimator
Compute explicitly:
* The possible values of the single-shot estimator.
* A bound on its magnitude.
* A bound on the variance.


### Define the multi-shot estimator
Given $N$ independent samples from $\rho$ (or $N$ from $\rho$ and $N$ from $\sigma$):
* Write down the empirical estimator.
* Show that it is unbiased.
* Give the sample complexity (Bernstein, no union bound) with the computed magnitude and variance of the single-shot estimator.


Let's say we have the expected value of the protocol to be $p=\mathrm{tr}(\rho\sigma)$.
Then define the single shot estimator $\hat p$ such that for $N\rightarrow\infty$ the multi-shot estimator $N^{-1}\sum_{t=1}^N\hat p$ goes to $\mathrm{tr}(\rho\sigma)$.

### Code a small example of the protocol
Write some (small) example on how this protocol would look like in practice. You can simulate your data acquisition phase however you want.

## Hint/Tipps
There is no one right solution here. I know of at least two ways of defining the single shot estimator for that, and they both have different variances. ;)

Also, check out the 'PREDICTING NONLINEAR FUNCTIONS' subsection of the shadow paper 'Predicting Many Properties of a Quantum System from Very Few Measurements' ;)
