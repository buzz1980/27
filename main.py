def on_forever():
    pins.digital_write_pin(DigitalPin.P0, 1)
    basic.pause(2000)
    pins.digital_write_pin(DigitalPin.P0, 0)
    basic.pause(2000)
basic.forever(on_forever)
