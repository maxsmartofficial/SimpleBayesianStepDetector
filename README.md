# Simple Bayesian Step Detector
## Description
This is an algorithm for finding a 'step' or changepoint in a segment of time-series data. The method assumes the data can be represented thus:
\[ x_t = \begin{cases} 
      \mu_1 + \epsilon_t & t < c  \\
      \mu_2 + \epsilon_t & t \geq c\\
   \end{cases}
\]