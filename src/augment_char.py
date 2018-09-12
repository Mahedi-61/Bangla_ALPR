import os, random
import numpy as np 
import skimage.transform as tf
from scipy import ndarray, ndimage
from skimage import io, util
from PIL import Image
import PIL

# path variables and constant
from .. import root_dir
data_dir = root_dir.data_path()

# existing images
char_dir = "ko"
aug_crop_img_dir = os.path.join(data_dir, "aug_crop_char_img", char_dir)
all_crop_images = os.listdir(aug_crop_img_dir)

# new augmented images
aug_crop_img_dir_final = os.path.join(data_dir, "aug_crop_char_img_final")
work_folder = os.path.join(aug_crop_img_dir_final, char_dir)
os.makedirs(work_folder, exist_ok = True)


# functions 
def deformation(image):
    random_shear_angl = np.random.random() * np.pi/6 - np.pi/12
    random_rot_angl = np.random.random() * np.pi/7 - np.pi/12 - random_shear_angl
    random_x_scale = np.random.random() * .4 + .8
    random_y_scale = np.random.random() * .4 + .8
    random_x_trans = np.random.random() * image.shape[0] / 4 - image.shape[0] / 8
    random_y_trans = np.random.random() * image.shape[1] / 4 - image.shape[1] / 8

    dx = image.shape[0]/2. \
            - random_x_scale * image.shape[0]/2 * np.cos(random_rot_angl)\
            + random_y_scale * image.shape[1]/2 * np.sin(random_rot_angl + random_shear_angl)

    dy = image.shape[1]/2. \
            - random_x_scale * image.shape[0]/2 * np.sin(random_rot_angl)\
            - random_y_scale * image.shape[1]/2 * np.cos(random_rot_angl + random_shear_angl)

    trans_mat = tf.AffineTransform(rotation = random_rot_angl,
                                translation=(dx + random_x_trans,
                                                dy + random_y_trans),
                                shear = random_shear_angl,
                                scale = (random_x_scale,random_y_scale))


    return tf.warp(image, trans_mat.inverse,output_shape=image.shape) 



def image_deformation(image):
    tform = tf.SimilarityTransform(scale=1, rotation = np.random.random() * np.pi/12,
                               translation=(0, .1))
    
    return tf.warp(image, tform)



def random_rotation(image_array: ndarray):
    # pick a random degree of rotation between 25% on the left and 25% on the right
    random_degree = random.uniform(-12, 12)
    return tf.rotate(image_array, random_degree)


def random_noise(image_array: ndarray):
    # add random noise to the image
    return util.random_noise(image_array)


def blur(image_array: ndarray):
    # add random noise to the image
    return ndimage.gaussian_filter(image_array, sigma = 2)


def horizontal_flip(image_array: ndarray):
    # horizontal flip doesn't need skimage, it's easy as flipping the image array of pixels !
    return image_array[:, ::-1]


def vertical_flip(image_array: ndarray):
    # horizontal flip doesn't need skimage, it's easy as flipping the image array of pixels !
    return image_array[::-1, :]



def padding_small_image(img, size):
    width, height = img.size  # Pillow return images size as (w, h)

    if(width > height):
        new_width = size
        new_height = int(size * (height / width) + 0.5)

    else:
        new_height = size
        new_width = int(size * (width / height) + 0.5)

    #resize for keeping aspect ratio
    img_res = img.resize((new_width, new_height), resample = PIL.Image.BICUBIC)

    #Pad the borders to create a square image
    img_pad = Image.new("RGB", (size, size), (128, 128, 128))
    ulc = ((size - new_width) // 2, (size - new_height) // 2)
    img_pad.paste(img_res, ulc)

    return img_pad
    
    
def do_augment(image_path):
    for i, path in enumerate(image_path):
        img = io.imread(path)
        trans_img_n = random_noise(img)
        trans_img_r = random_rotation(img)
        trans_img_b = blur(img)
        trans_img_d = image_deformation(img)

        # write image to the disk
        new_image_path = os.path.join(work_folder, "b_" + all_crop_images[i])
        io.imsave(new_image_path, trans_img_b)

        new_image_path = os.path.join(work_folder, "n_" + all_crop_images[i])
        io.imsave(new_image_path, trans_img_n)

        new_image_path = os.path.join(work_folder, "r_" + all_crop_images[i])
        io.imsave(new_image_path, trans_img_r)

        new_image_path = os.path.join(work_folder, "d_" + all_crop_images[i])
        io.imsave(new_image_path, trans_img_d)


## main code here ##

# for go
image_path = [os.path.join(aug_crop_img_dir, path) for path in all_crop_images]

# for augmentation
do_augment(image_path)


# first resizing, padding and making it square shape with keeping aspect ration
all_aug_image_path = [os.path.join(work_folder, path) for path in os.listdir(work_folder)]


for img_path in all_aug_image_path:
    img = Image.open(img_path)
    resize_image = padding_small_image (img, 150)
    io.imsave(img_path, resize_image)
