import numpy as np
import plotly.graph_objects as go

def mango(u, v):
    # Base ellipsoid
    a = 1.5 * (1 + 0.2 * np.sin(u))  # Wider in the middle
    b = 0.8 + 0.1 * np.cos(2*u)      # Thinner profile
    c = 1.2                          # Overall height
    
    # Characteristic mango curve and tip
    tip_curve = 0.3 * np.exp(-((v - np.pi/6)**2)) * np.sin(u) 
    side_curve = 0.2 * np.sin(3*u) * np.sin(v/2)              
    
    # Calculate coordinates
    x = a * np.sin(v) * np.cos(u) + side_curve
    y = b * np.sin(v) * np.sin(u)
    z = -(c * np.cos(v) + tip_curve)
    
    return x, y, z

# Generate grid with higher resolution
u = np.linspace(0, 2*np.pi, 200)
v = np.linspace(0, np.pi, 200)
u, v = np.meshgrid(u, v)

# Get coordinates
x, y, z = mango(u, v)

# Color mapping
z_normalized = (z - z.min()) / (z.max() - z.min())

# More natural mango color gradient
colorscale = [
    [0, '#006400'],    # Dark green for bottom
    [0.3, '#9ACD32'],  # Yellow-green
    [0.6, '#FFD700'],  # Golden yellow
    [0.8, '#FFA500'],  # Orange
    [1, '#FF6347']     # Red-orange for top
]

# Create the 3D surface with enhanced lighting
fig = go.Figure(data=[go.Surface(
    x=x, 
    y=y, 
    z=z, 
    surfacecolor=z_normalized,
    colorscale=colorscale,
    lighting=dict(
        ambient=0.6,
        diffuse=0.9,
        fresnel=0.2,
        specular=0.3,
        roughness=0.7
    )
)])

# mango visualization
fig.update_layout(
    title="Mango",
    scene=dict(
        xaxis_title="X",
        yaxis_title="Y",
        zaxis_title="Z",
        xaxis=dict(showgrid=False, showbackground=False),
        yaxis=dict(showgrid=False, showbackground=False),
        zaxis=dict(showgrid=False, showbackground=False),
        camera=dict(
            up=dict(x=0, y=0, z=1),
            center=dict(x=0, y=0, z=0),
            eye=dict(x=2, y=2, z=1.5)  
        ),
        aspectratio=dict(x=1, y=1, z=1.2)  
    ),
    margin=dict(l=0, r=0, t=50, b=0),
)

fig.show()