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
    def getAlbum(paese):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT DISTINCT (a.Title) as album
                    from Album a 
                    join Track t on t.AlbumId = a.AlbumId 
                    JOIN InvoiceLine il on il.TrackId = t.TrackId 
                    join Invoice i on i.InvoiceId = il.InvoiceId 
                    JOIN Customer c on c.CustomerId = i.CustomerId 
                    WHERE  c.Country = %s"""

        cursor.execute(query, (paese,))

        for row in cursor:
            result.append(row["album"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getClienti(album, paese):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT DISTINCT (c.CustomerId) cliente
                    from Customer c 
                    JOIN Invoice i on i.CustomerId = c.CustomerId 
                    join InvoiceLine il on il.InvoiceId = i.InvoiceId 
                    join Track t on t.TrackId = il.TrackId 
                    join Album a on a.AlbumId = t.AlbumId 
                    WHERE  a.Title = %s and c.Country = %s"""

        cursor.execute(query, (album, paese))

        for row in cursor:
            result.append(row["cliente"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNumeroTracce(album):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select COUNT(t.Name) as numeroTracce 
                    from Track t 
                    join Album a on a.AlbumId = t.AlbumId 
                    where a.Title = %s"""

        cursor.execute(query, (album, ))

        for row in cursor:
            result.append(row["numeroTracce"])

        cursor.close()
        conn.close()
        return result