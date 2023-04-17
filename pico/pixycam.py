import board
import busio
import time
import struct


class ColorBlock:
    def __init__(self, b_type, x, y, w, h, angle, index, age):
        self.type = b_type
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.index = index
        self.age = age
        self.angle = angle

    def __repr__(self):
        return f"<ColorBlock type:{self.type} x:{self.x} y:{self.y}>"


class PixyCam:
    def __init__(self):
        # clock, mosi, miso
        self.spi = busio.SPI(board.GP2, board.GP3, board.GP0)
        while (not self.spi.try_lock()):
            pass
        self.spi.configure(baudrate=1000000, phase=0, polarity=0, bits=8)

    def getFPS(self):
        resp = self._send_cmd([24, 0])
        rate = struct.unpack('<I', resp)[0]
        return rate

    def setLamp(self, upper, lower):
        self._send_cmd([22, 2, int(upper), int(lower)])

    def getResolution(self):
        resp = self._send_cmd([12, 1, 0])
        width, height = struct.unpack('<HH', resp)
        return width, height

    def getBlocks(self, block_type=None):
        """Pass in 1-7 to only return that blocks of that type, omit to return all types of blocks"""

        if block_type is None:
            sigmap = 127
        else:
            sigmap = 1 << (block_type - 1)
        resp = self._send_cmd([32, 2, sigmap, 255])
        if resp is None:
            # try again in case a frame was not ready to be read
            time.sleep(0.02)
            resp = self._send_cmd([32, 2, sigmap, 255])

        blocks = []
        if len(resp) % 14 != 0:
            print(f"PixyCam Error: unexpected response to getBlocks {resp}")
            return []
        num_blocks = len(resp) // 14
        for i in range(num_blocks):
            cc_num, x, y, w, h, angle, idx, age = struct.unpack('<HHHHHHBB', resp[i * 14:(i + 1) * 14])
            blocks.append(ColorBlock(cc_num, x, y, w, h, angle, idx, age))
        return blocks

    def _send_cmd(self, cmd):
        MAX_TRIES = 10

        cmd = bytearray([0xae, 0xc1] + cmd)
        self.spi.write(cmd)
        check_byte = bytearray(1)
        num_tries = 0
        while check_byte[0] != 0xAF:
            self.spi.readinto(check_byte)
            num_tries += 1
            if num_tries > MAX_TRIES:
                print("PixyCam Error, cannot find frame start byte")
                return []
        self.spi.readinto(check_byte)
        if check_byte[0] != 0xC1:
            print("PixyCam Error, unexpected packet frame type {frametype}")
            return None
        header = bytearray(4)
        self.spi.readinto(header)
        packet_type, length, checksum = struct.unpack('<BBH', header)
        data = bytearray(length)
        self.spi.readinto(data)
        if sum(data) != checksum:
            print("PixyCam Error, invalid checksum")
        return data
