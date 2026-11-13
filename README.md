# make.fun Food Picture Competition Entry (food-picture-01)

## Dish Description
A professional food photograph featuring a pan-seared salmon fillet with golden crispy skin, resting on a bed of vibrant green herb risotto, accompanied by glossy roasted cherry tomatoes, microgreens, and edible flowers on a dark ceramic plate under warm natural window light with subtle rising steam.

## How It Works
`main.py` is written in pure Python 3.13 using only the standard library (`pathlib`). It resolves the bundled `food.jpg` relative to its own location (`__file__`), creates the `/output` directory if it does not already exist, and performs a plain, verbatim binary copy of `food.jpg` to `/output/entry.png`. 

## Determinism & Constraints
- **Deterministic:** Produces identical byte output (`sha256: 2c25269a0e853fef37450e7ce815af7ac1ad6e703813c4d24fd5531c2d37485d`) on every execution.
- **Dependencies:** Standard library only (no third-party packages).
- **Network / Time:** Zero network access, time, date, or random number generation.
- **File Size:** 222,902 bytes (well under the 1 MiB limit).
- **Dimensions:** 1024x1024 pixels.
