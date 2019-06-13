from glob import glob
from code.data_preparation.data_divisor import create_training_data,create_test_data,create_validation_data

dog_filenames = glob('../../../../datasets/catsNdogs/train/dog*.jpg')
cat_filenames = glob('../../../../datasets/catsNdogs/train/cat*.jpg')

def create_datasets():
    print('creating training data....')
    create_training_data(dog_filenames,cat_filenames)
    print('creating test data....')
    create_test_data(dog_filenames,cat_filenames)
    print('creating validation data....')
    create_validation_data(dog_filenames,cat_filenames)

create_datasets()
