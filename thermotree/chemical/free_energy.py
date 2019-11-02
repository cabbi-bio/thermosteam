# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 06:56:43 2019

@author: yoelr
"""
from .utils import R
from ..base import H, S, PhasePropertyBuilder
from math import log
    
@H.l(njitcompile=False)
def Liquid_Enthalpy_Ref_Liquid(T, Cp, T_ref, H_ref):
    """Enthapy (kJ/kmol) disregarding pressure and assuming the specified phase."""
    return H_ref + Cp.l.integrate_by_T(T_ref, T)

@H.l(njitcompile=False)
def Liquid_Enthalpy_Ref_Gas(T, Cp, H_int_Tb_to_T_ref_g, Hvap_Tb, Tb, H_ref):
    return H_ref - H_int_Tb_to_T_ref_g - Hvap_Tb + Cp.l.integrate_by_T(Tb, T)
    
@H.l(njitcompile=False)
def Liquid_Enthalpy_Ref_Solid(T, Cp, H_int_T_ref_to_Tm_s, Hfus, Tm, H_ref):
    return H_ref + H_int_T_ref_to_Tm_s + Hfus + Cp.l.integrate_by_T(Tm, T)
    
@H.s(njitcompile=False)
def Solid_Enthalpy_Ref_Solid(T, Cp, T_ref, H_ref):
    return H_ref + Cp.s.integrate_by_T(T_ref, T)

@H.s(njitcompile=False)
def Solid_Enthalpy_Ref_Liquid(T, Cp, H_int_Tm_to_T_ref_l, Hfus, Tm, H_ref):
    return H_ref - H_int_Tm_to_T_ref_l - Hfus + Cp.s.integrate_by_T(Tm, T)

@H.s(njitcompile=False)
def Solid_Enthalpy_Ref_Gas(T, Cp, H_int_Tb_to_T_ref_g, Hvap_Tb, H_int_Tm_to_Tb_l, Hfus, Tm, H_ref):
    return H_ref - H_int_Tb_to_T_ref_g - Hvap_Tb - H_int_Tm_to_Tb_l - Hfus + Cp.s.integrate_by_T(Tm, T)
    
@H.g(njitcompile=False)
def Gas_Enthalpy_Ref_Gas(T, Cp, T_ref, H_ref):
    return H_ref + Cp.g.integrate_by_T(T_ref, T)

@H.g(njitcompile=False)
def Gas_Enthalpy_Ref_Liquid(T, Cp, H_int_T_ref_to_Tb_l, Hvap_Tb, T_ref, H_ref):
    return H_ref + H_int_T_ref_to_Tb_l + Hvap_Tb + Cp.g.integrate_by_T(T_ref, T)

@H.g(njitcompile=False)
def Gas_Enthalpy_Ref_Solid(T, Cp, H_int_T_ref_to_Tm_s, Hfus, H_int_Tm_to_Tb_l, Hvap_Tb, Tb, H_ref):
    return H_ref + H_int_T_ref_to_Tm_s + Hfus + H_int_Tm_to_Tb_l + Hvap_Tb + Cp.g.integrate_by_T(Tb, T)


EnthalpyRefLiquid = PhasePropertyBuilder(Solid_Enthalpy_Ref_Liquid,
                                         Liquid_Enthalpy_Ref_Liquid,
                                         Gas_Enthalpy_Ref_Liquid)

EnthalpyRefSolid = PhasePropertyBuilder(Solid_Enthalpy_Ref_Solid,
                                        Liquid_Enthalpy_Ref_Solid,
                                        Gas_Enthalpy_Ref_Solid)

EnthalpyRefGas = PhasePropertyBuilder(Solid_Enthalpy_Ref_Gas,
                                      Liquid_Enthalpy_Ref_Gas,
                                      Gas_Enthalpy_Ref_Gas)

@S.l(njitcompile=False)
def Liquid_Entropy_Ref_Liquid(T, Cp, T_ref, S_ref):
    """Enthapy (kJ/kmol) disregarding pressure and assuming the specified phase."""
    return S_ref + Cp.l.integrate_by_T_over_T(T_ref, T)

@S.l(njitcompile=False)
def Liquid_Entropy_Ref_Gas(T, Cp, S_int_Tb_to_T_ref_g, Svap_Tb, Tb, S_ref):
    return S_ref - S_int_Tb_to_T_ref_g - Svap_Tb + Cp.l.integrate_by_T_over_T(Tb, T)
    
@S.l(njitcompile=False)
def Liquid_Entropy_Ref_Solid(T, Cp, S_int_T_ref_to_Tm_s, Sfus, Tm, S_ref):
    return S_ref + S_int_T_ref_to_Tm_s + Sfus + Cp.l.integrate_by_T_over_T(Tm, T)
    
@S.s(njitcompile=False)
def Solid_Entropy_Ref_Solid(T, Cp, T_ref, S_ref):
    return S_ref + Cp.s.integrate_by_T_over_T(T_ref, T)

@S.s(njitcompile=False)
def Solid_Entropy_Ref_Liquid(T, Cp, S_int_Tm_to_T_ref_l, Sfus, Tm, S_ref):
    return S_ref - S_int_Tm_to_T_ref_l - Sfus + Cp.s.integrate_by_T_over_T(Tm, T)

@S.s(njitcompile=False)
def Solid_Entropy_Ref_Gas(T, Cp, S_int_Tb_to_T_ref_g, Svap_Tb, S_int_Tm_to_Tb_l, Sfus, Tm, S_ref):
    return S_ref - S_int_Tb_to_T_ref_g - Svap_Tb - S_int_Tm_to_Tb_l - Sfus + Cp.s.integrate_by_T_over_T(Tm, T)
    
@S.g(njitcompile=False)
def Gas_Entropy_Ref_Gas(T, P, Cp, T_ref, P_ref, S_ref):
    return S_ref + Cp.g.integrate_by_T_over_T(T_ref, T) - R*log(P/P_ref)

@S.g(njitcompile=False)
def Gas_Entropy_Ref_Liquid(T, P, Cp, S_int_T_ref_to_Tb_l, Svap_Tb, T_ref, P_ref, S_ref):
    return S_ref + S_int_T_ref_to_Tb_l + Svap_Tb + Cp.g.integrate_by_T_over_T(T_ref, T) - R*log(P/P_ref)

@S.g(njitcompile=False)
def Gas_Entropy_Ref_Solid(T, P, Cp, S_int_T_ref_to_Tm_s, Sfus, S_int_Tm_to_Tb_l, Svap_Tb, Tb, P_ref, S_ref):
    return S_ref + S_int_T_ref_to_Tm_s + Sfus + S_int_Tm_to_Tb_l + Svap_Tb + Cp.g.integrate_by_T_over_T(Tb, T) - R*log(P/P_ref)


EntropyRefLiquid = PhasePropertyBuilder(Solid_Entropy_Ref_Liquid,
                                         Liquid_Entropy_Ref_Liquid,
                                         Gas_Entropy_Ref_Liquid)

EntropyRefSolid = PhasePropertyBuilder(Solid_Entropy_Ref_Solid,
                                         Liquid_Entropy_Ref_Solid,
                                         Gas_Entropy_Ref_Solid)

EntropyRefGas = PhasePropertyBuilder(Solid_Entropy_Ref_Gas,
                                     Liquid_Entropy_Ref_Gas,
                                     Gas_Entropy_Ref_Gas)

@H.l(njitcompile=False)
def Excess_Liquid_Enthalpy_Ref_Liquid(T, P):
    return 0

@H.l(njitcompile=False)
def Excess_Liquid_Enthalpy_Ref_Gas(T, P, eos, H_dep_Tb_Pb_g, H_dep_Tb_P_ref_g, eos_T_101325):
    return (H_dep_Tb_Pb_g - H_dep_Tb_P_ref_g
            + eos.to_TP(T, P).H_dep_l - eos_T_101325.H_dep_l)
    
@H.l(njitcompile=False)
def Excess_Liquid_Enthalpy_Ref_Solid(T, P):
    return 0
    
@H.s(njitcompile=False)
def Excess_Solid_Enthalpy_Ref_Solid(T, P):
    return 0

@H.s(njitcompile=False)
def Excess_Solid_Enthalpy_Ref_Liquid(T, P):
    return 0

@H.s(njitcompile=False)
def Excess_Solid_Enthalpy_Ref_Gas(T, P):
    return 0
    
@H.g(njitcompile=False)
def Excess_Gas_Enthalpy_Ref_Gas(T, P, eos, H_dep_ref_g):
    return eos.to_TP(T, P).H_dep_g - H_dep_ref_g

@H.g(njitcompile=False)
def Excess_Gas_Enthalpy_Ref_Liquid(T, P, eos, H_dep_T_ref_Pb, H_dep_ref_l, H_dep_Tb_Pb_g):
    return H_dep_T_ref_Pb - H_dep_ref_l + eos.to_TP(T, P).H_dep_g - H_dep_Tb_Pb_g

@H.g(njitcompile=False)
def Excess_Gas_Enthalpy_Ref_Solid(T, Cp, H_int_T_ref_to_Tm_s, Hfus, H_int_Tm_to_Tb_l, Hvap_Tb, Tb, H_ref):
    return NotImplemented

ExcessEnthalpyRefLiquid = PhasePropertyBuilder(Excess_Solid_Enthalpy_Ref_Liquid,
                                               Excess_Liquid_Enthalpy_Ref_Liquid,
                                               Gas_Enthalpy_Ref_Liquid)

ExcessEnthalpyRefSolid = PhasePropertyBuilder(Solid_Enthalpy_Ref_Solid,
                                              Excess_Liquid_Enthalpy_Ref_Solid,
                                              Excess_Gas_Enthalpy_Ref_Solid)

ExcessEnthalpyRefGas = PhasePropertyBuilder(Excess_Solid_Enthalpy_Ref_Gas,
                                            Excess_Liquid_Enthalpy_Ref_Gas,
                                            Excess_Gas_Enthalpy_Ref_Gas)

@S.l(njitcompile=False)
def Excess_Liquid_Entropy_Ref_Liquid(T, P):
    return 0

@S.l(njitcompile=False)
def Excess_Liquid_Entropy_Ref_Gas(T, P, eos, S_dep_Tb_Pb_g, S_dep_Tb_P_ref_g, eos_T_101325):
    return (S_dep_Tb_Pb_g - S_dep_Tb_P_ref_g
            + eos.to_TP(T, P).S_dep_l - eos_T_101325.S_dep_l)
    
@S.l(njitcompile=False)
def Excess_Liquid_Entropy_Ref_Solid(T, P):
    return 0
    
@S.s(njitcompile=False)
def Excess_Solid_Entropy_Ref_Solid(T, P):
    return 0

@S.s(njitcompile=False)
def Excess_Solid_Entropy_Ref_Liquid(T, P):
    return 0

@S.s(njitcompile=False)
def Excess_Solid_Entropy_Ref_Gas(T, P):
    return 0
    
@S.g(njitcompile=False)
def Excess_Gas_Entropy_Ref_Gas(T, P, eos, S_dep_ref_g):
    return eos.to_TP(T, P).S_dep_g - S_dep_ref_g

@S.g(njitcompile=False)
def Excess_Gas_Entropy_Ref_Liquid(T, P, eos, S_dep_T_ref_Pb, S_dep_ref_l, S_dep_Tb_Pb_g):
    return S_dep_T_ref_Pb - S_dep_ref_l + eos.to_TP(T, P).S_dep_g - S_dep_Tb_Pb_g

@S.g(njitcompile=False)
def Excess_Gas_Entropy_Ref_Solid(T, Cp, S_int_T_ref_to_Tm_s, Sfus, S_int_Tm_to_Tb_l, Svap_Tb, Tb, S_ref):
    return NotImplemented

ExcessEntropyRefLiquid = PhasePropertyBuilder(Excess_Solid_Entropy_Ref_Liquid,
                                              Excess_Liquid_Entropy_Ref_Liquid,
                                              Gas_Entropy_Ref_Liquid)

ExcessEntropyRefSolid = PhasePropertyBuilder(Solid_Entropy_Ref_Solid,
                                             Excess_Liquid_Entropy_Ref_Solid,
                                             Excess_Gas_Entropy_Ref_Solid)

ExcessEntropyRefGas = PhasePropertyBuilder(Excess_Solid_Entropy_Ref_Gas,
                                           Excess_Liquid_Entropy_Ref_Gas,
                                           Excess_Gas_Entropy_Ref_Gas)