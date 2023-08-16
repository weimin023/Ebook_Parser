import argparse
import os, time
import tensorflow_hub as hub
from utils import*

from PIL import Image
from io import BytesIO

#os.environ["TFHUB_DOWNLOAD_PROGRESS"] = "True"


# Declaring Constants
SAVED_MODEL_PATH = "https://tfhub.dev/captain-pool/esrgan-tf2/1"
IMG_FORMAT = 'png'

def run(IMAGE_PATH: str, WORK_PATH: str):
        hr_image = utils.preprocess_image(IMAGE_PATH)

        # Plotting Original Resolution image
        #utils.plot_image(tf.squeeze(hr_image), title="Original Image")
        #utils.save_image(tf.squeeze(hr_image), filename="Original Image")
        model = hub.load(SAVED_MODEL_PATH)

        fake_image = model(hr_image)
        fake_image = tf.squeeze(fake_image)
        
        BASENAME = os.path.basename(IMAGE_PATH)
        NEWNAME = os.path.join(os.path.join(WORK_PATH, "processed"), BASENAME)
        # Plotting Super Resolution Image
        #utils.plot_image(tf.squeeze(fake_image), title="Super Resolution")
        utils.save_image(tf.squeeze(fake_image), filename = NEWNAME)

def main():
    parser = argparse.ArgumentParser(description="SRGAN v1_2023.08.14")
    parser.add_argument("-path", type=str, help="Path to the images")
    parser.add_argument("-sr", type=bool, help="Image super resolution")
    parser.add_argument("-compress", type=bool, help="Image size compression")
    args = parser.parse_args()

    PROCESS_PATH = os.path.join(args.path, "processed")

    if not args.path:
        print ("ERROR: Check Options.")
        return
    
    if not os.path.exists(PROCESS_PATH):
        os.mkdir(PROCESS_PATH)

    n = 0
    for file_name in os.listdir(args.path):
        IMAGE_PATH = args.path
        full_path = os.path.join(IMAGE_PATH, file_name)
        if os.path.isfile(full_path) and full_path.endswith("." + IMG_FORMAT):
            n = n + 1

    if args.sr:
        i = 1
        for file_name in os.listdir(args.path):
            IMAGE_PATH = args.path
            full_path = os.path.join(IMAGE_PATH, file_name)
            
            if os.path.isfile(full_path) and full_path.endswith("." + IMG_FORMAT):
                start = time.time()
                run(full_path, IMAGE_PATH)
                print ("[{}/{}] processed, time taken: {}".format(i, n, (time.time() - start)))
                i = i + 1
            

    if args.compress:
        imglist = []
        i = 1
        for file in os.listdir(PROCESS_PATH):
            if file.endswith("." + IMG_FORMAT):
                out = BytesIO()
                im = Image.open(os.path.join(PROCESS_PATH, file))
                im.save(out, format='png', optimize=True, quality=85)
                imglist.append(out.getvalue())
                
                print ("[{}/{}] {} compressed.".format(i, n, file))
                i = i + 1

        p1 = Image.open(BytesIO(imglist[0]))
        others = [Image.open(BytesIO(img)) for img in imglist[1:]]
        p1.save(os.path.join(PROCESS_PATH, 'result.pdf'), save_all=True, append_images=others)


    

if __name__ == "__main__":
    main()