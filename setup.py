from setuptools import setup, find_packages


def parse_requirements(filename):

    result = []
    with open(filename, "r", encoding="utf-8") as f:

        for line in (line.strip() for line in f):

            if not line or line.startswith("#"):
                continue

            if line.startswith("-r"):
                _, filename = line.split(" ", 1)
                result.extend(parse_requirements(filename))
            else:
                result.append(line)

    return result


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="sqs-cli",
    version="0.0.1",
    author="Pavel Knyazev",
    author_email="poulix.nova@mail.ru",
    url="https://github.com/poul1x/sqs-cli",
    description="Command line interface to manage SQS instances",
    install_requires=parse_requirements("requirements-prod.txt"),
    entry_points={"console_scripts": ["sqscli=sqs_cli.app:main"]},
    packages=find_packages(exclude=["*tests*"]),
    long_description_content_type="text/markdown",
    long_description=long_description,
    python_requires=">=3.7",
)
