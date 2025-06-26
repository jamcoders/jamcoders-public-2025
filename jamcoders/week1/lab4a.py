import geopandas as gpd
import matplotlib.pyplot as plt
import random
from shapely.geometry import Point
import ipywidgets as widgets
from IPython.display import display, clear_output

# Load data 
gdf = gpd.read_file("jamaica_parishes.geojson").to_crs(epsg=4326)
island = gdf.unary_union

def play_parish_search(tries=3):
    def get_random_point_on_land(polygon):
        minx, miny, maxx, maxy = polygon.bounds
        while True:
            p = Point(random.uniform(minx, maxx), random.uniform(miny, maxy))
            if polygon.contains(p):
                return p

    def run_game():
        clear_output(wait=True)
        pt = get_random_point_on_land(island)

        # Find parish
        correct_parish = None
        for _, row in gdf.iterrows():
            if row.geometry.contains(pt):
                correct_parish = row["name"]
                break

        # Initial plot
        fig, ax = plt.subplots(figsize=(6,6))
        gpd.GeoSeries(island).boundary.plot(ax=ax, color="black")
        ax.plot(pt.x, pt.y, marker="x", color="red", markersize=20)
        ax.set_axis_off()
        plt.show()

        # Game logic
        attempts = tries
        while attempts > 0:
            guess = input(f"Guess the parish ({attempts} {'tries' if attempts > 1 else 'try'} left): ").strip()
            if guess.lower() == correct_parish.lower():
                print("Correct! Well done.")
                break
            attempts -= 1
            if attempts == 2:
                print("Nice try but not yet.")
            elif attempts == 1:
                print("Only one guess left.")
            else:
                print(f"Out of guesses! The correct parish was **{correct_parish}**.")

        # Reveal map
        fig, ax = plt.subplots(figsize=(6,6))
        gdf.boundary.plot(ax=ax, color="gray")
        gdf[gdf["name"] == correct_parish].plot(ax=ax, color="yellow", alpha=0.5)
        ax.plot(pt.x, pt.y, marker="x", color="red", markersize=20)
        ax.set_title(f"The correct parish: {correct_parish}", fontsize=15)
        ax.set_axis_off()
        plt.show()

        # Replay button
        replay_button = widgets.Button(description="Play Again")
        output = widgets.Output()

        def on_replay_clicked(b):
            with output:
                clear_output(wait=True)
                play_parish_search(tries=tries)

        replay_button.on_click(on_replay_clicked)
        display(replay_button, output)

    run_game()
