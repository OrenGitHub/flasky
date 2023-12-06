from flask import Flask
from flask import request

app = Flask(__name__)

def prime(p: int) -> bool:
    for i in range(2, p):
        for j in range(2,p):
            if i*j == p:
                return False;
    return True;

@app.route('/is_prime')
def hello_world():
    p: int = request.args.get('number')
    if p is not None:
        p_is_prime: bool = prime(int(p))
        if p_is_prime:
            return f'{p} is prime\n'
        else:
            return f'{p} is not prime\n'
    return 'missing input number'

