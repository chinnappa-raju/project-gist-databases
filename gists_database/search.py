from .models import Gist

def search_gists(db_connection, **kwargs):
    sql = "select * from gists"
    if len(kwargs) > 0:
        sql+=" where "
    for key in kwargs.keys():
        if key == 'created_at':
            sql+= " datetime({}) = datetime(:{}) ".format(key, key)
        else:
            sql+= " {} = :{}".format(key, key)
    cursor = db_connection.execute(sql, kwargs)
    gists = cursor.fetchall()
    return [Gist(row) for row in gists]