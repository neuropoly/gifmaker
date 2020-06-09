# Usage

The examples below are based on the example images: `gifmaker/tests/images/`.
To look at all the features, run:

```bash
gifmaker -h
```

## Standard usage

```bash
gifmaker -i 1.png 2.png 3.png 4.png 5.png -o myanim.gif
```

Or, using Unix regex:

```bash
gifmaker -i *.png
```

!!! note
    All images should have the same size.
 
## Cropping

```bash
gifmaker -i *.png -c 10 100 40 100 -o anim-crop.gif
```

## Rescaling

For 2x downsampling:
```bash
gifmaker -i *.png -r 0.5 -o anim-ds.gif
```

You can combine processes. Example: cropping and 2x upsampling (in the same order):
```bash
gifmaker -i *.png -c 50 100 50 100 -r 2 -o anim-ds.gif
```
