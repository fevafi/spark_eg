docker-compose up;

docker exec -it da7ea45f680579ca30e8ad7c9af6c8ebbcda53d67dccb7218a7848e0dc634707 bash;

spark-submit /code/wordcount.py /data/logs.txt;