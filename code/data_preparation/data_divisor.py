import shutil
import os

TRAINING_BASE_DIR = "../../../../datasets/catsNdogs/training_data/"
CAT_TRAINING_DIR = "../../../../datasets/catsNdogs/training_data/cat/"
DOG_TRAINING_DIR = "../../../../datasets/catsNdogs/training_data/dog/"
TEST_BASE_DIR = "../../../../datasets/catsNdogs/test_data/"
CAT_TEST_DIR = "../../../../datasets/catsNdogs/test_data/cat/"
DOG_TEST_DIR = "../../../../datasets/catsNdogs/test_data/dog/"
VALIDATION_BASE_DIR = "../../../../datasets/catsNdogs/validation_data/"
CAT_VALIDATION_DIR = "../../../../datasets/catsNdogs/validation_data/cat/"
DOG_VALIDATION_DIR = "../../../../datasets/catsNdogs/validation_data/dog/"


def create_training_data(dog_filenames,cat_filenames):
    dog_filenames = dog_filenames[0:1000]
    cat_filenames = cat_filenames[0:1000]
    checkAndCreateDirectory(TRAINING_BASE_DIR)
    checkAndCreateDirectory(CAT_TRAINING_DIR)
    checkAndCreateDirectory(DOG_TRAINING_DIR)
    for i,dog_filename in enumerate(dog_filenames):
        shutil.copyfile(dog_filenames[i],DOG_TRAINING_DIR + "dog"+ str(i) + ".jpg")
        shutil.copyfile(cat_filenames[i],CAT_TRAINING_DIR + "cat"+ str(i) + ".jpg")


def create_test_data(dog_filenames,cat_filenames):
    dog_filenames = dog_filenames[1000:1500]
    cat_filenames = cat_filenames[1000:1500]
    checkAndCreateDirectory(TEST_BASE_DIR)
    checkAndCreateDirectory(CAT_TEST_DIR)
    checkAndCreateDirectory(DOG_TEST_DIR)
    for i, dog_filename in enumerate(dog_filenames):
        shutil.copyfile(dog_filenames[i], DOG_TEST_DIR + "dog"+ str(i) + ".jpg")
        shutil.copyfile(cat_filenames[i], CAT_TEST_DIR + "cat"+ str(i) + ".jpg")

def create_validation_data(dog_filenames,cat_filenames):
    dog_filenames = dog_filenames[1500:2000]
    cat_filenames = cat_filenames[1500:2000]
    checkAndCreateDirectory(VALIDATION_BASE_DIR)
    checkAndCreateDirectory(CAT_VALIDATION_DIR)
    checkAndCreateDirectory(DOG_VALIDATION_DIR)
    for i, dog_filename in enumerate(dog_filenames):
        shutil.copyfile(dog_filenames[i], DOG_VALIDATION_DIR + "dog"+ str(i) + ".jpg")
        shutil.copyfile(cat_filenames[i], CAT_VALIDATION_DIR + "cat"+ str(i) + ".jpg")


def checkAndCreateDirectory(path):
    if os.path.exists(path):
        return
    else:
        os.makedirs(path)





