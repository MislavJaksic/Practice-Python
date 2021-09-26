"""
    practice-python.py
    ------------------

    Runs the project.

    :copyrgiht: 2019 MislavJaksic
    :license: MIT License
"""
import sys

from loguru import logger

log_message = "who={username}, what={object}/{status}, where={system}/{application}/{component}/{source}, when={timestamp}/{timezone}, why={reason}, how={action}"


def main(args):
    """main() will be run if you run this script directly"""
    x = 2
    y = 7

    logger.info(
        log_message,
        username="1",
        object="2",
        status="3",
        system="4",
        application="5",
        component="6",
        source="7",
        timestamp="8",
        timezone="9",
        reason="10",
        action="11",
    )


def run():
    """Entry point for the runnable script."""
    sys.exit(main(sys.argv[1:]))


if __name__ == "__main__":
    """main calls run()."""
    run()
