from mongoengine import connect


def create_connect():
    connect('your_database_name_here', host='mongodb+srv://kioka:HokageE2222@kioka.stvxvxr.mongodb.net')