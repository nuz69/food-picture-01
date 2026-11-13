import pathlib

def main():
    current_dir = pathlib.Path(__file__).resolve().parent
    source_path = current_dir / "food.jpg"
    output_dir = pathlib.Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "entry.png"
    
    image_bytes = source_path.read_bytes()
    output_path.write_bytes(image_bytes)

if __name__ == "__main__":
    main()
