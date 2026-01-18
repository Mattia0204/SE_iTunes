from database.DB_connect import DBConnect
from model.connessione import Connessione


class DAO:
    @staticmethod
    def get_all_album():
        conn = DBConnect.get_connection()
        album = {}

        cursor = conn.cursor(dictionary=True)
        query = """
                SELECT album_id, (sum(milliseconds)/60000) AS durata
                FROM track 
                GROUP BY album_id 
                """
        cursor.execute(query)

        for row in cursor:
            album[row['album_id']] = row['durata']

        cursor.close()
        conn.close()
        return album

    @staticmethod
    def get_connessioni():
        conn = DBConnect.get_connection()
        connessioni = {}

        cursor = conn.cursor(dictionary=True)
        query = """
                select at1.album_id as a1, at2.album_id as a2
                from (select t1.album_id, pt1.playlist_id  
	                  from iTunes.track t1, iTunes.playlist_track pt1
	                  where pt1.track_id=t1.id) as at1,
	                 (select t2.album_id, pt2.playlist_id  
	                  from iTunes.track t2, iTunes.playlist_track pt2
	                  where pt2.track_id=t2.id) as at2
                      where at1.album_id!=at2.album_id and at1.playlist_id =at2.playlist_id  
                """
        cursor.execute(query)

        for row in cursor:
            a1 =row["a1"]
            a2 =row["a2"]

            if (a1,a2) not in connessioni:
                connessioni[a1,a2] = Connessione(a1, a2)

        cursor.close()
        conn.close()
        return connessioni

