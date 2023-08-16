import argparse
import os, time
import tensorflow_hub as hub
from utils import*

#os.environ["TFHUB_DOWNLOAD_PROGRESS"] = "True"
PROCESS_PATH = os.getcwd() + "\processed"

# Declaring Constants
SAVED_MODEL_PATH = "https://tfhub.dev/captain-pool/esrgan-tf2/1"

def run(IMAGE_PATH: str):
    hr_image = utils.preprocess_image(IMAGE_PATH)

    # Plotting Original Resolution image
    #utils.plot_image(tf.squeeze(hr_image), title="Original Image")
    #utils.save_image(tf.squeeze(hr_image), filename="Original Image")
    model = hub.load(SAVED_MODEL_PATH)

    fake_image = model(hr_image)
    fake_image = tf.squeeze(fake_image)
    
    BASENAME = os.path.basename(IMAGE_PATH)
    NEWNAME = os.path.join(PROCESS_PATH, BASENAME)
    # Plotting Super Resolution Image
    #utils.plot_image(tf.squeeze(fake_image), title="Super Resolution")
    utils.save_image(tf.squeeze(fake_image), filename = NEWNAME)

def main():
    parser = argparse.ArgumentParser(description="SRGAN v1_2023.08.14")
    parser.add_argument("-path", type=str, help="Path to the images")
    args = parser.parse_args()

    if not os.path.exists(PROCESS_PATH):
        os.mkdir(PROCESS_PATH)

    n = 0
    for file_name in os.listdir(args.path):
        IMAGE_PATH = args.path
        full_path = os.path.join(IMAGE_PATH, file_name)
        if os.path.isfile(full_path) and full_path.endswith(".png"):
            n = n+1
    i = 1
    for file_name in os.listdir(args.path):
        IMAGE_PATH = args.path
        full_path = os.path.join(IMAGE_PATH, file_name)

        if os.path.isfile(full_path) and full_path.endswith(".png"):
            start = time.time()
            run(full_path)
            print ("[{}/{}] processed, ime taken: {}".format(i, n, (time.time() - start)))
            i = i + 1

if __name__ == "__main__":
    main()