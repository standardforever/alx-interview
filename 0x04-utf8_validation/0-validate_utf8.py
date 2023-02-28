#!/usr/bin/python3
"""UTF-8 validation
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data: A list of integers representing bytes of data.

    Returns:
        True if data is a valid UTF-8 encoding, else return False.
    """
    """ Initialize a count of the number of bytes
     remaining in the current character.
     """
    remaining_bytes = 0

    """ Iterate over each byte in the data set.
    """
    for byte in data:
        """ If there are bytes remaining in the current character,
        then this byte should be a continuation byte.
        """
        if remaining_bytes > 0:
            """ Check that the high bit of this byte is set and the second
            highest bit is not set, indicating that
            this is a continuation byte.
            """
            if (byte & 0b11000000) != 0b10000000:
                return False
            remaining_bytes -= 1
        else:
            """ Otherwise, this byte should be the start of a new character.
            Count the number of high bits set
            in the byte to determine how many bytes are in the character.
            """
            if (byte & 0b10000000) == 0:
                remaining_bytes = 0
            elif (byte & 0b11100000) == 0b11000000:
                remaining_bytes = 1
            elif (byte & 0b11110000) == 0b11100000:
                remaining_bytes = 2
            elif (byte & 0b11111000) == 0b11110000:
                remaining_bytes = 3
            else:
                return False

    """ If we've iterated over all bytes and there are no remaining bytes in
    the current character, then the
    data is a valid UTF-8 encoding.
    """
    return remaining_bytes == 0
