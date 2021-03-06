# -*- coding: utf-8 -*-
"""
Free energy functors for Chemical objects.

"""
from .._constants import R
from ..base import functor, PhaseTFunctorBuilder, PhaseTPFunctorBuilder
from math import log
    
@functor(var='H.l')
def Liquid_Enthalpy_Ref_Liquid(T, Cn_l, T_ref, H_ref):
    """Enthapy (kJ/kmol) disregarding pressure and assuming the specified phase."""
    return H_ref + Cn_l.integrate_by_T(T_ref, T)

@functor(var='H.l')
def Liquid_Enthalpy_Ref_Gas(T, Cn_l, H_int_Tb_to_T_ref_g, Hvap_Tb, Tb, H_ref):
    return H_ref - H_int_Tb_to_T_ref_g - Hvap_Tb + Cn_l.integrate_by_T(Tb, T)
    
@functor(var='H.l')
def Liquid_Enthalpy_Ref_Solid(T, Cn_l, H_int_T_ref_to_Tm_s, Hfus, Tm, H_ref):
    return H_ref + H_int_T_ref_to_Tm_s + Hfus + Cn_l.integrate_by_T(Tm, T)
    
@functor(var='H.s')
def Solid_Enthalpy_Ref_Solid(T, Cn_s, T_ref, H_ref):
    return H_ref + Cn_s.integrate_by_T(T_ref, T)

@functor(var='H.s')
def Solid_Enthalpy_Ref_Liquid(T, Cn_s, H_int_Tm_to_T_ref_l, Hfus, Tm, H_ref):
    return H_ref - H_int_Tm_to_T_ref_l - Hfus + Cn_s.integrate_by_T(Tm, T)

@functor(var='H.s')
def Solid_Enthalpy_Ref_Gas(T, Cn_s, H_int_Tb_to_T_ref_g, Hvap_Tb,
                           H_int_Tm_to_Tb_l, Hfus, Tm, H_ref):
    return H_ref - H_int_Tb_to_T_ref_g - Hvap_Tb - H_int_Tm_to_Tb_l - Hfus + Cn_s.integrate_by_T(Tm, T)
    
@functor(var='H.g')
def Gas_Enthalpy_Ref_Gas(T, Cn_g, T_ref, H_ref):
    return H_ref + Cn_g.integrate_by_T(T_ref, T)

@functor(var='H.g')
def Gas_Enthalpy_Ref_Liquid(T, Cn_g, H_int_T_ref_to_Tb_l, Hvap_Tb, 
                            T_ref, H_ref):
    return H_ref + H_int_T_ref_to_Tb_l + Hvap_Tb + Cn_g.integrate_by_T(T_ref, T)

@functor(var='H.g')
def Gas_Enthalpy_Ref_Solid(T, Cn_g, H_int_T_ref_to_Tm_s, Hfus,
                           H_int_Tm_to_Tb_l, Hvap_Tb, Tb, H_ref):
    return H_ref + H_int_T_ref_to_Tm_s + Hfus + H_int_Tm_to_Tb_l + Hvap_Tb + Cn_g.integrate_by_T(Tb, T)


EnthalpyRefLiquid = PhaseTFunctorBuilder('H',
                                        Solid_Enthalpy_Ref_Liquid,
                                        Liquid_Enthalpy_Ref_Liquid,
                                        Gas_Enthalpy_Ref_Liquid)

EnthalpyRefSolid = PhaseTFunctorBuilder('H',
                                       Solid_Enthalpy_Ref_Solid,
                                       Liquid_Enthalpy_Ref_Solid,
                                       Gas_Enthalpy_Ref_Solid)

EnthalpyRefGas = PhaseTFunctorBuilder('H',
                                     Solid_Enthalpy_Ref_Gas,
                                     Liquid_Enthalpy_Ref_Gas,
                                     Gas_Enthalpy_Ref_Gas)

@functor(var='S.l')
def Liquid_Entropy_Ref_Liquid(T, Cn_l, T_ref, S_ref):
    """Enthapy (kJ/kmol) disregarding pressure and assuming the specified phase."""
    return S_ref + Cn_l.integrate_by_T_over_T(T_ref, T)

@functor(var='S.l')
def Liquid_Entropy_Ref_Gas(T, Cn_l, S_int_Tb_to_T_ref_g, Svap_Tb, Tb, S_ref):
    return S_ref - S_int_Tb_to_T_ref_g - Svap_Tb + Cn_l.integrate_by_T_over_T(Tb, T)
    
@functor(var='S.l')
def Liquid_Entropy_Ref_Solid(T, Cn_l, S_int_T_ref_to_Tm_s, Sfus, Tm, S_ref):
    return S_ref + S_int_T_ref_to_Tm_s + Sfus + Cn_l.integrate_by_T_over_T(Tm, T)
    
@functor(var='S.s')
def Solid_Entropy_Ref_Solid(T, Cn_s, T_ref, S_ref):
    return S_ref + Cn_s.integrate_by_T_over_T(T_ref, T)

@functor(var='S.s')
def Solid_Entropy_Ref_Liquid(T, Cn_s, S_int_Tm_to_T_ref_l, Sfus, Tm, S_ref):
    return S_ref - S_int_Tm_to_T_ref_l - Sfus + Cn_s.integrate_by_T_over_T(Tm, T)

@functor(var='S.s')
def Solid_Entropy_Ref_Gas(T, Cn_s, S_int_Tb_to_T_ref_g, Svap_Tb, 
                          S_int_Tm_to_Tb_l, Sfus, Tm, S_ref):
    return S_ref - S_int_Tb_to_T_ref_g - Svap_Tb - S_int_Tm_to_Tb_l - Sfus + Cn_s.integrate_by_T_over_T(Tm, T)
    
@functor(var='S.g')
def Gas_Entropy_Ref_Gas(T, P, Cn_g, T_ref, P_ref, S_ref):
    return S_ref + Cn_g.integrate_by_T_over_T(T_ref, T) - R*log(P/P_ref)

@functor(var='S.g')
def Gas_Entropy_Ref_Liquid(T, P, Cn_g, S_int_T_ref_to_Tb_l, Svap_Tb,
                           T_ref, P_ref, S_ref):
    return S_ref + S_int_T_ref_to_Tb_l + Svap_Tb + Cn_g.integrate_by_T_over_T(T_ref, T) - R*log(P/P_ref)

@functor(var='S.g')
def Gas_Entropy_Ref_Solid(T, P, Cn_g, S_int_T_ref_to_Tm_s, Sfus,
                          S_int_Tm_to_Tb_l, Svap_Tb, Tb, P_ref, S_ref):
    return S_ref + S_int_T_ref_to_Tm_s + Sfus + S_int_Tm_to_Tb_l + Svap_Tb + Cn_g.integrate_by_T_over_T(Tb, T) - R*log(P/P_ref)


EntropyRefLiquid = PhaseTPFunctorBuilder('S',
                                        Solid_Entropy_Ref_Liquid,
                                        Liquid_Entropy_Ref_Liquid,
                                        Gas_Entropy_Ref_Liquid)

EntropyRefSolid = PhaseTPFunctorBuilder('S',
                                       Solid_Entropy_Ref_Solid,
                                       Liquid_Entropy_Ref_Solid,
                                       Gas_Entropy_Ref_Solid)

EntropyRefGas = PhaseTPFunctorBuilder('S',
                                     Solid_Entropy_Ref_Gas,
                                     Liquid_Entropy_Ref_Gas,
                                     Gas_Entropy_Ref_Gas)

@functor(var='H.l')
def Excess_Liquid_Enthalpy_Ref_Liquid(T, P):
    return 0

@functor(var='H.l')
def Excess_Liquid_Enthalpy_Ref_Gas(T, P, eos, H_dep_Tb_Pb_g,
                                   H_dep_Tb_P_ref_g, eos_1atm):
    return (H_dep_Tb_Pb_g - H_dep_Tb_P_ref_g
            + eos.to_TP(T, P).H_dep_l - eos_1atm.H_dep_l)
    
@functor(var='H.l')
def Excess_Liquid_Enthalpy_Ref_Solid(T, P):
    return 0
    
@functor(var='H.s')
def Excess_Solid_Enthalpy_Ref_Solid(T, P):
    return 0

@functor(var='H.s')
def Excess_Solid_Enthalpy_Ref_Liquid(T, P):
    return 0

@functor(var='H.s')
def Excess_Solid_Enthalpy_Ref_Gas(T, P):
    return 0
    
@functor(var='H.g')
def Excess_Gas_Enthalpy_Ref_Gas(T, P, eos, H_dep_ref_g):
    return eos.to_TP(T, P).H_dep_g - H_dep_ref_g

@functor(var='H.g')
def Excess_Gas_Enthalpy_Ref_Liquid(T, P, eos, H_dep_T_ref_Pb,
                                   H_dep_ref_l, H_dep_Tb_Pb_g):
    return H_dep_T_ref_Pb - H_dep_ref_l + eos.to_TP(T, P).H_dep_g - H_dep_Tb_Pb_g

@functor(var='H.g')
def Excess_Gas_Enthalpy_Ref_Solid(T):
    return 0

ExcessEnthalpyRefLiquid = PhaseTPFunctorBuilder('H_excess',
                                               Excess_Solid_Enthalpy_Ref_Liquid,
                                               Excess_Liquid_Enthalpy_Ref_Liquid,
                                               Excess_Gas_Enthalpy_Ref_Liquid)

ExcessEnthalpyRefSolid = PhaseTPFunctorBuilder('H_excess',
                                                Excess_Solid_Enthalpy_Ref_Solid,
                                                Excess_Liquid_Enthalpy_Ref_Solid,
                                                Excess_Gas_Enthalpy_Ref_Solid)

ExcessEnthalpyRefGas = PhaseTPFunctorBuilder('H_excess',
                                            Excess_Solid_Enthalpy_Ref_Gas,
                                            Excess_Liquid_Enthalpy_Ref_Gas,
                                            Excess_Gas_Enthalpy_Ref_Gas)

@functor(var='S.l')
def Excess_Liquid_Entropy_Ref_Liquid(T, P):
    return 0

@functor(var='S.l')
def Excess_Liquid_Entropy_Ref_Gas(T, P, eos, S_dep_Tb_Pb_g,
                                  S_dep_Tb_P_ref_g, eos_1atm):
    return (S_dep_Tb_Pb_g - S_dep_Tb_P_ref_g
            + eos.to_TP(T, P).S_dep_l - eos_1atm.S_dep_l)
    
@functor(var='S.l')
def Excess_Liquid_Entropy_Ref_Solid(T, P):
    return 0
    
@functor(var='S.s')
def Excess_Solid_Entropy_Ref_Solid(T, P):
    return 0

@functor(var='S.s')
def Excess_Solid_Entropy_Ref_Liquid(T, P):
    return 0

@functor(var='S.s')
def Excess_Solid_Entropy_Ref_Gas(T, P):
    return 0
    
@functor(var='S.g')
def Excess_Gas_Entropy_Ref_Gas(T, P, eos, S_dep_ref_g):
    return eos.to_TP(T, P).S_dep_g - S_dep_ref_g

@functor(var='S.g')
def Excess_Gas_Entropy_Ref_Liquid(T, P, eos, S_dep_T_ref_Pb, 
                                  S_dep_ref_l, S_dep_Tb_Pb_g):
    return S_dep_T_ref_Pb - S_dep_ref_l + eos.to_TP(T, P).S_dep_g - S_dep_Tb_Pb_g

@functor(var='S.g')
def Excess_Gas_Entropy_Ref_Solid(T):
    return 0

ExcessEntropyRefLiquid = PhaseTPFunctorBuilder('S_excess',
                                              Excess_Solid_Entropy_Ref_Liquid,
                                              Excess_Liquid_Entropy_Ref_Liquid,
                                              Excess_Gas_Entropy_Ref_Liquid)

ExcessEntropyRefSolid = PhaseTPFunctorBuilder('S_excess',
                                             Excess_Solid_Entropy_Ref_Solid,
                                             Excess_Liquid_Entropy_Ref_Solid,
                                             Excess_Gas_Entropy_Ref_Solid)

ExcessEntropyRefGas = PhaseTPFunctorBuilder('S_excess',
                                           Excess_Solid_Entropy_Ref_Gas,
                                           Excess_Liquid_Entropy_Ref_Gas,
                                           Excess_Gas_Entropy_Ref_Gas)