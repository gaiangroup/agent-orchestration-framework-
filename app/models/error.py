class Error:
    def __init__(self, http_status: int, error_code: int, message: str, root_message: str):
        self.http_status = http_status
        self.error_code = error_code
        self.message = message
        self.root_message = root_message

    def to_dict(self):
        return {
            "error_code": self.error_code,
            "message": self.message,
            "root_message": self.root_message,
        }
