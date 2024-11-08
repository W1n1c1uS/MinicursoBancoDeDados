import DAO


#cadastro_usuario = DAO.inserir_usuario("tiago", "tiago@gmail.com", "12345")

busca_usuario = DAO.buscar_usuario("tiago")

listar_usuarios = DAO.listar_usuarios()

atualizar_usuario = DAO.atualizar_usuario(2, "tiago", "tiago@gmail.com")

#print(listar_usuarios)

deletar_usuario = DAO.deletar_usuario(1)