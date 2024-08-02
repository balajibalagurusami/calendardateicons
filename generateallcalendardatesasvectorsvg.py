import os
from datetime import datetime, timedelta

# Define the directory to save the SVG files
output_dir = r"C:\PNG\mmdd"

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Function to generate SVG content
def generate_svg(month, day):
    month_str = month.upper()
    day_str = f"{day:02d}"
    svg_content = f"""<!--Made with love by https://balaji.work-->
<svg id="eqGSVMi4EOm1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 64 64" shape-rendering="geometricPrecision" text-rendering="geometricPrecision" project-id="ef367fd1a0aa4f3cad7eaddfa3ad2c51" export-id="8b07b5e9cbb1489484662361a76cf016" cached="false">
  <rect width="64" height="32" rx="0" ry="0" fill="#ed4c5c" stroke-width="0"/>
  <rect width="64" height="32" rx="0" ry="0" transform="translate(0 32)" fill="#d9e3e8" stroke-width="0"/>
  <text dx="0" dy="0" font-family="Arial" font-size="25" font-weight="700" transform="translate(4.222754 24.654278)" fill="#fff" stroke-width="0"><tspan y="0" font-weight="700" stroke-width="0">
{month_str}
</tspan></text>
  <text dx="0" dy="0" font-family="Arial" font-size="30" font-weight="700" transform="translate(15.315085 58.430344)" stroke-width="0"><tspan y="0" font-weight="700" stroke-width="0">
{day_str}
</tspan></text>
</svg>
"""
    return svg_content

# Function to save SVG content to a file
def save_svg(content, file_path):
    with open(file_path, "w") as file:
        file.write(content)

# Starting date for the leap year (e.g., 2020)
start_date = datetime(2020, 1, 1)

# Loop through each day of the year
for day_offset in range(366):
    date = start_date + timedelta(days=day_offset)
    month_abbr = date.strftime('%b').upper()
    day = date.day
    year_suffix = date.strftime('%y')
    file_name = f"{year_suffix}{date.strftime('%m')}{date.strftime('%d')}.svg"
    file_path = os.path.join(output_dir, file_name)
    svg_content = generate_svg(month_abbr, day)
    save_svg(svg_content, file_path)

print("SVG files generated successfully.")
