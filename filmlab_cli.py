#!/usr/bin/env python3
"""
filmlab_cli.py

A simple CLI for adjusting the exposure and contrast of film scans. Built with Click and Pillow.
"""
import click
from PIL import Image, ImageEnhance

@click.command()
@click.argument('input_path', type=click.Path(exists=True))
@click.argument('output_path', type=click.Path())
@click.option('--exposure', default=1.0, show_default=True, help='Exposure multiplier (brightness).')
@click.option('--contrast', default=1.0, show_default=True, help='Contrast multiplier.')
def process(input_path, output_path, exposure, contrast):
    """Process the input image and save the result to OUTPUT_PATH."""
    img = Image.open(input_path).convert('RGB')
    # Adjust exposure
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(exposure)
    # Adjust contrast
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(contrast)
    img.save(output_path)
    click.echo(f'Saved processed image to {output_path}')

if __name__ == '__main__':
    process()
