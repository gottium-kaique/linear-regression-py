from typing import List
import math

class LinearModel:
  def __init__(self):
    self.x_values = []
    self.y_values = []
    self.list_size = 0
    self.y_total = 0
    self.x_total = 0
    self.squared_x = 0
    self.x_mult_y = 0
    self.is_the_first_iteration = True

  def fit(self, x_train: List, y_train: List):
    if len(x_train) != len(y_train):
      raise 'Lists have diffences dimensions'

    self.list_size += len(x_train)

    for index in range(len(x_train)):
      self.x_values.append(x_train[index])
      self.y_values.append(y_train[index])

    for index in range(0, self.list_size):
      self.x_total += self.x_values[index]
      self.y_total += self.y_values[index]
      self.squared_x += self.x_values[index] ** 2
      self.x_mult_y += self.x_values[index] * self.y_values[index]

    self.a = (
      (self.list_size * self.x_mult_y - self.x_total * self.y_total) /
      (self.list_size * self.squared_x - self.x_total ** 2)
    )

    y_mean = self.y_total / self.list_size
    x_mean = self.x_total / self.list_size

    self.b = (y_mean - self.a * x_mean)
    self.is_the_first_iteration = False

  def predict(self, x_test: int) -> int:
    y = self.a * x_test + self.b

    return y

if __name__ == "__main__":
  x = [1, 2, 3, 4]
  y = [3, 6, 9, 12]

  x2 = [10, 20, 30]
  y2 = [30, 60, 95]

  model = LinearModel()
  model.fit(x, y)
  model.fit(x2, y2)

  print(model.predict(30))