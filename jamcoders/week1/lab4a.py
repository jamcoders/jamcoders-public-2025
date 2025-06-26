import geopandas as gpd
import matplotlib.pyplot as plt
import random
from shapely.geometry import Point
import ipywidgets as widgets
from IPython.display import display, clear_output

# Load data 
#used for vscode playing:
# gdf = gpd.read_file("jamaica_parishes.geojson").to_crs(epsg=4326)
#used for colab playing:
import os
BASE_DIR = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE_DIR, "data", "jamaica_parishes.geojson")
gdf = gpd.read_file(DATA_PATH).to_crs(epsg=4326)
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

        # Game logic -- widget-based for "play again" option
        # Widget-based guessing logic
        guess_input = widgets.Text(
            placeholder='Type parish name...',
            description='Guess:',
            layout=widgets.Layout(width='300px')
        )
        submit_button = widgets.Button(description="Submit Guess")
        feedback_output = widgets.Output()

        # Track state
        attempts = [tries]  

        def on_submit_clicked(b):
            guess = guess_input.value.strip()
            with feedback_output:
                feedback_output.clear_output()
                if guess.lower() == correct_parish.lower():
                    print("Correct! Well done.")
                    guess_input.disabled = True
                    submit_button.disabled = True
                else:
                    attempts[0] -= 1
                    if attempts[0] == 2:
                        print("Nice try but not yet.")
                    elif attempts[0] == 1:
                        print("Only one guess left.")
                    elif attempts[0] <= 0:
                        print(f"Out of guesses! The correct parish was **{correct_parish}**.")
                        guess_input.disabled = True
                        submit_button.disabled = True

        submit_button.on_click(on_submit_clicked)
        display(widgets.HBox([guess_input, submit_button]), feedback_output)


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
        
        # Use Javascript + Colab callback to avoid input() bug
        from IPython.display import Javascript
        try:
            from google.colab import output
            output.register_callback("playGame", play_parish_search)

            def on_replay_clicked(b):
                display(Javascript('google.colab.kernel.invokeFunction("playGame", [], {})'))

        except ImportError:
            # Fallback: run directly (needed when using VSCode)
            def on_replay_clicked(b):
                clear_output(wait=True)
                play_parish_search(tries=tries)

        replay_button.on_click(on_replay_clicked)
        display(replay_button, output)

    run_game()
