class ResourceNotFoundError(Exception):

    def __init__(self, message: str):
        self.message = message

    def as_json_dict(self):
        return {
            "404": self.message
        }
