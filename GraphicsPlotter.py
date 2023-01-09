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

    #TODO: add settings for export graphic 
    #TODO: add setting for import graphic

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


    def get_N_from_freq(self):
        return Tok_functions.N_from_freq(self.get_dielectric())

    def real_part_N_from_freq(self):
        return np.real(self.get_N_from_freq())

    def imag_part_N_from_freq(self):
        return np.imag(self.get_N_from_freq())

    def real_part_dielectric(self):
        return np.real(self.get_dielectric())

    def imag_part_dielectric(self):
        return np.imag(self.get_dielectric())


    def get_R12(self):
        N_v = self.get_N_from_freq()
        r12 = Tok_functions.r12(self.variables.N_air, N_v)
        return Tok_functions.R(r12)

    def get_R23(self):
        N_v = self.get_N_from_freq()
        r = Tok_functions.r23(self.variables.N_air, N_v)
        return Tok_functions.R(r)

    def get_alpha(self):
        return Tok_functions.alpha_from_frea(self.__settings.get_freqs(), self.imag_part_N_from_freq())

    def get_optical_Density(self):
        return Tok_functions.optical_Density(self.get_alpha(), self.variables.d)

    def get_transparency(self):
        n_v = self.real_part_N_from_freq()
        d = self.variables.d
        return Tok_functions.T(self.get_R12(), self.get_R23(), self.get_alpha(), d, self.__settings.get_freqs(), Tok_functions.delta(n_v, d))

    def get_optical_density_interf(self):
        return Tok_functions.A(self.get_transparency())

    def set_settings(self, settings: GraphicSettings):
        self.__settings = settings

    def get_plot_data(self):
        freqs = self.__settings.get_freqs()
        evaluator = GraphicPlotter.__evaluators[self.__settings.graphic_type]
        values = evaluator(self)
        return freqs, values

    __evaluators: dict() = {
        Graphics.REAL_PART_DIELECTRIC: real_part_dielectric,
        Graphics.IMAG_PART_DIELECTRIC: imag_part_dielectric,
        Graphics.REAL_PART_REFRACTION: real_part_N_from_freq,
        Graphics.IMAG_PART_REFLECTION: imag_part_N_from_freq,
        Graphics.R12: get_R12,
        Graphics.PHASE_12: None,
        Graphics.ALPHA: get_alpha,
        Graphics.OPTICAL_DENS_SIMPLE: get_optical_Density,
        Graphics.TRANSPARENCY: get_transparency,
        Graphics.OPTICAL_DENS_HARD: get_transparency,
        Graphics.EXPORT: None 
        }

    pass