# Sign Language Detector
A simple CNN project for detecting american sign language.
Here, I have implemented CNN (Convolution Neural Network) using Keras.

### Tools Used
1. Python 3
2. OpenCV 3
3. Tensorflow
4. Keras

### Running this project
1. Install Python 3, Opencv 3, Tensorflow, Keras.
2. First Train the model.
    ```
    python cnn_model.py
    ```
2. Now to test the model with individual sign photos just run the test_model.py file. To do so just open the terminal and run following command.
    ```
    python test_model.py
    ```
    
3. To Test the model with your own hand, first run the file capture.py then place your hand in the green square and then press 'c' to        capture the individual picture. And in this code you can capture 5 pictures.
    ```
    python capture.py
    ```
    Then copy the pictures you just captured which is located in the same folder as capture.py and     place it in the folder named predicting_data.
    And run the following command
    ```
    python test_model.py
    ```




