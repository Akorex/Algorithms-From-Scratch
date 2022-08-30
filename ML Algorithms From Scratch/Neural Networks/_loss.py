import numpy as np
from math import log as l

# a single batch
softmax_output = [0.7, 0.2, 0.1]
target_output = [1, 0, 0]

loss = 0
for sf_out, tar_out in zip(softmax_output, target_output):
    loss += l(sf_out) * tar_out
loss = -loss
print(loss)

# 3 batches & sparse targets
softmax_output = [[0.7, 0.2, 0.1], 
                [0.1, 0.6, 0.3],
                 [0.08, 0.9, 0.02]]
softmax_output = np.array(softmax_output)
class_targets = [0, 1, 1]

neg_log = -np.log(softmax_output[range(len(softmax_output)), class_targets])
loss = np.mean(neg_log)
print(loss)

# 3 batches & dense targets
softmax_output = [[0.7, 0.2, 0.1],
                    [0.1, 0.6, 0.3],
                    [0.08, 0.9, 0.02]]
softmax_output = np.array(softmax_output)
class_targets = [[1, 0, 0],
                [0, 1, 0],
                [0, 1, 0]]
class_targets = np.array(class_targets)

# for sparse targets
if len(class_targets.shape) == 1:
    correct_confidences = softmax_output[range(len(softmax_output)), class_targets]

# for dense targets
elif len(class_targets.shape) == 2:
    correct_confidences = np.sum(softmax_output * class_targets, axis=1)

neg_log = -np.log(correct_confidences)
loss = np.mean(neg_log)
print(loss)