class Meta:

    def __init__(self, status: str, errors: list, links: list):
        self.status: str = status
        self.errors: list = errors
        self.links: list = links

    def get_info(self):
        return {
            "status": self.status,
            "errors": self.errors,
            "links": self.links
        }

    def _check_status(self):
        pass
