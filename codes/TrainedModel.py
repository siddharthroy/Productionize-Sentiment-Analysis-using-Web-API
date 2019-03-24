from keras.models import load_model
from keras.preprocessing import sequence
from bpemb import BPEmb
import numpy as np

myModel = load_model("myCNN.hdf5")
myModel._make_predict_function()     # initialize before threading, s.t. myModel.predict() can work when called from different thread like flask
bpemb_en = BPEmb(lang="en", vs=50000, dim=300)


def is_comment_good(input_comment):
    tokenised = bpemb_en.encode_ids(input_comment)
    padded_comment = sequence.pad_sequences([tokenised], maxlen=800, padding='post', truncating='post')
    devices = np.array([0, 0, 1, 0, 0, 0, 1, 0, 0], ndmin=2)     # 6 browser + 3 device
    
    
    pred_prob = myModel.predict([padded_comment, devices ] )
    
    pred = pred_prob>0.5
    return(np.squeeze(pred))    # is the user-comment good?


if __name__ == "__main__":
    input_comment = input("Input your comment: ")
    print(is_comment_good(input_comment))
