from django.core.management.base import BaseCommand, CommandError
import psycopg2

hostname = 'localhost'
user = 'nex'
password = 'C1li2tn45!'
database = 'vers_linfinie'


class Command(BaseCommand):

    help = "Create some tables in the database"

    def handle(self, *args, **options):
        cmds = [
            """CREATE TABLE IF NOT EXISTS web_app_arts(id SERIAL PRIMARY KEY, title VARCHAR(255), txt TEXT,
             user_id INTEGER NOT NULL, foreign key (user_id) REFERENCES auth_user(id), date DATE NOT NULL)""",
            """CREATE TABLE IF NOT EXISTS web_app_favs(id SERIAL PRIMARY KEY, art_id INTEGER NOT NULL,
             foreign key (art_id) REFERENCES web_app_arts(id), user_id INTEGER NOT NULL, foreign key (user_id)
              REFERENCES auth_user(id))""",
            """CREATE TABLE IF NOT EXISTS web_app_comments(id SERIAL PRIMARY KEY, art_id INTEGER NOT NULL,
             foreign key (art_id) REFERENCES web_app_arts(id), user_id INTEGER NOT NULL, foreign key (user_id)
              REFERENCES auth_user(id), comments TEXT NOT NULL)"""]

        conn = None

        try:
            conn = psycopg2.connect(host=hostname, user=user, password=password, database=database)
            cur = conn.cursor()
            for tables in cmds:
                cur.execute(tables)
                print("Done")
            cur.close()
            conn.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

