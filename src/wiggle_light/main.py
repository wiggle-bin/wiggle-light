import argparse
import board
import neopixel


def on(brightness=0.1):
    pixels = neopixel.NeoPixel(board.D21, 24, brightness=brightness)
    pixels.fill((255, 0, 0))
    print(f"WiggleLight: On, brightness = {brightness}")


def off():
    pixels = neopixel.NeoPixel(board.D21, 24)
    pixels.show()
    print(f"WiggleLight: Off")


def main():
    parser = argparse.ArgumentParser(
        prog="WiggleLight", description="Control NeoPixel led ring on WiggleBin"
    )

    light = parser.add_argument_group("light")
    light.add_argument(
        "--on", nargs="?", const=0.1, help="light intensity from 0.01 to 1", type=float
    )
    light.add_argument("--off", action="store_true", help="turn light off")

    args = parser.parse_args()

    if args.on:
        on(args.on)
    elif args.off:
        off()


if __name__ == "__main__":
    main()
