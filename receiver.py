import socket

# Create a socket
print("Creating a socket")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(1)
print("Done")
# Connect to the remote host and port
print("Connecting to remote host...")
sock.connect(("10.40.0.6", 4196))
print("Done")

encondings = [
    "ascii",
    # "big5",
    # "big5hkscs",
    # "cp037",
    # "cp273",
    # "cp424",
    # "cp437",
    # "cp500",
    # "cp720",
    # "cp737",
    # "cp775",
    # "cp850",
    # "cp852",
    # "cp855",
    # "cp856",
    # "cp857",
    # "cp858",
    # "cp860",
    # "cp861",
    # "cp862",
    # "cp863",
    # "cp864",
    # "cp865",
    # "cp866",
    # "cp869",
    # "cp874",
    # "cp875",
    # "cp932",
    # "cp949",
    # "cp950",
    # "cp1006",
    # "cp1026",
    # "cp1125",
    # "cp1140",
    # "cp1250",
    # "cp1251",
    # "cp1252",
    # "cp1253",
    # "cp1254",
    # "cp1255",
    # "cp1256",
    # "cp1257",
    # "cp1258",
    # "euc_jp",
    # "euc_jis_2004",
    # "euc_jisx0213",
    # "euc_kr",
    # "gb2312",
    # "gbk",
    # "gb18030",
    # "hz",
    # "iso2022_jp",
    # "iso2022_jp_1",
    # "iso2022_jp_2",
    # "iso2022_jp_2004",
    # "iso2022_jp_3",
    # "iso2022_jp_ext",
    # "iso2022_kr",
    # "latin_1",
    # "iso8859_2",
    # "iso8859_3",
    # "iso8859_4",
    # "iso8859_5",
    # "iso8859_6",
    # "iso8859_7",
    # "iso8859_8",
    # "iso8859_9",
    # "iso8859_10",
    # "iso8859_11",
    # "iso8859_13",
    # "iso8859_14",
    # "iso8859_15",
    # "iso8859_16",
    # "johab",
    # "koi8_r",
    # "koi8_t",
    # "koi8_u",
    # "kz1048",
    # "mac_cyrillic",
    # "mac_greek",
    # "mac_iceland",
    # "mac_latin2",
    # "mac_roman",
    # "mac_turkish",
    # "ptcp154",
    # "shift_jis",
    # "shift_jis_2004",
    # "shift_jisx0213",
    # "utf_32",
    # "utf_32_be",
    # "utf_32_le",
    # "utf_16",
    # "utf_16_be",
    # "utf_16_le",
    # "utf_7",
    # "utf_8",
    # "utf_8_sig",
]

repetitions = 0

while True:
    try:
        # Get the host's response, no more than, say, 1,024 bytes
        # print("Receiving data from host...")
        response_data = sock.recv(2049)
        response_string: list[tuple[str, str]] = []
        # response_data_reversed: bytes = response_data[::-1]
        # response_data_byte_transformed1: bytes = b""
        # response_data_reversed_byte_transformed1: bytes = b""
        # response_data_byte_transformed2: bytes = b""
        # response_data_reversed_byte_transformed2: bytes = b""
        # response_data_inverted: bytes = b""

        def byte_to_bit_list(value: int) -> list[int]:
            bit_array = [0] * 8
            for i in range(8):
                bit_array[7 - i] = (value >> i) & 1
            return bit_array

        def bit_list_to_byte(bit_array: list[int]) -> int:
            value = 0
            for i in range(8):
                value |= bit_array[7 - i] << i
            return value

        # for byte in response_data:
        #     bits = byte_to_bit_list(byte)
        #     transformed_bit_array = [0] * 8
        #     transformed_bit_array[0] = bits[7]
        #     transformed_bit_array[1] = bits[6]
        #     transformed_bit_array[2] = bits[5]
        #     transformed_bit_array[3] = bits[4]
        #     transformed_bit_array[4] = bits[3]
        #     transformed_bit_array[5] = bits[2]
        #     transformed_bit_array[6] = bits[1]
        #     transformed_bit_array[7] = bits[0]
        #     transformed_byte = bit_list_to_byte(transformed_bit_array)
        #     response_data_byte_transformed1 += bytes([transformed_byte])

        # for byte in response_data_reversed:
        #     bits = byte_to_bit_list(byte)
        #     transformed_bit_array = [0] * 8
        #     transformed_bit_array[0] = bits[7]
        #     transformed_bit_array[1] = bits[6]
        #     transformed_bit_array[2] = bits[5]
        #     transformed_bit_array[3] = bits[4]
        #     transformed_bit_array[4] = bits[3]
        #     transformed_bit_array[5] = bits[2]
        #     transformed_bit_array[6] = bits[1]
        #     transformed_bit_array[7] = bits[0]
        #     transformed_byte = bit_list_to_byte(transformed_bit_array)
        #     response_data_reversed_byte_transformed1 += bytes(
        #         [transformed_byte]
        #     )

        # for byte in response_data:
        #     bits = byte_to_bit_list(byte)
        #     transformed_bit_array = [0] * 8
        #     transformed_bit_array[0] = bits[3]
        #     transformed_bit_array[1] = bits[2]
        #     transformed_bit_array[2] = bits[1]
        #     transformed_bit_array[3] = bits[0]
        #     transformed_bit_array[4] = bits[7]
        #     transformed_bit_array[5] = bits[6]
        #     transformed_bit_array[6] = bits[5]
        #     transformed_bit_array[7] = bits[4]
        #     transformed_byte = bit_list_to_byte(transformed_bit_array)
        #     response_data_byte_transformed2 += bytes([transformed_byte])

        # for byte in response_data_reversed:
        #     bits = byte_to_bit_list(byte)
        #     transformed_bit_array = [0] * 8
        #     transformed_bit_array[0] = bits[3]
        #     transformed_bit_array[1] = bits[2]
        #     transformed_bit_array[2] = bits[1]
        #     transformed_bit_array[3] = bits[0]
        #     transformed_bit_array[4] = bits[7]
        #     transformed_bit_array[5] = bits[6]
        #     transformed_bit_array[6] = bits[5]
        #     transformed_bit_array[7] = bits[4]
        #     transformed_byte = bit_list_to_byte(transformed_bit_array)
        #     response_data_reversed_byte_transformed2 += bytes(
        #         [transformed_byte]
        #     )

        # for byte in response_data:
        #     bits = byte_to_bit_list(byte)
        #     transformed_bit_array = [0] * 8
        #     transformed_bit_array[0] = not bits[0]
        #     transformed_bit_array[1] = not bits[1]
        #     transformed_bit_array[2] = not bits[2]
        #     transformed_bit_array[3] = not bits[3]
        #     transformed_bit_array[4] = not bits[4]
        #     transformed_bit_array[5] = not bits[5]
        #     transformed_bit_array[6] = not bits[6]
        #     transformed_bit_array[7] = not bits[7]
        #     transformed_byte = bit_list_to_byte(transformed_bit_array)
        #     response_data_inverted += bytes([transformed_byte])

        for enconding in encondings:
            response_string.append(
                (
                    f"Original {enconding}",
                    str(response_data, encoding=enconding, errors="ignore"),
                )
            )
            # response_string.append(
            #     (
            #         f"Reversed {enconding}",
            #         str(
            #             response_data_reversed,
            #             encoding=enconding,
            #             errors="ignore",
            #         ),
            #     )
            # )
            # response_string.append(
            #     (
            #         f"Transformed {enconding}",
            #         str(
            #             response_data_byte_transformed1,
            #             encoding=enconding,
            #             errors="ignore",
            #         ),
            #     )
            # )
            # response_string.append(
            #     (
            #         f"Reversed transformed {enconding}",
            #         str(
            #             response_data_byte_transformed1,
            #             encoding=enconding,
            #             errors="ignore",
            #         ),
            #     )
            # )
            # response_string.append(
            #     (
            #         f"Reversed transformed2 {enconding}",
            #         str(
            #             response_data_byte_transformed2,
            #             encoding=enconding,
            #             errors="ignore",
            #         ),
            #     )
            # )
            # response_string.append(
            #     (
            #         f"Reversed transformed2 {enconding}",
            #         str(
            #             response_data_byte_transformed2,
            #             encoding=enconding,
            #             errors="ignore",
            #         ),
            #     )
            # )

            # response_string.append(
            #     (
            #         f"Inverted {enconding}",
            #         str(
            #             response_data_inverted,
            #             encoding=enconding,
            #             errors="ignore",
            #         ),
            #     )
            # )

        if repetitions > 0:
            print(
                "Received data: ", *[f"{char:02x} " for char in response_data]
            )
            # print(
            #     "Received data reversed: ",
            #     *[f"{char:02x} " for char in response_data_reversed],
            # )
            # print(
            #     "Received data byte transformed: ",
            #     *[f"{char:02x} " for char in response_data_byte_transformed1],
            # )
            # print(
            #     "Received data inverted: ",
            #     *[f"{char:02x} " for char in response_data_inverted],
            # )
            print("Received data strings decoded: ")
            for encoding, string in response_string:
                print(f"{encoding:35} - {string}")

        print("Done")
        repetitions += 1
    except socket.timeout:
        print("No response from host")
    except KeyboardInterrupt:
        print("User interrupted")
        break

# Terminate
sock.close()
