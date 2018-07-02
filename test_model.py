from keras.models import load_model

classifier = load_model('Trained_model.h5')


#Prediction of single image
import numpy as np
from keras.preprocessing import image
img_name = input('Enter Image Name: ')
image_path = './predicting_data/{}'.format(img_name)
print('')

test_image = image.load_img(image_path, target_size=(200, 200))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict(test_image)
#training_set.class_indices
print('Predicted Sign is:')
print('')
if result[0][0] == 1:
       print('P')
elif result[0][1] == 1:
       print('Y')
elif result[0][2] == 1:
       print('Cool')
elif result[0][3] == 1:
       print('Five')
else:
       print('Like')

