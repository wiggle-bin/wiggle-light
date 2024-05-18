import argparse
import board
import neopixel_spi as neopixel

spi = board.SPI()

NUM_PIXELS = 24
PIXEL_ORDER = neopixel.GRB

pixels = neopixel.NeoPixel_SPI(spi,
                               NUM_PIXELS,
                               pixel_order=PIXEL_ORDER,
                               auto_write=False)

default_brightness = 0.2

def on(brightness=default_brightness):
    pixels.brightness = brightness
    pixels.fill((255, 0, 0))
    pixels.show()
    print(f"WiggleLight: On, brightness = {brightness}")


def off():
    pixels.fill((0, 0, 0))
    pixels.show()
    print(f"WiggleLight: Off")


def main():
    parser = argparse.ArgumentParser(
        prog="WiggleLight", description="Control NeoPixel led ring on WiggleBin"
    )

    light = parser.add_argument_group("light")
    light.add_argument(
        "--on", nargs="?", const=default_brightness, help="light intensity from 0.01 to 1", type=float
    )
    light.add_argument("--off", action="store_true", help="turn light off")

    args = parser.parse_args()

    if args.on:
        on(args.on)
    elif args.off:
        off()


if __name__ == "__main__":
    main()
