import os
import sys
from typing import Callable, Dict, Type

from sqs_cli.app import output
from sqs_cli.app.commands import profiles
from sqs_cli.app.errors import BadParameterError, CLIError
from sqs_cli.app.utils import APP_DIR
from .models import AppContext

# from .toolkit import queues
from .models import Verbosity, OutputMode

import typer

########################################
# Client CLI
########################################

ExceptionType = Type[Exception]
ExceptionHandler = Callable[[Exception], int]


class EnhancedTyper(typer.Typer):

    _error_handlers: Dict[ExceptionType, ExceptionHandler] = {}

    def error_handler(self, e: ExceptionType):
        def decorator(handler: ExceptionHandler):
            self._error_handlers[e] = handler
            return handler

        return decorator

    def __call__(self, *args, **kwargs):
        try:
            return super().__call__(*args, **kwargs)
        except Exception as e:
            try:
                callback = self._error_handlers[type(e)]
                sys.exit(callback(e))
            except KeyError:
                raise


sqscli = EnhancedTyper(
    name="sqs_cli",
    help="Command line interface to manage SQS instances",
)

sqscli.add_typer(profiles.app)


@sqscli.callback()
def common_options(
    ctx: typer.Context,
    verbosity: str = typer.Option(
        Verbosity.none.value,
        "-v",
        "--verbosity",
        help="Enable logging output. Usually used for debugging",
        autocompletion=lambda: [e.value for e in Verbosity],
        metavar=f"[{'|'.join([e.value for e in Verbosity])}]",
    ),
    output_mode: str = typer.Option(
        OutputMode.human.value,
        "-o",
        "--output-mode",
        help="Choose an output mode. Human-readable by default",
        autocompletion=lambda: [e.value for e in OutputMode],
        metavar=f"[{'|'.join([e.value for e in OutputMode])}]",
    ),
    silent: bool = typer.Option(
        False,
        "-s",
        "--silent",
        help="Show only result of operation and suppress any other output",
    ),
    auto_approve: bool = typer.Option(
        False,
        "-y",
        "--yes",
        help="Automatic 'yes', if set. No prompts with 'y/n' will be shown",
    ),
):
    os.makedirs(APP_DIR, exist_ok=True)

    ctx.obj = AppContext(
        verbosity=verbosity,
        output_mode=output_mode,
        auto_approve=auto_approve,
        silent=silent,
    )

@sqscli.error_handler(BadParameterError)
def handle_bad_parameter(e: BadParameterError):
    output.bad_parameters(e)
    return 1

@sqscli.error_handler(CLIError)
def handle_bad_parameter(e: CLIError):
    output.error(str(e))
    return 1