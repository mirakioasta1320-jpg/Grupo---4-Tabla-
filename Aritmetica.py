def evaluar_tabla_verdad_cloudsec():
    """Construye y evalúa la tabla de verdad de 16 filas para el sistema CloudSec."""
    print("=" * 75)
    print(" TABLA DE VERDAD COMPLETA (16 FILAS) - SISTEMA CLOUDSEC")
    print(" Fórmula: A(p, q, r, s) = [p OR (q AND r)] AND NOT s")
    print("=" * 75)
    
    header = f"{'Fila':<5} | {'p':<2} {'q':<2} {'r':<2} {'s':<2} | {'q ^ r':<7} | {'p v (q ^ r)':<13} | {'~s':<4} | {'Acceso (A)':<10}"
    print(header)
    print("-" * len(header))
    
    resultados_totales = []
    fila_num = 1
    

    for p in [True, False]:
        for q in [True, False]:
            for r in [True, False]:
                for s in [True, False]:
                    

                    q_and_r = q and r
                    p_or_q_and_r = p or q_and_r
                    not_s = not s
                    acceso = p_or_q_and_r and not_s
                    
                    resultados_totales.append(acceso)
                    

                    p_str = 'V' if p else 'F'
                    q_str = 'V' if q else 'F'
                    r_str = 'V' if r else 'F'
                    s_str = 'V' if s else 'F'
                    qr_str = 'V' if q_and_r else 'F'
                    pqr_str = 'V' if p_or_q_and_r else 'F'
                    nots_str = 'V' if not_s else 'F'
                    acc_str = 'VERDADERO' if acceso else 'FALSO'
                    
                    print(f"{fila_num:<5} | {p_str:<2} {q_str:<2} {r_str:<2} {s_str:<2} | {qr_str:<7} | {pqr_str:<13} | {nots_str:<4} | {acc_str:<10}")
                    fila_num += 1

    print("-" * 75)
    
    tiene_verdaderos = True in resultados_totales
    tiene_falsos = False in resultados_totales
    
    if tiene_verdaderos and tiene_falsos:
        clasificacion = "CONTINGENCIA"
    elif tiene_verdaderos:
        clasificacion = "TAUTOLOGÍA"
    else:
        clasificacion = "CONTRADICCIÓN"
        
    print(f"ANÁLISIS FORMAL: La proposición se clasifica como una {clasificacion}.")
    print(f"Total de casos con Acceso Permitido (V): {resultados_totales.count(True)}")
    print(f"Total de casos con Acceso Denegado (F): {resultados_totales.count(False)}")
    print("=" * 75 + "\n")

if __name__ == '__main__':
    evaluar_tabla_verdad_cloudsec()
