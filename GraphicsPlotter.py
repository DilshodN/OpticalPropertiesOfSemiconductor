import numpy as np
from constants import Constants
import enum
import Tok_functions

class Graphics(enum.Enum):

    REAL_PART_DIELECTRIC = 0
    IMAG_PART_DIELECTRIC = 1
    REAL_PART_REFRACTION = 2
    IMAG_PART_REFLECTION = 3
    R12 = 4
    PHASE_12 = 5
    ALPHA = 6
    OPTICAL_DENS_SIMPLE = 7
    TRANSPARENCY = 8
    OPTICAL_DENS_HARD = 9
    EXPORT = 10

    pass


class GraphicSettings:

    graphic_type: Graphics = Graphics.EXPORT

    __freq_max: float = 4500
    __freq_min: float = 100
    # __sample_count: int = 500
    __step: float = 10

    # __sample_count: int = (int)(__freq_max - __freq_min)/__step

    _freqs: np.array = np.arange(__freq_min, __freq_max, __step)


    def __update_freqs(self):
        self._freqs = np.arange(self.__freq_min, self.__freq_max, self.__step)

    def set_sample_count(self, sample_count: int):
        # self.__sample_count = sample_count
        self.__step = (self.__freq_max - self.__freq_min)/sample_count
        self.__update_freqs()

    def set_step(self, step: float):
        self.__step = step
        self.__update_freqs()
    
    def get_freqs(self):
        return self._freqs

    pass


class GraphicPlotter:

    __settings: GraphicSettings = GraphicSettings()


    variables: Tok_functions.InputVariables


    def __init__(self, input: Tok_functions.InputVariables):
        self.variables = input

    def get_dielectric(self):
        freq_p0 = Tok_functions.plasma_freq_of_free_oscillations(self.variables.N0, self.variables.eps_inf)
        freq_pi = Tok_functions.plasma_freq_of_connected_charges(self.variables.ei, self.variables.Ni, self.variables.mi, self.variables.eps_inf)
        return Tok_functions.dielectric_from_freq(freq_p0, freq_pi, self.variables.vi, self.variables.Gamma0,
         self.variables.Gamma_i, self.variables.eps_inf, self.__settings.get_freqs())

    def real_part_dielectric(self):
        return np.real(self.get_dielectric())

    def imag_part_dielectric(self):
        return np.imag(self.get_dielectric())

    def get_plot_data_certain(settings: GraphicSettings):
        freqs = settings.get_freqs()
        evaluator = GraphicPlotter.__evaluators[settings.graphic_type]
        values = evaluator(freqs)
        return freqs, values

    __evaluators: dict() = {
        Graphics.REAL_PART_DIELECTRIC: real_part_dielectric,
        Graphics.IMAG_PART_DIELECTRIC: imag_part_dielectric,
        Graphics.REAL_PART_REFRACTION: Tok_functions.N_from_freq, # same
        Graphics.IMAG_PART_REFLECTION: Tok_functions.N_from_freq, # same
        Graphics.R12: Tok_functions.R,
        Graphics.PHASE_12: None,
        Graphics.ALPHA: Tok_functions.alpha_from_frea,
        Graphics.OPTICAL_DENS_SIMPLE: Tok_functions.optical_Density,
        Graphics.TRANSPARENCY: Tok_functions.T,
        Graphics.OPTICAL_DENS_HARD: Tok_functions.A,
        Graphics.EXPORT: None 
        }

    pass