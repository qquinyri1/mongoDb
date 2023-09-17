import redis
from mongoengine import connect
from models import Contact 

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

connect('kioka')  

def send_email(contact_id):
    print(f"Отправлен email для контакта с ID: {contact_id}")

while True:
    contact_id = redis_client.lpop('email_queue')

    if contact_id:
        contact = Contact.objects(id=contact_id.decode()).first()

        if contact:
            send_email(contact_id.decode())

            contact.sent_email = True
            contact.save()
