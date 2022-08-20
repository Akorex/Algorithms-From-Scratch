import pandas as pd
from sklearn.preprocessing import OneHotEncoder
# for Gender
ohe = OneHotEncoder()
ohe.fit(train[['Gender']])
temp = ohe.transform(train[['Gender']]).toarray()
temp = pd.DataFrame(temp, columns=ohe.get_feature_names_out())
train = pd.concat([train, temp], axis=1).drop(columns=['Gender'])