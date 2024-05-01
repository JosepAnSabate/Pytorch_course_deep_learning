import torch
import torch.nn as nn


class RegressionModel(nn.Module):
    # You should build your model with at least 2 layers using tanh activation in between
    def __init__(self, input_size, hidden_size):
        super().__init__()
        self.layer1 = nn.Linear(input_size, 
                                 hidden_size)
        self.layer2 = nn.Linear(hidden_size,
                                    hidden_size)
        self.layer3 = nn.Linear(hidden_size,
                                    1)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.layer1(x))
        x = self.relu(self.layer2(x))
        x = self.layer3(x)
        return x
        