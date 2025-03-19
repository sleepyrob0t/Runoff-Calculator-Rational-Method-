

# Runoff Calculator (Rational Method) 🌧️💧  

## Overview  
This Python script calculates **peak runoff using the Rational Method**, a fundamental equation in **stormwater management and water resources engineering**.  

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
