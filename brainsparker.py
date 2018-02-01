"""
bot implementation.
"""
import os
import random

import pyCiscoSpark

# Sets config values from the config file
ACCESS_TOKEN_SPARK = "Bearer " + os.environ['access_token_spark']
FILEPATH = 'sparks.txt'


def random_line_from_file(file_name):
    """
    return random spark
    """

    afile = open(file_name)
    line = next(afile)
    for num, aline in enumerate(afile):
        if random.randrange(num + 2):
            continue
        line = aline
    return line


def post_sparks(event, context):
    """
    brainsparker
    """

    spark = random_line_from_file(FILEPATH)
    room_dict = pyCiscoSpark.get_rooms(ACCESS_TOKEN_SPARK)

    for room in room_dict['items']:
        print "Posting to " + room['title'] + " --- " + spark
        pyCiscoSpark.post_message_rich(ACCESS_TOKEN_SPARK, room['id'], spark)
