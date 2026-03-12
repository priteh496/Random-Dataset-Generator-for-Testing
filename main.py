"""
Random Dataset Generator for Testing
Generates realistic fake datasets for development and testing.
"""

import argparse
from src.generator import DatasetGenerator
from src.config import DATASET_TYPES


def parse_args():
    parser = argparse.ArgumentParser(description="Random Dataset Generator")
    parser.add_argument("type", choices=list(DATASET_TYPES.keys()), help="Dataset type")
    parser.add_argument("-n", "--rows", type=int, default=100, help="Number of rows (default: 100)")
    parser.add_argument("-o", "--output", default="dataset.csv", help="Output file (.csv or .json)")
    parser.add_argument("--seed", type=int, default=42, help="Random seed for reproducibility")
    parser.add_argument("--preview", type=int, default=5, help="Preview N rows in terminal")
    return parser.parse_args()


def main():
    args = parse_args()
    gen = DatasetGenerator(seed=args.seed)

    print(f"\n📊 Generating {args.rows} rows of '{args.type}' data...")
    df = gen.generate(args.type, args.rows)

    # Preview
    print(f"\nPreview ({min(args.preview, len(df))} rows):")
    print(df.head(args.preview).to_string(index=False))

    # Save
    if args.output.endswith(".json"):
        df.to_json(args.output, orient="records", indent=2)
    else:
        df.to_csv(args.output, index=False)

    print(f"\n✅ Saved {len(df)} rows to '{args.output}'")


if __name__ == "__main__":
    main()
