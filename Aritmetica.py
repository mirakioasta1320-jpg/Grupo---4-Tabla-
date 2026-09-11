def evaluar_acceso(p: bool, q: bool, r: bool, s: bool) -> bool:
    """
    Evalúa la regla de negocio del sistema CloudSec.
    p: Es Administrador del sistema
    q: Posee una Credencial Activa
    r: Supera la Verificación Biométrica
    s: Alarma de Emergencia del edificio está ACTIVADA
    """

    acceso = (p or (q and r)) and not s
    return acceso


def generar_tabla_verdad_cloudsec():
    """Genera la tabla de verdad completa de 16 filas para las variables p, q, r, s."""
    print("=" * 75)
    print(" TABLA DE VERDAD COMPLETA (16 FILAS) - SISTEMA CLOUDSEC")
    print(" Expresión: [p v (q ^ r)] ^ ~s")
    print("=" * 75)
    
    header = f"{'Fila':<5} | {'p':<2} {'q':<2} {'r':<2} {'s':<2} | {'q ^ r':<7} | {'p v (q ^ r)':<13} | {'~s':<4} | {'Acceso':<8}"
    print(header)
    print("-" * len(header))
    
    fila = 1

    for p in [True, False]:
        for q in [True, False]:
            for r in [True, False]:
                for s in [True, False]:
                    
                    q_and_r = q and r
                    p_or_q_and_r = p or q_and_r
                    not_s = not s
                    resultado = evaluar_acceso(p, q, r, s)
                    

                    p_str = 'V' if p else 'F'
                    q_str = 'V' if q else 'F'
                    r_str = 'V' if r else 'F'
                    s_str = 'V' if s else 'F'
                    qr_str = 'V' if q_and_r else 'F'
                    pqr_str = 'V' if p_or_q_and_r else 'F'
                    nots_str = 'V' if not_s else 'F'
                    res_str = 'VERDADERO' if resultado else 'FALSO'
                    
                    print(f"{fila:<5} | {p_str:<2} {q_str:<2} {r_str:<2} {s_str:<2} | {qr_str:<7} | {pqr_str:<13} | {nots_str:<4} | {res_str:<8}")
                    fila += 1
                    
    print("=" * 75 + "\n")


if __name__ == "__main__":

    generar_tabla_verdad_cloudsec()
    
    print("--- MATRIZ DE PRUEBAS (CASOS BORDE - PASO 3) ---")

    print(f"Caso 1 (Admin=V, Cred=F, Bio=F, Alarma=F): {evaluar_acceso(True, False, False, False)}")
    

    print(f"Caso 2 (Admin=V, Cred=F, Bio=F, Alarma=V): {evaluar_acceso(True, False, False, True)}")
    

    print(f"Caso 3 (Admin=F, Cred=V, Bio=V, Alarma=F): {evaluar_acceso(False, True, True, False)}")
    

    print(f"Caso 4 (Admin=F, Cred=V, Bio=F, Alarma=F): {evaluar_acceso(False, True, False, False)}")
    

    print(f"Caso 5 (Admin=V, Cred=V, Bio=V, Alarma=V): {evaluar_acceso(True, True, True, True)}")
    print("=" * 75 + "\n")

if __name__ == '__main__':
    evaluar_tabla_verdad_cloudsec()
