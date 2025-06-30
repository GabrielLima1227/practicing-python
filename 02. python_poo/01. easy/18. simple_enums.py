class StatusPedido:
    PENDENTE = "Pendente"
    PROCESSANDO = "Processando"
    ENVIADO = "Enviado"
    ENTREGUE = "Entregue"
    CANCELADO = "Cancelado"
    STATUS_VALIDOS = {PENDENTE, PROCESSANDO, ENVIADO, ENTREGUE, CANCELADO}

class Pedido:
    def __init__(self, id: int):
        self.id = id
        self.status = StatusPedido.PENDENTE
        print(f"Pedido {self.id} criado com status: {self.status}")

    def __str__(self):
        return f"Pedido ID: {self.id}, Status Atual: {self.status}"

    def alterar_status(self, novo_status: str) -> None:
        if novo_status in StatusPedido.STATUS_VALIDOS:
            self.status = novo_status
            print(f"Status do Pedido {self.id} alterado para: {self.status}")
        else:
            print(f"Erro: '{novo_status}' não é um status de pedido válido. "
                f"Status válidos são: {', '.join(StatusPedido.STATUS_VALIDOS)}")


pedido1 = Pedido(id=101)
print(pedido1)

pedido1.alterar_status(StatusPedido.PROCESSANDO)
print(pedido1)

pedido1.alterar_status(StatusPedido.ENVIADO)
print(pedido1)

pedido1.alterar_status("EmTrânsito")
print(pedido1)

pedido1.alterar_status(StatusPedido.ENTREGUE)
print(pedido1)

pedido2 = Pedido(id=102)
pedido2.alterar_status(StatusPedido.CANCELADO)
print(pedido2)