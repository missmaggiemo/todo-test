import ujson as json

import tornado.ioloop
import tornado.web

DB = {'1': {'name': 'test', 'description': 'test description'}}

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("app.html")


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.finish(DB)

    def post(self):
        item_data = json.loads(self.request.body)
        next_id = max([int(k) for k in DB.keys]) + 1
        DB[str(next_id)] = {'name': item_data['name'], 'description': item_data['description']}
        self.finish(DB)


class ItemHandler(tornado.web.RequestHandler):
    def get(self, item_id):
        item_id = str(item_id)
        item = DB.get(item_id)
        print item
        if not item:
            self.set_status(400)
            self.finish("No To-do item with ID {}".format(item_id))
        else:
            self.finish(DB.get(item_id))

    def put(self, item_id):
        item_id = str(item_id)
        item_data = json.loads(self.request.body)
        item = DB.get(item_id)
        if not item:
            self.set_status(400)
            self.finish("No To-do item with ID {}".format(item_id))
        else:
            DB[item_id] = {'name': item_data['name'], 'description': item_data['description']}
            self.finish(DB.get(item_id))

    def delete(self, item_id):
        item_id = str(item_id)
        item = DB.get(item_id)
        if not item:
            self.set_status(400)
            self.finish("No To-do item with ID {}".format(item_id))
        else:
            self.write("{} deleted".format(item_id))


application = tornado.web.Application([
    ("/", MainHandler),
    (r"/api/todo/(\d+)", ItemHandler),
    (r"/api/todo/", IndexHandler),
])

if __name__ == "__main__":
    print "Why hello there! I'm starting a server on port 8888..."
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
