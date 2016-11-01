import models

def getUser():
    user = models.User('zeopean1', 'zeopean1', 'zeopean@163.com', '1111111')
    models.mysqldb.session.add(user)
    models.mysqldb.session.commit()
    return True