from modulos import Casa, Pessoa


casa_da_julia = Casa()
tiago = Pessoa('Tiago')

# associação entre as classes
tiago.set_local(casa_da_julia)
casa_da_julia.set_proprietario(tiago)

proprietario = casa_da_julia.get_proprietario()
proprietario.se_apresentar()
tiago.apresentar_local()