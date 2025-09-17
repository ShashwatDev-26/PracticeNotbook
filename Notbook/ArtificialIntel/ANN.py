import pandas as pd
df = pd.read_csv("Notbook\ArtificialIntel\data\PracTitanic.csv")
collist=['sex', 'age', 'fare', 'class', 'survived']
def data_fermentation(target):
  ind = df.drop(columns=target,axis=1)
  dep = df[target]
  return ind,dep
ind,dep = data_fermentation('survived')
incol   = ind.columns.tolist()
from keras.models import Sequential
from keras.layers import Input,Dense,BatchNormalization,Dropout
from keras.activations import relu,sigmoid,leaky_relu,tanh
from keras.initializers import he_normal,he_uniform
from keras.optimizers import Adam
from keras.metrics import Accuracy,F1Score
from keras.losses import binary_crossentropy

def arc(features):
  model =Sequential()
  model.add(Input(shape=(features,)))
  model.add(Dense(128,kernel_initializer=he_normal,activation=relu))
  model.add(Dense(16,kernel_initializer=he_uniform,activation=leaky_relu))
  model.add(Dense(128,kernel_initializer=he_normal,activation=relu))
  model.add(Dropout(0.001))
  model.add(BatchNormalization())
  model.add(Dense(16,kernel_initializer=he_uniform,activation=leaky_relu))
  model.add(Dense(128,kernel_initializer=he_normal,activation=relu))
  model.add(Dense(16,kernel_initializer=he_uniform,activation=leaky_relu))
  model.add(Dense(128,kernel_initializer=he_normal,activation=relu))
  model.add(Dense(16,kernel_initializer=he_uniform,activation=tanh))
  model.add(Dense(1,activation=sigmoid))
  return model
ANN = arc(ind.shape[1])
ANN.summary()
ANN.compile(optimizer=Adam(0.01),loss=binary_crossentropy,metrics=[Accuracy,F1Score])
ANN.fit(ind,dep,epochs=12,batch_size=100,shuffle=True,validation_split=0.3)
