#!/usr/bin/python3
""""UTF-8 Validation"""


def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    :param data: List of integers representing the data bytes
    :return: True if data is a valid UTF-8 encoding, else return False
    """
    num_bytes_to_follow = 0

    for byte in data:
        # Check if the current byte is a continuation byte
        if num_bytes_to_follow:
            # If the byte doesn't start with '10', it's not a valid continuation byte
            if (byte >> 6) != 0b10:
                return False
            num_bytes_to_follow -= 1
        else:
            # Count the number of bytes to follow based on the leading bits
            if (byte >> 7) == 0b0:
                num_bytes_to_follow = 0
            elif (byte >> 5) == 0b110:
                num_bytes_to_follow = 1
            elif (byte >> 4) == 0b1110:
                num_bytes_to_follow = 2
            elif (byte >> 3) == 0b11110:
                num_bytes_to_follow = 3
            else:
                return False

    # If there are still bytes expected, it's not a valid encoding
    return num_bytes_to_follow == 0
