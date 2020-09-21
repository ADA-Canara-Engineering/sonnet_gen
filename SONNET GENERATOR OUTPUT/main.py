#!/usr/bin/env python
#sonnet generator
#ada_lovelase_day_celebration
#19/09/2020


#import req. lib/package
from keras.models import load_model
import os
import numpy as np


#training text and vectorize to 3D tensor
def load_data(max_length_seq=25, step=3):
    with open(os.path.join(os.getcwd(),os.path.join('res','dataset.txt')), 'r', encoding = 'utf8') as f:
        data = f.read().lower()

    sentences = []
    targets = []
    for i in range(0, len(data) - max_length_seq, step):
        sentences.append(data[i:i + max_length_seq])
        targets.append(data[max_length_seq + i])
    #all unique characters
    uniques = sorted(list(set(data)))
    #unique --->  integer indices
    unique_indices = dict((unique, uniques.index(unique)) for unique in uniques)
    return data, unique_indices, uniques

#Reweight predicted
def sample(preds, temperature=1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

#model loading and construction through prediction
def generate_sonnet():
    max_length_seq = 40
    step = 3
    new_gen = ""
    data, unique_indices, uniques = load_data(max_length_seq, step)

    model = load_model('sonnet_gen_model.h5')
    start_idx = np.random.randint(0, len(data) - max_length_seq - 1)
    new_sonnet = data[start_idx:start_idx + max_length_seq]
    new_gen += new_sonnet
    for i in range(625):

        sampled = np.zeros((1, max_length_seq, len(uniques)))
        for j, unique in enumerate(new_sonnet):
            sampled[0, j, unique_indices[unique]] = 1.


        preds = model.predict(sampled, verbose=0)[0]
        pred_idx = sample(preds, temperature=0.5)
        next_unique = uniques[pred_idx]

        # Append unique and ready for next unique
        new_sonnet += next_unique
        new_sonnet = new_sonnet[1:]

        new_gen += next_unique
        
    print("\n\n")
    return new_gen

if __name__ == '__main__':
    d=generate_sonnet().replace("\n\n","\n").split("\n")[1:15]
    d1=d.pop(0).split(" ")

    if(d1[0].lower()=='and' or d1[0].lower()=='but'):d1[0]="As"

    for i in([" ".join(d1).capitalize()]+d):
        print(i)


##########  attributions  ##############
## loosely based on theory on machinelearningmastery.com by Jason Brownlee