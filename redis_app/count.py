from flask import Flask
import redis 

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)

@app.route('/')
def welcome():
    return 'Welcome to the CoderCo containers challenge' 


@app.route('/count')
def counter():
    # Increment the counter in Redis
    count = r.incr('visits')
    return f'This page has been visited {count} times.'

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5002)