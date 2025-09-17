import pandas as pd
df = pd.read_csv("\ArtificialIntel\data\PracTitanic.csv")
collist=['sex', 'age', 'fare', 'class', 'survived']
# def data_fermentation(target):
#   ind = df.drop(columns=target,axis=1)
#   dep = df[target]
#   return ind,dep
# ind,dep = data_fermentation('survived')
# incol   = ind.columns.tolist()
# from keras.models import Sequential
# from keras.layers import Input,Dense,BatchNormalization
# from keras.activations import relu,sigmoid,leaky_relu
# from keras.initializers import he_normal,he_uniform
# from keras.optimizers import Adam
# from keras.losses import binary_crossentropy

# def arc(features):
#   model =Sequential()
#   model.add(Input(shape=(features,)))
#   model.add(Dense(128,kernel_initializer=he_normal,activation=relu))
#   model.add(Dense(16,kernel_initializer=he_uniform,activation=leaky_relu))
#   model.add(Dense(128,kernel_initializer=he_normal,activation=relu))
#   model.add(Dense(16,kernel_initializer=he_uniform,activation=leaky_relu))
#   model.add(Dense(128,kernel_initializer=he_normal,activation=relu))
#   model.add(Dense(16,kernel_initializer=he_uniform,activation=leaky_relu))
#   model.add(Dense(128,kernel_initializer=he_normal,activation=relu))
#   model.add(Dense(16,kernel_initializer=he_uniform,activation=leaky_relu))
#   model.add(Dense(1,activation=sigmoid))
#   return model
# ANN = arc(ind.shape[1])
# ANN.summary()
