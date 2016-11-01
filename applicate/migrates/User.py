#encoding=utf-8
# from migrates import loader



class User(mysqldb.Model):

    id = mysqldb.Column(mysqldb.Integer , primary_key=True)
    username    = mysqldb.Column(mysqldb.String(255))
    nickname    = mysqldb.Column(mysqldb.String(255))
    email       = mysqldb.Column(mysqldb.String(32))
    password    = mysqldb.Column(mysqldb.String(32))

    def to_json(self):
        return {"username": self.username,
                "password": self.password}
    #当前用户是否被授权，因为我们登陆了就可以操作，所以默认都是被授权的
    def is_authenticated(self):
        return True

    #用于判断当前用户是否已经激活，已经激活的用户才能登陆
    def is_active(self):
        return True

    #用于判断当前用户是否是匿名用户，很明显，如果这个用户登陆了，就必须不是
    def is_anonymous(self):
        return False

    #获取改用户的唯一标示
    def get_id(self):
        return str(self.id)


# user = User.objects(username='zeopean' ,
#                     password='12').first()
# print user
#

