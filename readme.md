# Deep Learning Observables in Computational Fluid Dynamics

## Introduction
This project focuses on studying the relationship between the coefficients of lift and drag for NACA foils with varying thickness under different flow conditions. The flow parameters that are considered include the angle of attack, Mach number, and Reynolds number. The objective is to develop a neural network that can approximate the relationship between the input parameters (NACA airfoil number, angle of attack, Mach number, and Reynolds number) and the corresponding outputs (coefficients of lift and drag).

## Data Generation
The data used in this project is generated using XFLR5, a software that stores the data across multiple files. The generated data is then preprocessed and combined into a format that can be readily fed into the neural network.

## Neural Network Model
The neural network model is implemented using a Jupyter notebook (`model.ipynb`). It leverages Keras' hyperband tuner to optimize the model's hyperparameters. 

## Usage
To run this project, follow these steps:
1. Execute the `data.py` script, which will generate and preprocess the necessary data files.
2. Open and run the `model.ipynb` notebook, which contains the code for training and evaluating the neural network model.
