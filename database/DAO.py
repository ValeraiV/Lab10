from database.DB_connect import DBConnect
from model.country import Country
from model.border import Border

class DAO():

    @staticmethod
    def getAllCountries(year):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select co.StateAbb, co.CCode, co.StateNme
                    from contiguity c, country co
                    where c.`year` <= %s
                    and c.state1no = co.CCode
                    group by c.state1no order by StateAbb"""

        cursor.execute(query, (year, ))

        for row in cursor:
            result.append(Country(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getCountryPairs(idMap, year):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary= True)
        query = """select state1no, state2no
                    from contiguity c
                    where c.conttype=1 and c.`year` <= %s""" #conttype=1 == raggiungibile via terra

        cursor.execute(query, (year, ))

        for row in cursor:
            c1 = idMap[row["state1no"]]
            c2 = idMap[row["state2no"]]

            if c1 is not None and c2 is not None:
                result.append(Border(c1, c2))

        cursor.close()
        conn.close()
        return result
