class Answer:

    def __init__(self, status: int, errors: str, data: list):
        self.status: int = status
        self.errors: str = errors
        self.data: list = data

    def get_info(self):
        return {
            "status": self.status,
            "errors": self.errors,
            "data": self.data
        }
