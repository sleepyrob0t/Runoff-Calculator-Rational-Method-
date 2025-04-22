

# Runoff Calculator (Rational Method) 🌧️💧  

## Overview  
This Python script calculates peak stormwater runoff using the Rational Method—a fundamental equation in stormwater management and water resources engineering. The Rational Method is a widely accepted technique for estimating runoff from small to mid-sized drainage areas, especially in urban and semi-urban environments.

Accurate runoff estimation plays a vital role in the design of infrastructure like storm drains, culverts, detention basins, and erosion control systems. This script offers a lightweight, easy-to-use tool for engineers, students, and environmental professionals to model how different land use types and rainfall intensities affect runoff volumes.

While the current script provides a functional and educational tool, several enhancements could be implemented in future versions to expand its capabilities and user experience:

- Graphical User Interface (GUI): A simple desktop GUI using Tkinter or PyQt for non-technical users.
- Unit Conversion Options: Support for metric units (e.g., mm/hr, hectares) alongside imperial.
- Multiple Land Use Areas: Allow input of multiple zones with different land uses and areas for more complex watershed modeling.
- Rainfall Data Integration: Link to online rainfall datasets or allow CSV upload for historical/forecasted data analysis.
- Export Results: Generate and export reports as PDFs or spreadsheets for record-keeping and presentations.
- Error Handling Improvements: More robust input validation and user feedback.
- Mobile/Web Version: Adapt the script into a web app or mobile-friendly version for use in the field.


### The Rational Method Equation:  
\[
Q = C \times I \times A
\]  
Where:  
- **Q** = Peak runoff (cubic feet per second, cfs)  
- **C** = Runoff coefficient (depends on land use)  
- **I** = Rainfall intensity (inches per hour)  
- **A** = Drainage area (acres)  

## Features  
- User inputs land use, rainfall intensity, and drainage area.  
- Uses **predefined runoff coefficients** for different land types (pavement, urban, grass, etc.).  
- Outputs peak **runoff flow rate (cfs)** for stormwater design.  

## Installation & Usage  
### 1. Clone the Repository  
```bash
git clone https://github.com/your-username/runoff-calculator.git
cd runoff-calculator


### 2. Run the Script  
Make sure you have **Python 3** installed, then run:  
```bash
python runoff_calculator.py
```

### 3. Example Input & Output  
```
Enter land use type (pavement, urban, suburban, grass, forest): Urban
Enter rainfall intensity (in/hr): 2.5
Enter drainage area (acres): 10

Estimated peak runoff: 17.50 cubic feet per second (cfs)
```

## Future Improvements  
- Add support for **GIS integration**  
- Implement **HEC-HMS or SWMM modeling compatibility**  
- Develop a **GUI interface**  

## License  
 MIT License - Feel free to use and modify!  
