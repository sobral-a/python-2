import sys
from . import db
from . import todo_server


def start():
  args = sys.argv[1:]
  if len(args) > 0:
    if args [0] == 'show':
      print(db.find())

    if args[0] == 'create':
      print(db.create(str(args[1])))

    if args[0] == 'flag':
      db.toggle(args[1])

    if args[0] == 'remove':
      db.remove(args[1])
  else:
    server = todo_server.TodoServer()
    server.run()

start()