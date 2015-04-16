import ujson as json

import tornado.ioloop
import tornado.web

DB = {'1': {'name': 'test', 'description': 'test description'}}

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
            self.send_error(status_code=400, reason="No To-do item with ID {}".format(item_id))
        else:
            self.finish(DB.get(item_id))

    def put(self, item_id):
        item_id = str(item_id)
        item_data = json.loads(self.request.body)
        item = DB.get(item_id)
        if not item:
            self.send_error(status_code=400, reason="No To-do item with ID {}".format(item_id))
        else:
            DB[item_id] = {'name': item_data['name'], 'description': item_data['description']}
            self.finish(DB.get(item_id))

    def delete(self, item_id):
        item_id = str(item_id)
        item = DB.get(item_id)
        if not item:
            self.send_error(status_code=400, reason="No To-do item with ID {}".format(item_id))
        else:
            self.write("{} deleted".format(item_id))


application = tornado.web.Application([
    (r"/api/todo/(\d+)", ItemHandler),
    (r"/api/todo/", IndexHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
