import GraphicsPlotter
import matplotlib.pyplot as plt
import Tok_functions

def main():
    
    settings = GraphicsPlotter.GraphicSettings()
    settings.graphic_type = GraphicsPlotter.Graphics.EXPORT

    input_vars = Tok_functions.InputVariables()

    plotter = GraphicsPlotter.GraphicPlotter(input_vars)
    plotter.set_settings(settings)

    x,y = plotter.get_plot_data()

    plt.plot(x,y)
    plt.grid()
    plt.show()
    pass


if __name__ == '__main__':
    main()