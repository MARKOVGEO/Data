## File mining_trajectories.csv
 Column        Type     Description                                   Values                 
-----------------------------------------------------------------------------------------  
 site_id       string   Unique mining site identifier                Format MXXXXXX      
 years         list     Observation years (sorted)                  1990;1995;2000      
 states        list     Status codes at corresponding years          0=Prospect, 1=Active, 2=Past Producer, 3=Closed   
 commodity     string   Primary resource                            Cu, Au, Fe      
 latitude      float    WGS84 coordinate                            [-90.0, 90.0]         
 longitude     float    WGS84 coordinate                            [-180.0, 180.0]       

## Processing History
- Filtered sites with ≥2 temporal observations
- State label standardization
- Coordinate validation (WGS84)