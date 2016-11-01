#encoding=utf-8
from flask_script import Manager
from app import app
from flask_script.commands import ShowUrls

manager = Manager(app)
manager.add_option('-c','--config',dest="mode",required=False)


manager.add_command("showurls",ShowUrls)

if __name__ == '__main__':
    manager.run()