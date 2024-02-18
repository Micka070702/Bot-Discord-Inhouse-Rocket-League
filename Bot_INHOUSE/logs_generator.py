import random
import string

def generate_log():

    id_length = random.randint(5, 8)
    id_chars = string.ascii_letters + string.digits
    log_id = ''.join(random.choice(id_chars) for _ in range(id_length))

    password_length = random.randint(5, 8)
    password_chars = string.ascii_letters + string.digits
    log_password = ''.join(random.choice(password_chars) for _ in range(password_length))

    return str("ID: RLIH" + str(log_id) + "\nMDP: RLIH" + str(log_password))
