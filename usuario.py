class user:
    id_user = 19931
    nombre = 'Irwin'
    saldo = []
    nro_cta = 4152452 

    def ret_mony (self):
        if self.nro_cta == 4152452 and self.id_user == 19931:
            print('Bienvenido usuario')
            print('su saldo es {}:'.format(self.saldo[0]))
        else: 
            print('usted no esta registrado en el sistema')


