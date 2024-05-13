import argparse
import sqlalchemy
from tqdm import tqdm
import random
import string

# Setup command line argument parsing
parser = argparse.ArgumentParser(description="Load data into the database")
parser.add_argument('--db', required=True) 
parser.add_argument('--num_rows',type=int, default=100)
args = parser.parse_args()

# Database connection setup
engine = sqlalchemy.create_engine(args.db)
connection = engine.connect()

def read_words(file_path='dictionary.txt'):
    with open(file_path, 'r') as file:
        words = file.read().split()
    random.shuffle(words)
    return words

word_list = read_words()

# Generate and insert users
def generate_users(num_users):
    for i in tqdm(range(num_users), desc="Generating Users"):
        username = ''.join(random.choices(string.ascii_letters, k=8))
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
        age = random.randint(18, 80)
        sql = sqlalchemy.sql.text("""
        INSERT INTO users (username, password, age) VALUES (:u, :p, :a);
        """)
        try:
            connection.execute(sql, {'u': username, 'p': password, 'a': age})
        except sqlalchemy.exc.IntegrityError as e:
            print("Failed to insert user {}: {}".format(i, e))

# Generate and insert URLs
def generate_urls(num_urls):
    for i in tqdm(range(num_urls), desc="Generating URLs"):
        url = 'https://' + ''.join(random.choices(string.ascii_lowercase, k=10)) + '.com'
        sql = sqlalchemy.sql.text("""
        INSERT INTO urls (url) VALUES (:url);
        """)
        try:
            connection.execute(sql, {'url': url})
        except sqlalchemy.exc.IntegrityError as e:
            print("Failed to insert url {}: {}".format(i, e))

# Generate and insert messages
def generate_messages(num_messages):
    user_ids = [row[0] for row in connection.execute("SELECT id FROM users;").fetchall()]
    url_ids = [row[0] for row in connection.execute("SELECT id_urls FROM urls;").fetchall()] 
    for i in tqdm(range(num_messages), desc="Generating Messages"):
        sender_id = random.choice(user_ids)
        message = ' '.join(random.sample(word_list, 10))
        url_id = random.choice(url_ids)
        sql = "INSERT INTO messages (sender_id, message, id_urls) VALUES (%s, %s, %s);"
        try:
            connection.execute(sql, (sender_id, message, url_id))
        except sqlalchemy.exc.IntegrityError as e:
            print("Failed to insert message {}: {}".format(i, e))

generate_users(args.num_rows)
generate_urls(args.num_rows)
generate_messages(10 * args.num_rows)

connection.close()
