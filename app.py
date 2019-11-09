import os
from src.repository.mysql import Mysql
from src.repository.twitter import Twitter
from src.usecase.usecase import Usecase
from dotenv import load_dotenv


def start():
    try:
        mysql = Mysql(os.getenv("MYSQL_USER"), os.getenv("MYSQL_PASSWORD"),
                      os.getenv("MYSQL_DATABASE"), os.getenv("MYSQL_HOST"), os.getenv("MYSQL_PORT"))
        twitter = Twitter(os.getenv("CONSUMER_KEY"), os.getenv(
            "CONSUMER_KEY_SECRET"), os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))
    except Exception as e:
        print(e)
        exit(1)

    try:
        Usecase.do_crawling(twitter, mysql)
    except Exception as e:
        print(e)
        exit(1)


load_dotenv()
start()
