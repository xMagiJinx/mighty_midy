import usb_cdc
import analogio
import board

# instead of camera logic, now using knob logic

knob_tilt = analogio.AnalogIn(board.A0)
knob_pan = analogio.AnalogIn(board.A1)
# or try GP26 or GP27

while True:
    # wait for data from serial, stalls at line 8
    usb_cdc.data.readline()
    msg = f"{knob_pan.value},{knob_tilt.value}\n"
    usb_cdc.data.write(msg.encode())

    # if opened in TeraTerm, sends back value between 0 - 65535

