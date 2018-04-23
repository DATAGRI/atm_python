class bco:

    cod_bco = []
    nom_client = []    
    saldo = []
    cap = 1000000
    cap_fin = []


    def bco_pres(self):
        cant_sol = int(input('cantidad de dinero a prestar')) 
        if cant_sol > 0:
            self.saldo.append(cant_sol)
            self.cap_fin.append(self.saldo[0]- self.cap)
            print(self.cap_fin) 




