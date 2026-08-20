import os
from pdf2image import convert_from_path
from pathlib import Path

# Define input files and output directory
pdf_files = [
    "Physics 180/p180.pdf",
    "Physics 131/p131.pdf",
    "Physics 225/p225.pdf"
]

output_dir = "pdf_covers"

# Create output directory if it doesn't exist
Path(output_dir).mkdir(parents=True, exist_ok=True)

# Process each PDF
for pdf_path in pdf_files:
    try:
        print(f"Processing: {pdf_path}")
        
        # Convert only the first page
        images = convert_from_path(pdf_path, dpi=300, first_page=1, last_page=1)
        
        # Generate output filename
        base_name = os.path.basename(pdf_path).replace('.pdf', '.png')
        output_path = os.path.join(output_dir, base_name)
        
        # Save the first page as PNG
        images[0].save(output_path, 'PNG')
        print(f"  -> Saved to: {output_path}")
        
    except Exception as e:
        print(f"  Error processing {pdf_path}: {e}")

print("\nDone!")
