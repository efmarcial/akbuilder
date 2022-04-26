import imp
from .models import *
import selenium
import beautifulsoup

# The only problem I see for now it that there are going to be duplicates later on.

def get_page():

    return 0

def save_database(image, customer):


    database_object = GalleryImage.objects.all()

    # Check if the database object is there
    if database_object.exists():

        # do something
        print("Already in database")

    # if doesnt exist then add to database
    else:

        database_object = GalleryImage(Image = image, Customer_name = customer)
        database_object.save()



    return 0

if __name__ == "__main__":
    get_page()