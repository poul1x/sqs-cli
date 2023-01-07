#!/bin/sh

autoflake -r ./sqs_cli --remove-all-unused-imports -i
isort -q ./sqs_cli
black -q ./sqs_cli
