import torch
import torch.nn as nn
import torch.nn.functional as F


class QNetwork(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size, action_size, seed):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed

        Input shape: 1x37
        Layers
        ======
            name    (type)   - filters, flt_size stride
            cnl1    (conv1d) -   32        7       2
            cnl2    (conv1d) -   64        4       2
            cnl3    (conv1d) -   64        3       1
                             - num_units
            dense1  (dense)  - 512
            out     (dense)  - action_size
        """
        super(QNetwork, self).__init__()
        self.seed = torch.manual_seed(seed)

        self.cnl1 = nn.Conv1d(1, 32, 7, 2)
        self.cnl2 = nn.Conv1d(32, 64, 4, 2)
        self.cnl3 = nn.Conv1d(64, 64, 3, 1)
        self.dense1 = nn.Linear(320, 512)
        self.out = nn.Linear(512, action_size)

    def forward(self, state):
        """Build a network that maps state -> action values."""
        x = state.unsqueeze(1)
        x = F.relu(self.cnl1(x))
        x = F.relu(self.cnl2(x))
        x = F.relu(self.cnl3(x))
        x = x.view(x.shape[0], -1)  # flatten
        x = F.relu(self.dense1(x))
        x = self.out(x)
        return x
