import os


class Usecase:

    @classmethod
    def do_crawling(cls, twitter, mysql):
        print(os.getenv("QUERY"))
        cursor = twitter.create_cursor(os.getenv("QUERY"))

        try:
            print("Start Crawling...")
            for tweet in twitter.limit_handled(cursor.items()):
                print(f"{tweet.id} -> {tweet.full_text} \n")
                mysql.insert_tweet(tweet.id, tweet.full_text)
        except StopIteration:
            print("Done, exit process...")
        except KeyboardInterrupt:
            print("Stop Crawling...")
        except Exception as e:
            raise Exception(e)
