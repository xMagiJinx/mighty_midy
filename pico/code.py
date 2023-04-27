from pixycam import PixyCam
import usb_cdc

camera = PixyCam()

while True:
    # wait for data from serial, stalls at line 8
    usb_cdc.data.readline()
    blocks1 = camera.getBlocks(1)

    # need len statements for both ball types
    if len(blocks1) == 0:
        bx = -1
        by = -1
    else:
        bx = blocks1[0].x
        by = blocks1[0].y

    blocks2 = camera.getBlocks(2)
    if len(blocks2) == 0:
        rx = -2
        ry = -2
    else:
        rx = blocks2[0].x
        ry = blocks2[0].y

    msg = f"{bx},{by},{rx}, {ry}\n"
    usb_cdc.data.write(msg.encode())

