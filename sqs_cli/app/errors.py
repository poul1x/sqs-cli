
class CLIError(Exception):
    """Base exception for all errors of SQS CLI"""

class InternalError(CLIError):
    def __init__(self) -> None:
        super().__init__(
            "Internal error occurred. Possibly, bug in client or API server\n"
            "Please, contact support service to resolve the issue"
        )

class CommandFailed(CLIError):
    pass

class BadParameterError(CLIError):
    def __init__(self, ctx, msg: str, *params: str) -> None:
        super().__init__(msg)
        self.params = params
        self.ctx = ctx