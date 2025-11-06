from servidor import Servidor

serv = Servidor("localhost",9000)  #cada protocolo tem uma porta padrão 
                                   #-> uso de porta com numero maior para evitar conflito com serivço ja executado 
serv.start()

