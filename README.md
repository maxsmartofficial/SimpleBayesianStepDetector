# Simple Bayesian Step Detector
## Description
This is a method for finding a 'step' or changepoint in a segment of time-series data, and is an implementation of the algorithm found in Ruanaidh and Fitzgerald [2012]. The method assumes the data can be represented by two sub-segments, each of which is comprised of values drawn from a Gaussian distribution. The centres of these two Gaussian distributions must be distinct. The changepoint is the point at which the centre changes. 

## Usage

The data is represented as a list or numpy array of length N where N > 1. Calling `SBSD(data)` will give the predicted index of the changepoint. Calling `test()` will show off how great the algorithm is by printing the actual changepoint, the predicted changepoint and plotting a graph of the data with a line representing the predicted changepoint.

## Reference

Ruanaidh, J.J.O and Fitzgerald, W.J., 2012. Numerical Bayesian methods applied to signal processing. Springer Science and & Business Media. 