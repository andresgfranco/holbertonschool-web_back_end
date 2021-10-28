#!/usr/bin/env python3
"""This module contais the filter_datum function"""


from typing import List
import re
import logging
import mysql.connector
import os


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """the RedactingFormatter Constructor"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.__fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ filters values in incoming log records using filter_datum """
        record_formatted = logging.Formatter(self.FORMAT).format(record)
        return filter_datum(
            self.__fields, self.REDACTION, record_formatted, self.SEPARATOR
        )


def filter_datum(
    fields: List[str], redaction: str,
    message: str, separator: str
) -> str:
    """returns the log message obfuscated"""
    redaction += separator
    regex_str = "=[\\s\\S]*?;"
    for i in fields:
        message = re.sub(i + regex_str, i + "=" + redaction, message)
    return message


def get_logger() -> logging.Logger:
    """returns a logging.Logger object"""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    formatter = RedactingFormatter(list(PII_FIELDS))

    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """returns a connector to the database"""
    return mysql.connector.connection.MySQLConnection(
        user=os.getenv("PERSONAL_DATA_DB_USERNAME", "root"),
        password=os.getenv("PERSONAL_DATA_DB_PASSWORD", ""),
        database=os.getenv("PERSONAL_DATA_DB_NAME"),
        host=os.getenv("PERSONAL_DATA_DB_HOST")
    )


def main():
    """the main function"""
    con = get_db()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM users;")

    new_logger = get_logger()

    for row in cursor:
        row_format = "name={}; email={}; phone={}; ssn={}; password={}; \
            ip={}; last_login={}; user_agent={}; ".format(
                row[0], row[1], row[2], row[3],
                row[4], row[5], row[6], row[7]
            )

        row_format = filter_datum(
            list(PII_FIELDS),
            '***',
            format_message,
            '; '
        )

        new_logger.info(row_format)

    cursor.close()
    con.close()


if __name__ == '__main__':
    main()
