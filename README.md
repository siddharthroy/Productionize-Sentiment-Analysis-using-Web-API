# Productionize-Sentiment-Analysis-using-Web-API
- **Sentiment Analysis model** (CNN) is trained on corpus of labeled data. 
- Byte-Pair-Encoding (BPE) is used for tokenizing and embedding the user comment. 
- Trained model is "myCNN.hdf5" gave validation accuracy of 87%, and is 100MB in size hence couldn't be uploaded to GitHub.<br>
- Above model is converted to WSGI app using **Flask & Flask-restful**<br>
- To scale up the flask WSGI app and make production ready, **Waitress** is used
