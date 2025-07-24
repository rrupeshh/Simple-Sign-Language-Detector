# Sign Language Detector
A simple CNN project for detecting american sign language.
Here, I have implemented CNN (Convolution Neural Network) using Keras.

Complete Walkaround is covered in this blog:  [Building a Simple Sign Language Detector with CNN]([https://link-url-here.org](https://rupeshpoudel.com.np/blog/simple-sign-language-detector-cnn))


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
2. Now to test the model you just need to run recognise.py . To do so just open the terminal and run following command.
    ```
    python recognise.py
    ```
    Adjust the hsv values from the track bar to segment your hand color.

3. To create your own data set.
    ```
    python capture.py
    ```





