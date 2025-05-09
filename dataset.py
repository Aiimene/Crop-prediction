import random

def generate_random_rice_data(num_rows):
    # Define the range for each parameter
    ranges = {
        'N': (80, 100),
        'P': (40, 50),
        'K': (40, 50),
        'temperature': (18, 22),
        'humidity': (80, 85),
        'ph': (6.4, 6.7),
        'rainfall': (200, 220),
        # rice will go here as the 8th column
        'sunlight': (29, 32),
        'soil_moisture': (1, 3),
        'soil_type': (8, 10),
        'irrigation': (10, 15),
        'fertilizer_usage': (430, 450),
        'growth_stage': (3, 4),
        'pest_pressure': (11, 15),
        'water_usage_efficiency': (55, 60),
        'co2_concentration': (180, 190),
        'frost_risk': (1, 2),
        'urban_area_proximity': (2, 3),
        'water_source_type': (90, 100),
        'soil_type_index': (1, 3),
        'sunlight_exposure': (0.5, 1.5),
        'irrigation_frequency': (1, 7)
    }

    data = []
    for _ in range(num_rows):
        row = [
            random.uniform(*ranges['N']),
            random.uniform(*ranges['P']),
            random.uniform(*ranges['K']),
            random.uniform(*ranges['temperature']),
            random.uniform(*ranges['humidity']),
            random.uniform(*ranges['ph']),
            random.uniform(*ranges['rainfall']),
        ]

        row.append('rice')  # 8th column

        row.extend([
            random.uniform(*ranges['sunlight']),
            random.randint(*ranges['soil_moisture']),
            random.uniform(*ranges['soil_type']),
            random.uniform(*ranges['irrigation']),
            random.uniform(*ranges['fertilizer_usage']),
            random.uniform(*ranges['growth_stage']),
            random.uniform(*ranges['pest_pressure']),
            random.uniform(*ranges['water_usage_efficiency']),
            random.uniform(*ranges['co2_concentration']),
            random.randint(*ranges['frost_risk']),
            random.uniform(*ranges['urban_area_proximity']),
            random.uniform(*ranges['water_source_type']),
            random.randint(*ranges['soil_type_index']),
            random.uniform(*ranges['sunlight_exposure']),
            random.randint(*ranges['irrigation_frequency']),
        ])
        
        data.append(row)
    
    return data

# Example usage
num_rows = 10000
random_rice_data = generate_random_rice_data(num_rows)

# Print with rounded floats and rice in 8th column
for row in random_rice_data:
    formatted_row = [f"{x:.3f}" if isinstance(x, float) else str(x) for x in row]
    print(",".join(formatted_row))