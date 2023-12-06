# flasky
A minimal docker image with exposed port running flask

## run
```bash
docker build --tag host --file Dockerfile .
docker run -p 8000:5000 -d -t --name flasky host
curl 'http://localhost:8000/is_prime?number=17' 
17 is prime # <--- expected
```
