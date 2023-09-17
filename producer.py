import redis
from faker import Faker
from mongoengine import connect
from models import Contact  

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

connect('kioka') 

fake = Faker()
num_contacts = 10 

for _ in range(num_contacts):
    full_name = fake.name()
    email = fake.email()

    contact = Contact(full_name=full_name, email=email, sent_email=False)
    contact.save()

    redis_client.rpush('email_queue', str(contact.id))

print('succesfull')
