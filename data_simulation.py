
import numpy as np
from itertools import product

import functools
from itertools import product

d = 2

def multikron(*args):
    dtype = np.result_type(*args)
    return functools.reduce(np.kron, args, np.array(1, dtype=dtype)) 

def convert_binary_to_fock(clicks_binary:np.ndarray):
    nsettings, nshots, dim_tot = clicks_binary.shape
    nqubits = int(np.log(dim_tot) / np.log(d))
    fock_states = np.tile(list(product(range(d), repeat=nqubits)), (nsettings * nshots, 1))
    fock_states = fock_states.reshape(nsettings, nshots, d**nqubits, nqubits)
    return fock_states[clicks_binary.astype(bool)].reshape(nsettings, nshots, nqubits)

def draw_settings_clicks(
        nqubits:int,
        nsettings:int,
        nshots:int,
        allprobs:np.ndarray,
        seed=None
    ):
    rng = np.random.default_rng(seed = seed)
    rand_settings = rng.integers(0, (d + 1) ** nqubits, size = nsettings)
    clicks_binary = rng.multinomial(1, allprobs[rand_settings], size = (nshots, nsettings)).transpose(1,0,2)
    rand_settings_per_qubit = np.take(list(product(range(d+1), repeat = nqubits)), rand_settings, axis=0)
    return rand_settings_per_qubit, convert_binary_to_fock(clicks_binary)

def calc_all_probs_from_state_vector(
        nqubits:int,
        state_vector:np.ndarray,
        unitary_ensemble:np.ndarray
    ) -> np.ndarray:
    all_probs = np.array([
        np.abs(multikron(*np.take(unitary_ensemble, settings, axis=0)) @ state_vector) ** 2
        for settings in product(range(d + 1), repeat = nqubits)
    ])
    return all_probs / np.sum(all_probs, axis=1).reshape(-1,1) # In case of rounding issues.

def calc_all_probs_from_density_matrix(
        nqubits,
        density_matrix:np.ndarray,
        unitary_ensemble:np.ndarray,
    ) -> np.ndarray:
    all_probs = np.real(np.array([
        np.diag(multikron(*np.take(unitary_ensemble, s, axis=0)) @ density_matrix @ multikron(*np.take(unitary_ensemble, s, axis=0)).conj().T)
        for s in product(range(d+1), repeat = nqubits)
    ]))
    all_probs = np.round(all_probs, 15)
    return all_probs / np.sum(all_probs, axis=1).reshape(-1,1) # In case of rounding issues.

def data_simulation_multi_q(rho, unitary_ensemble, N):
    nqubits = int(np.log2(len(rho)))
    all_probs = calc_all_probs_from_density_matrix(nqubits, rho, unitary_ensemble)
    settings, clicks = draw_settings_clicks(nqubits,N, 1, all_probs)
    return np.array(list(zip(settings, clicks.reshape(settings.shape))))