class PostData:

    def __init__(self, **kwargs):
        self.userId = "1" if "userId" not in kwargs.keys() else kwargs['userId']
        self.id = "1" if "id" not in kwargs.keys() else kwargs['id']
        self.title = "sunt aut facere repellat provident occaecati excepturi optio reprehenderit" \
            if "title" not in kwargs.keys() else kwargs['title']
        self.body = "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut " \
                    "ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto" \
            if "body" not in kwargs.keys() else kwargs['body']

    @classmethod
    def from_json(cls, **kwargs):
        return cls(**kwargs)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    post_data = {'userId': 1, 'title': 'test title', 'body': 'test body'}
    updated_post_data = {'id': 1, 'userId': 1, 'title': 'updated title', 'body': 'updated body'}