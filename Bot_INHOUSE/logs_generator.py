import random
import string

def generate_log():

    id_length = 2
    id_chars = string.digits
    log_id = ''.join(random.choice(id_chars) for _ in range(id_length))

    password_length = 3
    password_chars = string.digits
    log_password = ''.join(random.choice(password_chars) for _ in range(password_length))

    return str("ID: IH" + str(log_id) + "\nMDP: IH" + str(log_password))
