from database.DB_connect import DBConnect


class DAO():
    @staticmethod
    def getPaese():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT DISTINCT (c.Country) as paesi
                    from Customer c """

        cursor.execute(query)

        for row in cursor:
            result.append(row["paesi"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getArtisti(genere):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT DISTINCT a.Name as nomiArtisti
                    FROM Genre g
                    JOIN Track t ON t.GenreId = g.GenreId
                    JOIN Album al ON al.AlbumId = t.AlbumId
                    JOIN Artist a ON a.ArtistId = al.ArtistId
                    WHERE g.Name = %s"""

        cursor.execute(query, (genere,))

        for row in cursor:
            result.append(row["nomiArtisti"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getClienti(artista, genere):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT DISTINCT i.CustomerId as cliente
                    FROM Artist a 
                    JOIN Album al on al.ArtistId = a.ArtistId 
                    join Track t on t.AlbumId = al.AlbumId 
                    join InvoiceLine il on il.TrackId = t.TrackId 
                    join Invoice i on i.InvoiceId = il.InvoiceId 
                    join Genre g on g.GenreId = t.GenreId 
                    WHERE a.Name  = %s 
                    and g.Name = %s"""

        cursor.execute(query, (artista, genere))

        for row in cursor:
            result.append(row["cliente"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNumeroTracce(artista, genere):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT  COUNT( t.TrackId) as numeroTracce
                    FROM Artist a
                    JOIN Album al on al.ArtistId = a.ArtistId
                    join Track t on t.AlbumId = al.AlbumId
                    join InvoiceLine il on il.TrackId = t.TrackId
                    join Genre g on g.GenreId = t.GenreId
                    WHERE a.Name  = %s
                    and g.Name = %s"""

        cursor.execute(query, (artista, genere))

        for row in cursor:
            result.append(row["numeroTracce"])

        cursor.close()
        conn.close()
        return result