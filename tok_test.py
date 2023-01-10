import GraphicsPlotter
import matplotlib.pyplot as plt
import Tok_functions
import ASCIIparser


def main():
    settings = GraphicsPlotter.GraphicSettings()
    settings.graphic_type = GraphicsPlotter.Graphics.IMAG_PART_DIELECTRIC

    input_vars = Tok_functions.InputVariables()

    plotter = GraphicsPlotter.GraphicPlotter(input_vars)
    # settings._import_path = "test_export.ASCII"
    plotter.set_settings(settings)

    x, y = plotter.get_plot_data(normalize=True)

    plt.plot(x, y)
    plt.grid()
    plt.show()

    # ASCIIparser.exportASCII(x,y, "test_export.ASCII")

    pass


if __name__ == '__main__':
    main()
