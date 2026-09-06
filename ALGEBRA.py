

def evaluar_tabla_verdad():
    """Valida la equivalencia entre F(A,B,C,D) y la optimizada XNOR(B,D) sin librerías."""
    miniterminos_activos = {0, 2, 5, 7, 8, 10, 13, 15}
    
    print("=" * 65)
    print(" 1. VERIFICACIÓN DE TABLA DE VERDAD: CIRCUITO ORIGINAL VS OPTIMIZADO")
    print("=" * 65)
    
    
    header = f"{'m':<5} | {'A':<2} {'B':<2} {'C':<2} {'D':<2} | {'F_Orig':<7} | {'F_Opt':<6} | {'Estado':<7}"
    print(header)
    print("-" * len(header))
    
    totales_coinciden = True
    
    for a in [0, 1]:
        for b in [0, 1]:
            for c in [0, 1]:
                for d in [0, 1]:
                    
                    m_idx = (a << 3) | (b << 2) | (c << 1) | d
                    
                    
                    f_orig = 1 if m_idx in miniterminos_activos else 0
                    
                    
                    f_opt = 1 if b == d else 0
                    
                    valido = (f_orig == f_opt)
                    if not valido:
                        totales_coinciden = False
                    
                    
                    m_str = f"m{m_idx}"
                    estado_str = "OK" if valido else "ERROR"
                    print(f"{m_str:<5} | {a:<2} {b:<2} {c:<2} {d:<2} | {f_orig:<7} | {f_opt:<6} | {estado_str:<7}")
                    
    print("-" * 65)
    if totales_coinciden:
        print("RESULTADO: ¡Simplificación Matemática Verificada Exitosamente!")
        print("La función F(A,B,C,D) equivale exactamente a la compuerta XNOR(B, D).")
    else:
        print("RESULTADO: Se encontraron discrepancias en la tabla de verdad.")
    print("=" * 65 + "\n")



class AuditoriaPredicados:
    """Modelo formal en Python puro para la evaluación de políticas de seguridad."""
    
    def __init__(self, servidores, procesos, usuarios, ejecuciones, verificados, admins, accesos_escritura):
        self.S = set(servidores)         
        self.P = set(procesos)           
        self.U = set(usuarios)           
        self.E = set(ejecuciones)        
        self.V = set(verificados)       
        self.A = set(admins)            
        self.W = set(accesos_escritura)  

    def evaluar_regla_original(self):
        """
        ∀s ∈ S [ (∃p ∈ P (E(s,p) ∧ ¬V(p))) ⇒ ∃u ∈ U (¬A(u) ∧ W(u,s)) ]
        """
        for s in self.S:
            ejecuta_no_verificado = any((s, p) in self.E and p not in self.V for p in self.P)
            if ejecuta_no_verificado:
                tiene_usuario_no_admin_write = any(
                    u not in self.A and (u, s) in self.W for u in self.U
                )
                if not tiene_usuario_no_admin_write:
                    return False, f"Servidor '{s}' viola la regla de auditoría."
        return True, "Todos los servidores cumplen la política."

    def evaluar_negacion_equivalente(self):
        """
        ∃s ∈ S [ ∃p ∈ P (E(s,p) ∧ ¬V(p)) ∧ ∀u ∈ U (W(u,s) ⇒ A(u)) ]
        """
        for s in self.S:
            ejecuta_no_verificado = any((s, p) in self.E and p not in self.V for p in self.P)
            if ejecuta_no_verificado:
                todos_write_son_admin = all(
                    u in self.A for u in self.U if (u, s) in self.W
                )
                if todos_write_son_admin:
                    return True, f"Infracción detectada en el servidor '{s}' (Negación es Verdadera)."
        return False, "No se detectaron infracciones (Negación es Falsa)."


def simular_auditoria_seguridad():
    print("=" * 65)
    print(" 2. EVALUACIÓN DE REGLAS DE AUDITORÍA Y SU NEGACIÓN DE MORGAN")
    print("=" * 6
          
    escenario_valido = AuditoriaPredicados(
        servidores=['srv_app_01', 'srv_db_01'],
        procesos=['script_unverified', 'daemon_core'],
        usuarios=['admin_sys', 'operador_juan'],
        ejecuciones=[('srv_app_01', 'script_unverified')],
        verificados=['daemon_core'],
        admins=['admin_sys'],
        accesos_escritura=[('operador_juan', 'srv_app_01'), ('admin_sys', 'srv_db_01')]
    )
    
    cumple_a, msg_a1 = escenario_valido.evaluar_regla_original()
    neg_a, msg_a2 = escenario_valido.evaluar_negacion_equivalente()
    
    print("Escenario A (Configuración Conforme):")
    print(f" - Regla Original: {'CUMPLIDA' if cumple_a else 'VIOLADA'} -> {msg_a1}")
    print(f" - Negación De Morgan: {neg_a} -> {msg_a2}\n")


    escenario_infraccion = AuditoriaPredicados(
        servidores=['srv_critico_01'],
        procesos=['malware_process'],
        usuarios=['admin_sys', 'usuario_invitado'],
        ejecuciones=[('srv_critico_01', 'malware_process')],
        verificados=[],
        admins=['admin_sys'],
        accesos_escritura=[('admin_sys', 'srv_critico_01')]
    )
    
    cumple_b, msg_b1 = escenario_infraccion.evaluar_regla_original()
    neg_b, msg_b2 = escenario_infraccion.evaluar_negacion_equivalente()
    
    print("Escenario B (Configuración No Conforme / Infracción):")
    print(f" - Regla Original: {'CUMPLIDA' if cumple_b else 'VIOLADA'} -> {msg_b1}")
    print(f" - Negación De Morgan: {neg_b} -> {msg_b2}")
    print("=" * 65)


if __name__ == '__main__':
    evaluar_tabla_verdad()
    simular_auditoria_seguridad()
