import os
import time
import tensorflow_hub as hub
from utils import*

#os.environ["TFHUB_DOWNLOAD_PROGRESS"] = "True"

# Declaring Constants
IMAGE_PATH = "C:\\Users\\tnwil\\Downloads\\CH12.13\\page_724.png"
SAVED_MODEL_PATH = "https://tfhub.dev/captain-pool/esrgan-tf2/1"

hr_image = utils.preprocess_image(IMAGE_PATH)

# Plotting Original Resolution image
utils.plot_image(tf.squeeze(hr_image), title="Original Image")
utils.save_image(tf.squeeze(hr_image), filename="Original Image")

model = hub.load(SAVED_MODEL_PATH)

start = time.time()
fake_image = model(hr_image)
fake_image = tf.squeeze(fake_image)
print("Time Taken: %f" % (time.time() - start))

# Plotting Super Resolution Image
utils.plot_image(tf.squeeze(fake_image), title="Super Resolution")
utils.save_image(tf.squeeze(fake_image), filename="Super Resolution")