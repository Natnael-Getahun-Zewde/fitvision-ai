import pandas as pd
import torch
import torch.nn as nn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv("dataset/dataset.csv")

X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

encoder = LabelEncoder()
y = encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

X_train = torch.tensor(X_train).float()
y_train = torch.tensor(y_train)

input_size = X_train.shape[1]

class ExerciseModel(nn.Module):

    def __init__(self, input_size):

        super().__init__()

        self.network = nn.Sequential(
            nn.Linear(input_size, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 4)
        )

    def forward(self, x):

        return self.network(x)


model = ExerciseModel(input_size)

loss_fn = nn.CrossEntropyLoss()

optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

epochs = 20

for epoch in range(epochs):

    outputs = model(X_train)

    loss = loss_fn(outputs, y_train)

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()

    print(f"Epoch {epoch+1}/{epochs}  Loss: {loss.item():.4f}")

torch.save(model.state_dict(), "models/exercise_model.pth")

print("Model saved to models/exercise_model.pth")