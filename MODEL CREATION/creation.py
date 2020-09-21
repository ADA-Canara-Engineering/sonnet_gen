#!/usr/bin/env python
#sonnet generator
#ada_lovelase_day_celebration
#19/09/2020


############## 1 ##############
#importing lib/packages
from keras.models import Sequential
from keras.layers import Dense, LSTM
from keras.optimizers import SGD

import numpy as np
import sys
import os
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import seaborn as sn

np.random.seed()



############## 2 ##############
#provide data set
with open('res/dataset.txt', 'r', encoding = 'utf8') as f:
    data = f.read().lower()

#preprocessing is not need, since sonnet can't contain NaN
#Analyise data set
#so here we can observe average length of the sonnet interms of characters
#\n\n is a differentiater
sonnets = data.split('\n\n')
sonnet_len = [len(sonnet) for sonnet in sonnets]

plt.style.use('classic')
plt.figure(figsize=(15,10))
plt.plot([i for i in range(1, len(sonnets)+1)], sonnet_len)
plt.show()

print('AVG len: %f' % np.mean(sonnet_len))



############## 3 ##############
#Vectorization of the data for the gen of new datas
#max length of characters per sentence is approx. 40
max_length_seq = 40
step_size = 3
sentences = []
destin = []

for i in range(0, len(data) - max_length_seq, step_size):
    sentences.append(data[i:i + max_length_seq])
    destin.append(data[max_length_seq + i])

#all unique characters
uniques = sorted(list(set(data)))

#unique --> integer index
unique_index = dict((unique , uniques.index(unique)) for unique in uniques)

#creating numpy array to hold this vectorized data
x = np.zeros((len(sentences),max_length_seq, len(uniques)), dtype=np.bool)
y = np.zeros((len(sentences), len(uniques)), dtype=np.bool)
for i, sentences in enumerate(sentences):
    for j, unique in enumerate(sentences):
        x[i, j, unique_index[unique]] = 1
    y[i, unique_index[destin[i]]] = 1

print("Size of training sequences:", x.shape)
print("Size of training targets:", y.shape)



############## 4 ##############
#Creation of  a model and fitting it
# output with softmax activation function
model = Sequential()
model.add(LSTM(128, input_shape=(max_length_seq, len(uniques))))
model.add(Dense(len(uniques), activation='softmax'))
model.summary()

optimizer = SGD(lr=0.01, momentum=0.9, nesterov=True)
model.compile(optimizer=optimizer, loss='categorical_crossentropy')




############## 5 ##############
#predict probability --> newly created probability
def sample(preds, temperature=1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)


epochs = 60 #100

loss = []  # save model's loss

#dir to store generated text
base_dir = 'data_generated'
if not os.path.isdir(base_dir):
    os.mkdir(base_dir)

for epoch in range(1, epochs+1):
    #(if encountered with utf-9 than pass it)
    try:
        print("Epoch", epoch)
    #fit model with 1 epoch
    #generate text give seed
        history = model.fit(x, y, batch_size=128, epochs=1)
        loss.append(history.history['loss'][0])
    
    #dir for each epoch
        epoch_dir = os.path.join(base_dir, 'epoch_' + str(epoch))
        if not os.path.isdir(epoch_dir):
            os.mkdir(epoch_dir)
    
    #random seed feed into model and generate text
        start_idx = np.random.randint(0, len(data) - max_length_seq - 1)
        seed_text = data[start_idx:start_idx + max_length_seq]
        for temp in [0.2, 0.5, 1.0, 1.3]:
            data_generated = seed_text
            temp_file = 'epoch' + str(epoch) + '_temp' + str(temp) + '.txt'
            file = open(os.path.join(epoch_dir, temp_file), 'w')
            file.write(data_generated)
        
        # generate 1 sonnet length chars
            for i in range(625): #approx 625
            # Vectorize
                sampled = np.zeros((1, max_length_seq, len(uniques)))
                for j, unique in enumerate(data_generated):
                    sampled[0, j, unique_index[unique]] = 1.
            #next unique
                preds = model.predict(sampled, verbose=0)[0]
                pred_idx = sample(preds, temperature=temp)
                next_unique = uniques[pred_idx]
            
            #join unique to seed text
                data_generated += next_unique
                data_generated = data_generated[1:]
            #text file
                file.write(next_unique)
            print('Temp ' + str(temp) + " done.")
            file.close()
    except:
        pass


############## 6 ##############
 model.save('sonnet_gen_model.h5')



 ############## attributions #############
 # 1. https://spectrum.ieee.org/artificial-intelligence/machine-learning/this-ai-poet-mastered-rhythm-rhyme-and-natural-language-to-write-like-shakespeare

 # 2. https://github.com/deepmind/sonnet  reference to building model
 # 3. kennyng hmm sonnet generator model - reference
 # 4. Text Generation With LSTM Recurrent Neural Networks in Python with Keras
 #      https://machinelearningmastery.com/text-generation-lstm-recurrent-neural-networks-python-keras/
